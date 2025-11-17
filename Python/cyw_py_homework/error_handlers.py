"""
全局异常处理
"""
from flask import jsonify, request
from werkzeug.exceptions import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from utils import success_response, error_response
from utils.exceptions import BusinessException, ValidationError

def register_error_handlers(app):
    """注册全局异常处理器"""

    @app.errorhandler(BusinessException)
    def handle_business_exception(e):
        """处理业务异常"""
        return error_response(e.message, e.status_code, e.error_code)

    @app.errorhandler(ValidationError)
    def handle_validation_error(e):
        """处理验证错误"""
        return error_response(e.message, 400, "VALIDATION_ERROR")

    @app.errorhandler(404)
    def handle_not_found(e):
        """处理404错误"""
        return error_response("API接口不存在", 404, "NOT_FOUND")

    @app.errorhandler(500)
    def handle_internal_error(e):
        """处理500错误"""
        return error_response("服务器内部错误", 500, "INTERNAL_ERROR")

    @app.errorhandler(SQLAlchemyError)
    def handle_database_error(e):
        """处理数据库错误"""
        return error_response("数据库操作失败", 500, "DATABASE_ERROR")

    @app.errorhandler(Exception)
    def handle_general_error(e):
        """处理未捕获的异常"""
        if request.environ.get('FLASK_ENV') == 'development':
            # 开发环境显示详细错误信息
            return error_response(f"服务器错误: {str(e)}", 500, "UNKNOWN_ERROR")
        else:
            # 生产环境隐藏具体错误信息
            return error_response("服务器内部错误", 500, "INTERNAL_ERROR")

    return app
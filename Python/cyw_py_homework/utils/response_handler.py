"""
响应处理工具
"""
from flask import jsonify
from typing import Any, Optional

def success_response(data: Any = None, message: str = "操作成功", status_code: int = 200):
    """
    成功响应

    Args:
        data: 返回的数据
        message: 响应消息
        status_code: HTTP状态码
    """
    response = {
        'success': True,
        'message': message
    }

    if data is not None:
        response['data'] = data

    return jsonify(response), status_code

def error_response(message: str = "操作失败", status_code: int = 400, error_code: Optional[str] = None):
    """
    错误响应

    Args:
        message: 错误消息
        status_code: HTTP状态码
        error_code: 错误代码
    """
    response = {
        'success': False,
        'message': message
    }

    if error_code:
        response['error_code'] = error_code

    return jsonify(response), status_code

def paginated_response(data: list, pagination: dict, message: str = "查询成功", status_code: int = 200):
    """
    分页响应

    Args:
        data: 数据列表
        pagination: 分页信息
        message: 响应消息
        status_code: HTTP状态码
    """
    response = {
        'success': True,
        'message': message,
        'data': data,
        'pagination': pagination
    }

    return jsonify(response), status_code
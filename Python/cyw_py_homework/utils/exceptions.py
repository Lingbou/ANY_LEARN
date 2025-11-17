"""
自定义异常类
"""

class BusinessException(Exception):
    """业务异常"""

    def __init__(self, message: str, error_code: str = None, status_code: int = 400):
        super().__init__(message)
        self.message = message
        self.error_code = error_code
        self.status_code = status_code

class ValidationError(BusinessException):
    """验证错误"""

    def __init__(self, message: str, field: str = None):
        super().__init__(message, "VALIDATION_ERROR", 400)
        self.field = field

class NotFoundError(BusinessException):
    """资源不存在错误"""

    def __init__(self, message: str = "资源不存在"):
        super().__init__(message, "NOT_FOUND", 404)

class ConflictError(BusinessException):
    """冲突错误（如资源重复）"""

    def __init__(self, message: str = "资源冲突"):
        super().__init__(message, "CONFLICT", 409)

class InsufficientStockError(BusinessException):
    """库存不足错误"""

    def __init__(self, current_stock: int, requested: int):
        message = f"库存不足，当前库存：{current_stock}，请求：{requested}"
        super().__init__(message, "INSUFFICIENT_STOCK", 400)
        self.current_stock = current_stock
        self.requested = requested
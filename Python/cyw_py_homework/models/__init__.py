"""
数据库模型初始化
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# 导入所有模型
from .product import Product
from .stock import Stock
from .stock_log import StockLog

__all__ = ['db', 'Product', 'Stock', 'StockLog']
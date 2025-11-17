"""
商品模型
"""
from datetime import datetime
from decimal import Decimal
from . import db

class Product(db.Model):
    """商品模型"""
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, comment='商品名称')
    description = db.Column(db.Text, comment='商品描述')
    price = db.Column(db.Numeric(10, 2), nullable=False, comment='商品价格')
    category = db.Column(db.String(50), comment='商品分类')
    sku = db.Column(db.String(50), unique=True, nullable=False, comment='商品SKU')
    created_at = db.Column(db.DateTime, default=datetime.utcnow, comment='创建时间')
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, comment='更新时间')

    # 关联库存表
    stock = db.relationship('Stock', backref='product', lazy=True, uselist=False)

    def to_dict(self):
        """转换为字典"""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': float(self.price),
            'category': self.category,
            'sku': self.sku,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'stock_quantity': self.stock.quantity if self.stock else 0
        }

    def __repr__(self):
        return f'<Product {self.name}>'
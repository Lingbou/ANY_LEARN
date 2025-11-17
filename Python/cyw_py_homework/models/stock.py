"""
库存模型
"""
from datetime import datetime
from . import db

class Stock(db.Model):
    """库存模型"""
    __tablename__ = 'stock'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False, unique=True, comment='商品ID')
    quantity = db.Column(db.Integer, default=0, nullable=False, comment='库存数量')
    min_quantity = db.Column(db.Integer, default=0, comment='最低库存警戒线')
    max_quantity = db.Column(db.Integer, comment='最高库存')
    location = db.Column(db.String(100), comment='库存位置')
    created_at = db.Column(db.DateTime, default=datetime.utcnow, comment='创建时间')
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, comment='更新时间')

    def to_dict(self):
        """转换为字典"""
        return {
            'id': self.id,
            'product_id': self.product_id,
            'product_name': self.product.name if self.product else None,
            'quantity': self.quantity,
            'min_quantity': self.min_quantity,
            'max_quantity': self.max_quantity,
            'location': self.location,
            'is_low_stock': self.quantity <= self.min_quantity if self.min_quantity else False,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

    def __repr__(self):
        return f'<Stock {self.product_id}: {self.quantity}>'
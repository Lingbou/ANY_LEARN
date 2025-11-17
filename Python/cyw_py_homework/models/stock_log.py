"""
库存变动记录模型
"""
from datetime import datetime
from . import db

class StockLog(db.Model):
    """库存变动记录模型"""
    __tablename__ = 'stock_logs'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False, comment='商品ID')
    action = db.Column(db.Enum('in', 'out', 'adjust'), nullable=False, comment='操作类型：入库/出库/调整')
    quantity = db.Column(db.Integer, nullable=False, comment='变动数量')
    before_quantity = db.Column(db.Integer, nullable=False, comment='变动前数量')
    after_quantity = db.Column(db.Integer, nullable=False, comment='变动后数量')
    reason = db.Column(db.String(200), comment='变动原因')
    operator = db.Column(db.String(50), comment='操作人')
    created_at = db.Column(db.DateTime, default=datetime.utcnow, comment='创建时间')

    # 关联商品
    product = db.relationship('Product', backref='stock_logs')

    def to_dict(self):
        """转换为字典"""
        return {
            'id': self.id,
            'product_id': self.product_id,
            'product_name': self.product.name if self.product else None,
            'action': self.action,
            'quantity': self.quantity,
            'before_quantity': self.before_quantity,
            'after_quantity': self.after_quantity,
            'reason': self.reason,
            'operator': self.operator,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

    def __repr__(self):
        return f'<StockLog {self.product_id}: {self.action} {self.quantity}>'
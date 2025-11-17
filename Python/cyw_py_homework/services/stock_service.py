"""
库存服务层
"""
from datetime import datetime
from typing import Dict, Optional, List
from models import db, Product, Stock, StockLog

class StockService:
    """库存服务类"""

    @staticmethod
    def get_all_stock(page: int = 1, per_page: int = 10, low_stock: Optional[bool] = False) -> Dict:
        """获取所有库存信息"""
        query = Stock.query.join(Product)

        if low_stock:
            query = query.filter(Stock.quantity <= Stock.min_quantity)

        stock_list = query.paginate(
            page=page, per_page=per_page, error_out=False
        )

        return {
            'success': True,
            'data': [stock.to_dict() for stock in stock_list.items],
            'pagination': {
                'page': page,
                'per_page': per_page,
                'total': stock_list.total,
                'pages': stock_list.pages
            }
        }

    @staticmethod
    def get_product_stock(product_id: int) -> Dict:
        """获取单个商品的库存信息"""
        product = Product.query.get(product_id)
        if not product:
            return {
                'success': False,
                'message': '商品不存在'
            }

        if not product.stock:
            # 如果没有库存记录，创建一个默认的
            stock = Stock(
                product_id=product_id,
                quantity=0,
                min_quantity=0
            )
            db.session.add(stock)
            db.session.commit()

        return {
            'success': True,
            'data': product.stock.to_dict()
        }

    @staticmethod
    def add_stock(data: Dict) -> Dict:
        """入库操作"""
        # 验证必填字段
        if not data.get('product_id') or not data.get('quantity'):
            return {
                'success': False,
                'message': '商品ID和数量为必填字段'
            }

        if data['quantity'] <= 0:
            return {
                'success': False,
                'message': '入库数量必须大于0'
            }

        product = Product.query.get(data['product_id'])
        if not product:
            return {
                'success': False,
                'message': '商品不存在'
            }

        try:
            # 获取或创建库存记录
            stock = product.stock
            if not stock:
                stock = Stock(
                    product_id=data['product_id'],
                    quantity=0,
                    min_quantity=data.get('min_quantity', 0)
                )
                db.session.add(stock)

            before_quantity = stock.quantity
            stock.quantity += data['quantity']
            stock.updated_at = datetime.utcnow()

            # 创建库存变动记录
            log = StockLog(
                product_id=data['product_id'],
                action='in',
                quantity=data['quantity'],
                before_quantity=before_quantity,
                after_quantity=stock.quantity,
                reason=data.get('reason', '入库操作'),
                operator=data.get('operator', '系统')
            )
            db.session.add(log)

            db.session.commit()

            return {
                'success': True,
                'message': '入库成功',
                'data': {
                    'stock': stock.to_dict(),
                    'log': log.to_dict()
                }
            }

        except Exception as e:
            db.session.rollback()
            return {
                'success': False,
                'message': f'入库失败: {str(e)}'
            }

    @staticmethod
    def reduce_stock(data: Dict) -> Dict:
        """出库操作"""
        # 验证必填字段
        if not data.get('product_id') or not data.get('quantity'):
            return {
                'success': False,
                'message': '商品ID和数量为必填字段'
            }

        if data['quantity'] <= 0:
            return {
                'success': False,
                'message': '出库数量必须大于0'
            }

        product = Product.query.get(data['product_id'])
        if not product:
            return {
                'success': False,
                'message': '商品不存在'
            }

        # 获取库存记录
        stock = product.stock
        if not stock:
            return {
                'success': False,
                'message': '该商品没有库存记录'
            }

        # 检查库存是否充足
        if stock.quantity < data['quantity']:
            return {
                'success': False,
                'message': f'库存不足，当前库存：{stock.quantity}，请求出库：{data["quantity"]}'
            }

        try:
            before_quantity = stock.quantity
            stock.quantity -= data['quantity']
            stock.updated_at = datetime.utcnow()

            # 创建库存变动记录
            log = StockLog(
                product_id=data['product_id'],
                action='out',
                quantity=data['quantity'],
                before_quantity=before_quantity,
                after_quantity=stock.quantity,
                reason=data.get('reason', '出库操作'),
                operator=data.get('operator', '系统')
            )
            db.session.add(log)

            db.session.commit()

            return {
                'success': True,
                'message': '出库成功',
                'data': {
                    'stock': stock.to_dict(),
                    'log': log.to_dict()
                }
            }

        except Exception as e:
            db.session.rollback()
            return {
                'success': False,
                'message': f'出库失败: {str(e)}'
            }

    @staticmethod
    def adjust_stock(data: Dict) -> Dict:
        """库存调整操作"""
        # 验证必填字段
        if not data.get('product_id') or data.get('quantity') is None:
            return {
                'success': False,
                'message': '商品ID和调整数量为必填字段'
            }

        product = Product.query.get(data['product_id'])
        if not product:
            return {
                'success': False,
                'message': '商品不存在'
            }

        try:
            # 获取或创建库存记录
            stock = product.stock
            if not stock:
                stock = Stock(
                    product_id=data['product_id'],
                    quantity=0,
                    min_quantity=data.get('min_quantity', 0)
                )
                db.session.add(stock)

            before_quantity = stock.quantity
            stock.quantity = data['quantity']
            stock.updated_at = datetime.utcnow()

            # 创建库存变动记录
            log = StockLog(
                product_id=data['product_id'],
                action='adjust',
                quantity=data['quantity'] - before_quantity,
                before_quantity=before_quantity,
                after_quantity=stock.quantity,
                reason=data.get('reason', '库存调整'),
                operator=data.get('operator', '系统')
            )
            db.session.add(log)

            db.session.commit()

            return {
                'success': True,
                'message': '库存调整成功',
                'data': {
                    'stock': stock.to_dict(),
                    'log': log.to_dict()
                }
            }

        except Exception as e:
            db.session.rollback()
            return {
                'success': False,
                'message': f'库存调整失败: {str(e)}'
            }

    @staticmethod
    def get_low_stock() -> Dict:
        """获取低库存商品"""
        try:
            stock_list = Stock.query.filter(
                Stock.quantity <= Stock.min_quantity,
                Stock.min_quantity > 0
            ).join(Product).all()

            return {
                'success': True,
                'data': [stock.to_dict() for stock in stock_list]
            }

        except Exception as e:
            return {
                'success': False,
                'message': f'查询失败: {str(e)}'
            }
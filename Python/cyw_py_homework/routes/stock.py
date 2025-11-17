"""
库存管理路由
"""
from flask import Blueprint, request, jsonify
from datetime import datetime
from models import db, Product, Stock, StockLog

stock_bp = Blueprint('stock', __name__)

@stock_bp.route('/', methods=['GET'])
def get_stock():
    """获取所有库存信息"""
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        low_stock = request.args.get('low_stock', type=bool)

        query = Stock.query.join(Product)

        if low_stock:
            query = query.filter(Stock.quantity <= Stock.min_quantity)

        stock_list = query.paginate(
            page=page, per_page=per_page, error_out=False
        )

        return jsonify({
            'success': True,
            'data': [stock.to_dict() for stock in stock_list.items],
            'pagination': {
                'page': page,
                'per_page': per_page,
                'total': stock_list.total,
                'pages': stock_list.pages
            }
        })
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@stock_bp.route('/product/<int:product_id>', methods=['GET'])
def get_product_stock(product_id):
    """获取单个商品的库存信息"""
    try:
        product = Product.query.get_or_404(product_id)
        if not product.stock:
            # 如果没有库存记录，创建一个默认的
            stock = Stock(
                product_id=product_id,
                quantity=0,
                min_quantity=0
            )
            db.session.add(stock)
            db.session.commit()

        return jsonify({
            'success': True,
            'data': product.stock.to_dict()
        })
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@stock_bp.route('/add', methods=['POST'])
def add_stock():
    """入库操作"""
    try:
        data = request.get_json()

        # 验证必填字段
        if not data.get('product_id') or not data.get('quantity'):
            return jsonify({
                'success': False,
                'message': '商品ID和数量为必填字段'
            }), 400

        if data['quantity'] <= 0:
            return jsonify({
                'success': False,
                'message': '入库数量必须大于0'
            }), 400

        product = Product.query.get_or_404(data['product_id'])

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

        return jsonify({
            'success': True,
            'message': '入库成功',
            'data': {
                'stock': stock.to_dict(),
                'log': log.to_dict()
            }
        })

    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500

@stock_bp.route('/reduce', methods=['POST'])
def reduce_stock():
    """出库操作"""
    try:
        data = request.get_json()

        # 验证必填字段
        if not data.get('product_id') or not data.get('quantity'):
            return jsonify({
                'success': False,
                'message': '商品ID和数量为必填字段'
            }), 400

        if data['quantity'] <= 0:
            return jsonify({
                'success': False,
                'message': '出库数量必须大于0'
            }), 400

        product = Product.query.get_or_404(data['product_id'])

        # 获取库存记录
        stock = product.stock
        if not stock:
            return jsonify({
                'success': False,
                'message': '该商品没有库存记录'
            }), 400

        # 检查库存是否充足
        if stock.quantity < data['quantity']:
            return jsonify({
                'success': False,
                'message': f'库存不足，当前库存：{stock.quantity}，请求出库：{data["quantity"]}'
            }), 400

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

        return jsonify({
            'success': True,
            'message': '出库成功',
            'data': {
                'stock': stock.to_dict(),
                'log': log.to_dict()
            }
        })

    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500

@stock_bp.route('/adjust', methods=['POST'])
def adjust_stock():
    """库存调整操作"""
    try:
        data = request.get_json()

        # 验证必填字段
        if not data.get('product_id') or data.get('quantity') is None:
            return jsonify({
                'success': False,
                'message': '商品ID和调整数量为必填字段'
            }), 400

        product = Product.query.get_or_404(data['product_id'])

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

        return jsonify({
            'success': True,
            'message': '库存调整成功',
            'data': {
                'stock': stock.to_dict(),
                'log': log.to_dict()
            }
        })

    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500

@stock_bp.route('/low-stock', methods=['GET'])
def get_low_stock():
    """获取低库存商品"""
    try:
        stock_list = Stock.query.filter(
            Stock.quantity <= Stock.min_quantity,
            Stock.min_quantity > 0
        ).join(Product).all()

        return jsonify({
            'success': True,
            'data': [stock.to_dict() for stock in stock_list]
        })
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500
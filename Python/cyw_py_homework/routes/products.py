"""
商品管理路由
"""
from flask import Blueprint, request, jsonify
from models import db, Product, Stock

product_bp = Blueprint('products', __name__)

@product_bp.route('/', methods=['GET'])
def get_products():
    """获取所有商品"""
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        category = request.args.get('category')

        query = Product.query
        if category:
            query = query.filter_by(category=category)

        products = query.paginate(
            page=page, per_page=per_page, error_out=False
        )

        return jsonify({
            'success': True,
            'data': [product.to_dict() for product in products.items],
            'pagination': {
                'page': page,
                'per_page': per_page,
                'total': products.total,
                'pages': products.pages
            }
        })
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@product_bp.route('/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """获取单个商品"""
    try:
        product = Product.query.get_or_404(product_id)
        return jsonify({
            'success': True,
            'data': product.to_dict()
        })
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@product_bp.route('/', methods=['POST'])
def create_product():
    """创建商品"""
    try:
        data = request.get_json()

        # 验证必填字段
        if not data.get('name') or not data.get('price') or not data.get('sku'):
            return jsonify({
                'success': False,
                'message': '商品名称、价格和SKU为必填字段'
            }), 400

        # 检查SKU是否重复
        if Product.query.filter_by(sku=data['sku']).first():
            return jsonify({
                'success': False,
                'message': 'SKU已存在'
            }), 400

        # 创建商品
        product = Product(
            name=data['name'],
            description=data.get('description', ''),
            price=data['price'],
            category=data.get('category', ''),
            sku=data['sku']
        )

        db.session.add(product)
        db.session.commit()

        # 创建对应的库存记录
        stock = Stock(
            product_id=product.id,
            quantity=0,
            min_quantity=data.get('min_quantity', 0),
            max_quantity=data.get('max_quantity'),
            location=data.get('location', '')
        )
        db.session.add(stock)
        db.session.commit()

        return jsonify({
            'success': True,
            'message': '商品创建成功',
            'data': product.to_dict()
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500

@product_bp.route('/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """更新商品"""
    try:
        product = Product.query.get_or_404(product_id)
        data = request.get_json()

        # 更新商品信息
        if 'name' in data:
            product.name = data['name']
        if 'description' in data:
            product.description = data['description']
        if 'price' in data:
            product.price = data['price']
        if 'category' in data:
            product.category = data['category']
        if 'sku' in data:
            # 检查新SKU是否重复
            existing = Product.query.filter_by(sku=data['sku']).first()
            if existing and existing.id != product_id:
                return jsonify({
                    'success': False,
                    'message': 'SKU已存在'
                }), 400
            product.sku = data['sku']

        # 更新库存信息
        if product.stock:
            if 'min_quantity' in data:
                product.stock.min_quantity = data['min_quantity']
            if 'max_quantity' in data:
                product.stock.max_quantity = data['max_quantity']
            if 'location' in data:
                product.stock.location = data['location']

        db.session.commit()

        return jsonify({
            'success': True,
            'message': '商品更新成功',
            'data': product.to_dict()
        })

    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500

@product_bp.route('/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """删除商品"""
    try:
        product = Product.query.get_or_404(product_id)

        # 检查库存是否为0
        if product.stock and product.stock.quantity > 0:
            return jsonify({
                'success': False,
                'message': '商品库存不为0，无法删除'
            }), 400

        db.session.delete(product)
        db.session.commit()

        return jsonify({
            'success': True,
            'message': '商品删除成功'
        })

    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500

@product_bp.route('/categories', methods=['GET'])
def get_categories():
    """获取所有商品分类"""
    try:
        categories = db.session.query(Product.category).distinct().all()
        category_list = [cat[0] for cat in categories if cat[0]]

        return jsonify({
            'success': True,
            'data': category_list
        })
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500
"""
商品服务层
"""
from typing import List, Dict, Optional
from models import db, Product, Stock

class ProductService:
    """商品服务类"""

    @staticmethod
    def get_all_products(page: int = 1, per_page: int = 10, category: Optional[str] = None) -> Dict:
        """获取所有商品"""
        query = Product.query
        if category:
            query = query.filter_by(category=category)

        products = query.paginate(
            page=page, per_page=per_page, error_out=False
        )

        return {
            'success': True,
            'data': [product.to_dict() for product in products.items],
            'pagination': {
                'page': page,
                'per_page': per_page,
                'total': products.total,
                'pages': products.pages
            }
        }

    @staticmethod
    def get_product_by_id(product_id: int) -> Dict:
        """根据ID获取商品"""
        product = Product.query.get(product_id)
        if not product:
            return {
                'success': False,
                'message': '商品不存在'
            }

        return {
            'success': True,
            'data': product.to_dict()
        }

    @staticmethod
    def create_product(data: Dict) -> Dict:
        """创建商品"""
        # 验证必填字段
        if not data.get('name') or not data.get('price') or not data.get('sku'):
            return {
                'success': False,
                'message': '商品名称、价格和SKU为必填字段'
            }

        # 检查SKU是否重复
        if Product.query.filter_by(sku=data['sku']).first():
            return {
                'success': False,
                'message': 'SKU已存在'
            }

        try:
            # 创建商品
            product = Product(
                name=data['name'],
                description=data.get('description', ''),
                price=data['price'],
                category=data.get('category', ''),
                sku=data['sku']
            )

            db.session.add(product)
            db.session.flush()  # 获取product.id

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

            return {
                'success': True,
                'message': '商品创建成功',
                'data': product.to_dict()
            }

        except Exception as e:
            db.session.rollback()
            return {
                'success': False,
                'message': f'创建失败: {str(e)}'
            }

    @staticmethod
    def update_product(product_id: int, data: Dict) -> Dict:
        """更新商品"""
        product = Product.query.get(product_id)
        if not product:
            return {
                'success': False,
                'message': '商品不存在'
            }

        try:
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
                    return {
                        'success': False,
                        'message': 'SKU已存在'
                    }
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

            return {
                'success': True,
                'message': '商品更新成功',
                'data': product.to_dict()
            }

        except Exception as e:
            db.session.rollback()
            return {
                'success': False,
                'message': f'更新失败: {str(e)}'
            }

    @staticmethod
    def delete_product(product_id: int) -> Dict:
        """删除商品"""
        product = Product.query.get(product_id)
        if not product:
            return {
                'success': False,
                'message': '商品不存在'
            }

        # 检查库存是否为0
        if product.stock and product.stock.quantity > 0:
            return {
                'success': False,
                'message': '商品库存不为0，无法删除'
            }

        try:
            db.session.delete(product)
            db.session.commit()

            return {
                'success': True,
                'message': '商品删除成功'
            }

        except Exception as e:
            db.session.rollback()
            return {
                'success': False,
                'message': f'删除失败: {str(e)}'
            }

    @staticmethod
    def get_categories() -> Dict:
        """获取所有商品分类"""
        try:
            categories = db.session.query(Product.category).distinct().all()
            category_list = [cat[0] for cat in categories if cat[0]]

            return {
                'success': True,
                'data': category_list
            }

        except Exception as e:
            return {
                'success': False,
                'message': f'查询失败: {str(e)}'
            }
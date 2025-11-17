"""
主路由 - 处理前端页面渲染
"""
from flask import Blueprint, render_template, request, jsonify, redirect, url_for

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """首页"""
    return render_template('index.html')

@main_bp.route('/products')
def products():
    """商品管理页面"""
    return render_template('products.html')

@main_bp.route('/stock')
def stock():
    """库存管理页面"""
    return render_template('stock.html')

@main_bp.route('/logs')
def logs():
    """库存变动记录页面"""
    # 获取查询参数
    product_id = request.args.get('product_id', type=int)
    return render_template('logs.html', product_id=product_id)

@main_bp.route('/statistics')
def statistics():
    """统计分析页面"""
    return render_template('statistics.html')

@main_bp.route('/api')
def api_info():
    """API信息页面 - 返回JSON格式"""
    return jsonify({
        'message': 'Inventory Management System API',
        'version': '1.0.0',
        'endpoints': {
            'products': '/api/products',
            'stock': '/api/stock',
            'logs': '/api/logs'
        },
        'web_pages': {
            'home': '/',
            'products': '/products',
            'stock': '/stock',
            'logs': '/logs',
            'statistics': '/statistics'
        }
    })

@main_bp.route('/health')
def health_check():
    """健康检查"""
    return jsonify({'status': 'healthy'})

@main_bp.app_errorhandler(404)
def page_not_found(e):
    """404错误处理"""
    if request.path.startswith('/api/'):
        return jsonify({
            'success': False,
            'message': 'API接口不存在',
            'error_code': 'NOT_FOUND'
        }), 404
    else:
        # 对于网页请求，返回404页面
        return render_template('404.html'), 404

@main_bp.app_errorhandler(500)
def internal_server_error(e):
    """500错误处理"""
    if request.path.startswith('/api/'):
        return jsonify({
            'success': False,
            'message': '服务器内部错误',
            'error_code': 'INTERNAL_ERROR'
        }), 500
    else:
        # 对于网页请求，返回500页面
        return render_template('500.html'), 500
"""
库存记录查询路由
"""
from flask import Blueprint, request, jsonify
from models import db, StockLog

log_bp = Blueprint('logs', __name__)

@log_bp.route('/', methods=['GET'])
def get_stock_logs():
    """获取所有库存变动记录"""
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 20, type=int)
        product_id = request.args.get('product_id', type=int)
        action = request.args.get('action')
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')

        query = StockLog.query

        # 按商品ID筛选
        if product_id:
            query = query.filter_by(product_id=product_id)

        # 按操作类型筛选
        if action:
            query = query.filter_by(action=action)

        # 按时间范围筛选
        if start_date:
            query = query.filter(StockLog.created_at >= start_date)
        if end_date:
            query = query.filter(StockLog.created_at <= end_date)

        # 按创建时间倒序排列
        query = query.order_by(StockLog.created_at.desc())

        logs = query.paginate(
            page=page, per_page=per_page, error_out=False
        )

        return jsonify({
            'success': True,
            'data': [log.to_dict() for log in logs.items],
            'pagination': {
                'page': page,
                'per_page': per_page,
                'total': logs.total,
                'pages': logs.pages
            }
        })
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@log_bp.route('/<int:log_id>', methods=['GET'])
def get_stock_log(log_id):
    """获取单个库存变动记录"""
    try:
        log = StockLog.query.get_or_404(log_id)
        return jsonify({
            'success': True,
            'data': log.to_dict()
        })
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@log_bp.route('/product/<int:product_id>', methods=['GET'])
def get_product_logs(product_id):
    """获取指定商品的库存变动记录"""
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 20, type=int)
        action = request.args.get('action')

        query = StockLog.query.filter_by(product_id=product_id)

        if action:
            query = query.filter_by(action=action)

        query = query.order_by(StockLog.created_at.desc())

        logs = query.paginate(
            page=page, per_page=per_page, error_out=False
        )

        return jsonify({
            'success': True,
            'data': [log.to_dict() for log in logs.items],
            'pagination': {
                'page': page,
                'per_page': per_page,
                'total': logs.total,
                'pages': logs.pages
            }
        })
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@log_bp.route('/statistics', methods=['GET'])
def get_statistics():
    """获取库存变动统计"""
    try:
        # 总入库数量
        total_in = db.session.query(db.func.sum(StockLog.quantity)).filter_by(action='in').scalar() or 0

        # 总出库数量
        total_out = db.session.query(db.func.sum(StockLog.quantity)).filter_by(action='out').scalar() or 0

        # 今日操作次数
        today_logs = StockLog.query.filter(
            db.func.date(StockLog.created_at) == db.func.current_date()
        ).count()

        # 最近7天操作趋势
        from datetime import datetime, timedelta
        seven_days_ago = datetime.utcnow() - timedelta(days=7)

        recent_logs = db.session.query(
            db.func.date(StockLog.created_at).label('date'),
            db.func.count(StockLog.id).label('count')
        ).filter(
            StockLog.created_at >= seven_days_ago
        ).group_by(
            db.func.date(StockLog.created_at)
        ).order_by('date').all()

        trend_data = [
            {'date': str(log.date), 'count': log.count}
            for log in recent_logs
        ]

        return jsonify({
            'success': True,
            'data': {
                'total_in_quantity': total_in,
                'total_out_quantity': total_out,
                'today_operations': today_logs,
                'recent_trend': trend_data
            }
        })
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@log_bp.route('/actions', methods=['GET'])
def get_action_types():
    """获取所有操作类型"""
    try:
        return jsonify({
            'success': True,
            'data': [
                {'value': 'in', 'label': '入库'},
                {'value': 'out', 'label': '出库'},
                {'value': 'adjust', 'label': '调整'}
            ]
        })
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500
"""
库存记录服务层
"""
from datetime import datetime, timedelta
from typing import Dict, Optional
from models import db, StockLog

class LogService:
    """库存记录服务类"""

    @staticmethod
    def get_stock_logs(page: int = 1, per_page: int = 20,
                      product_id: Optional[int] = None,
                      action: Optional[str] = None,
                      start_date: Optional[str] = None,
                      end_date: Optional[str] = None) -> Dict:
        """获取所有库存变动记录"""
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

        return {
            'success': True,
            'data': [log.to_dict() for log in logs.items],
            'pagination': {
                'page': page,
                'per_page': per_page,
                'total': logs.total,
                'pages': logs.pages
            }
        }

    @staticmethod
    def get_stock_log_by_id(log_id: int) -> Dict:
        """获取单个库存变动记录"""
        log = StockLog.query.get(log_id)
        if not log:
            return {
                'success': False,
                'message': '记录不存在'
            }

        return {
            'success': True,
            'data': log.to_dict()
        }

    @staticmethod
    def get_product_logs(product_id: int, page: int = 1, per_page: int = 20,
                        action: Optional[str] = None) -> Dict:
        """获取指定商品的库存变动记录"""
        query = StockLog.query.filter_by(product_id=product_id)

        if action:
            query = query.filter_by(action=action)

        query = query.order_by(StockLog.created_at.desc())

        logs = query.paginate(
            page=page, per_page=per_page, error_out=False
        )

        return {
            'success': True,
            'data': [log.to_dict() for log in logs.items],
            'pagination': {
                'page': page,
                'per_page': per_page,
                'total': logs.total,
                'pages': logs.pages
            }
        }

    @staticmethod
    def get_statistics() -> Dict:
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

            return {
                'success': True,
                'data': {
                    'total_in_quantity': total_in,
                    'total_out_quantity': total_out,
                    'today_operations': today_logs,
                    'recent_trend': trend_data
                }
            }
        except Exception as e:
            return {
                'success': False,
                'message': f'统计失败: {str(e)}'
            }

    @staticmethod
    def get_action_types() -> Dict:
        """获取所有操作类型"""
        return {
            'success': True,
            'data': [
                {'value': 'in', 'label': '入库'},
                {'value': 'out', 'label': '出库'},
                {'value': 'adjust', 'label': '调整'}
            ]
        }
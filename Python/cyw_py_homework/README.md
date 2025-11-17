# Flask 微服务库存管理系统

AI辅助实验项目 - 基于 Flask 的库存管理系统

## 项目概述

这是一个基于 Flask 框架的微服务库存管理系统，提供了完整的商品管理、库存操作和记录查询功能。

## 技术栈

- **后端框架**: Flask 2.3.3
- **数据库**: SQLite (开发) / MySQL (生产)
- **ORM**: SQLAlchemy
- **前端**: 支持 RESTful API，可对接任意前端框架
- **部署**: Gunicorn + Flask

## 项目结构

```
cyw_py_homework/
├── main.py                 # 应用入口
├── config.py              # 配置文件
├── requirements.txt       # 依赖包
├── gunicorn.conf.py      # Gunicorn配置
├── models/               # 数据模型
│   ├── __init__.py
│   ├── product.py       # 商品模型
│   ├── stock.py         # 库存模型
│   └── stock_log.py     # 库存记录模型
├── routes/              # 路由层
│   ├── __init__.py
│   ├── products.py      # 商品路由
│   ├── stock.py        # 库存路由
│   └── logs.py         # 记录路由
├── services/           # 服务层
│   ├── __init__.py
│   ├── product_service.py
│   ├── stock_service.py
│   └── log_service.py
├── utils/              # 工具类
│   ├── __init__.py
│   ├── response_handler.py
│   └── exceptions.py
├── error_handlers.py    # 异常处理
└── templates/          # 模板文件
```

## 环境要求

- Python 3.8+
- pip

## 安装和运行

### 1. 创建虚拟环境

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境 (Linux/Mac)
source venv/bin/activate

# 激活虚拟环境 (Windows)
venv\Scripts\activate
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 环境配置

```bash
# 复制环境配置文件
cp .env.example .env

# 编辑 .env 文件，设置相应的配置值
```

### 4. 运行应用

#### 开发环境运行

```bash
python main.py
```

#### 生产环境部署

```bash
# 使用 Gunicorn 启动
gunicorn --config gunicorn.conf.py main:app

# 或者使用 nohup 后台运行
nohup gunicorn --config gunicorn.conf.py main:app > app.log 2>&1 &
```

## API 文档

### 基础接口

- `GET /` - 系统信息
- `GET /health` - 健康检查

### 商品管理

- `GET /api/products/` - 获取商品列表
- `GET /api/products/{id}` - 获取单个商品
- `POST /api/products/` - 创建商品
- `PUT /api/products/{id}` - 更新商品
- `DELETE /api/products/{id}` - 删除商品
- `GET /api/products/categories` - 获取商品分类

### 库存管理

- `GET /api/stock/` - 获取库存列表
- `GET /api/stock/product/{id}` - 获取单个商品库存
- `POST /api/stock/add` - 入库操作
- `POST /api/stock/reduce` - 出库操作
- `POST /api/stock/adjust` - 库存调整
- `GET /api/stock/low-stock` - 获取低库存商品

### 库存记录

- `GET /api/logs/` - 获取库存变动记录
- `GET /api/logs/{id}` - 获取单条记录
- `GET /api/logs/product/{id}` - 获取指定商品的变动记录
- `GET /api/logs/statistics` - 获取统计信息
- `GET /api/logs/actions` - 获取操作类型

## 请求示例

### 创建商品

```bash
curl -X POST http://localhost:5000/api/products/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "测试商品",
    "description": "这是一个测试商品",
    "price": 99.99,
    "category": "电子产品",
    "sku": "TEST001"
  }'
```

### 入库操作

```bash
curl -X POST http://localhost:5000/api/stock/add \
  -H "Content-Type: application/json" \
  -d '{
    "product_id": 1,
    "quantity": 50,
    "reason": "初始入库"
  }'
```

### 查询库存

```bash
curl http://localhost:5000/api/stock/
```

## 数据库表结构

### products (商品表)

- `id` - 主键
- `name` - 商品名称
- `description` - 商品描述
- `price` - 商品价格
- `category` - 商品分类
- `sku` - 商品SKU
- `created_at` - 创建时间
- `updated_at` - 更新时间

### stock (库存表)

- `id` - 主键
- `product_id` - 商品ID (外键)
- `quantity` - 库存数量
- `min_quantity` - 最低库存警戒线
- `max_quantity` - 最高库存
- `location` - 库存位置
- `created_at` - 创建时间
- `updated_at` - 更新时间

### stock_logs (库存变动记录表)

- `id` - 主键
- `product_id` - 商品ID (外键)
- `action` - 操作类型 (in/out/adjust)
- `quantity` - 变动数量
- `before_quantity` - 变动前数量
- `after_quantity` - 变动后数量
- `reason` - 变动原因
- `operator` - 操作人
- `created_at` - 创建时间

## 开发说明

### 代码结构

项目采用分层架构：
- **Routes**: 路由层，处理HTTP请求和响应
- **Services**: 服务层，包含业务逻辑
- **Models**: 模型层，定义数据结构
- **Utils**: 工具层，提供通用功能

### 异常处理

系统提供了统一的异常处理机制：
- 全局异常处理器
- 自定义业务异常
- 标准化响应格式

### 扩展开发

1. 在 `models/` 中添加新的数据模型
2. 在 `services/` 中实现业务逻辑
3. 在 `routes/` 中创建API接口
4. 在 `main.py` 中注册新的蓝图

## 部署说明

### 生产环境部署

1. 设置环境变量
2. 配置数据库 (建议使用MySQL)
3. 使用 Gunicorn 作为 WSGI 服务器
4. 配置 Nginx 反向代理 (可选)

### 性能优化

- 使用连接池
- 配置适当的 worker 数量
- 启用数据库查询缓存
- 使用 Redis 缓存热点数据

## 许可证

MIT License

## 作者

AI 辅助实验项目
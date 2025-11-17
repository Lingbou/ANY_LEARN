#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
API 测试脚本
测试所有主要功能
"""
import requests
import json
import time

BASE_URL = "http://localhost:5000"

def test_api():
    """测试所有API接口"""

    print("=== Flask 库存管理系统 API 测试 ===\n")

    # 测试1: 系统信息
    print("1. 测试系统信息...")
    response = requests.get(f"{BASE_URL}/")
    print(f"   状态码: {response.status_code}")
    print(f"   响应: {json.dumps(response.json(), indent=2, ensure_ascii=False)}\n")

    # 测试2: 健康检查
    print("2. 测试健康检查...")
    response = requests.get(f"{BASE_URL}/health")
    print(f"   状态码: {response.status_code}")
    print(f"   响应: {json.dumps(response.json(), indent=2, ensure_ascii=False)}\n")

    # 测试3: 创建商品
    print("3. 测试创建商品...")
    product_data = {
        "name": "API测试商品",
        "description": "通过API创建的测试商品",
        "price": 199.99,
        "category": "测试分类",
        "sku": f"API_TEST_{int(time.time())}",
        "min_quantity": 5,
        "location": "测试仓库"
    }

    response = requests.post(f"{BASE_URL}/api/products/", json=product_data)
    print(f"   状态码: {response.status_code}")
    product_response = response.json()
    print(f"   响应: {json.dumps(product_response, indent=2, ensure_ascii=False)}")

    if product_response.get('success'):
        product_id = product_response['data']['id']
        print(f"   商品ID: {product_id}\n")
    else:
        print("   商品创建失败，跳过后续测试\n")
        return

    # 测试4: 获取商品列表
    print("4. 测试获取商品列表...")
    response = requests.get(f"{BASE_URL}/api/products/")
    print(f"   状态码: {response.status_code}")
    products_response = response.json()
    print(f"   商品数量: {products_response.get('pagination', {}).get('total', 0)}")
    print(f"   响应: {json.dumps(products_response, indent=2, ensure_ascii=False)}\n")

    # 测试5: 获取单个商品
    print("5. 测试获取单个商品...")
    response = requests.get(f"{BASE_URL}/api/products/{product_id}")
    print(f"   状态码: {response.status_code}")
    print(f"   响应: {json.dumps(response.json(), indent=2, ensure_ascii=False)}\n")

    # 测试6: 入库操作
    print("6. 测试入库操作...")
    stock_in_data = {
        "product_id": product_id,
        "quantity": 100,
        "reason": "API测试入库",
        "operator": "测试用户"
    }
    response = requests.post(f"{BASE_URL}/api/stock/add", json=stock_in_data)
    print(f"   状态码: {response.status_code}")
    stock_response = response.json()
    print(f"   响应: {json.dumps(stock_response, indent=2, ensure_ascii=False)}\n")

    # 测试7: 获取库存信息
    print("7. 测试获取库存信息...")
    response = requests.get(f"{BASE_URL}/api/stock/")
    print(f"   状态码: {response.status_code}")
    stock_list_response = response.json()
    print(f"   响应: {json.dumps(stock_list_response, indent=2, ensure_ascii=False)}\n")

    # 测试8: 出库操作
    print("8. 测试出库操作...")
    stock_out_data = {
        "product_id": product_id,
        "quantity": 20,
        "reason": "API测试出库",
        "operator": "测试用户"
    }
    response = requests.post(f"{BASE_URL}/api/stock/reduce", json=stock_out_data)
    print(f"   状态码: {response.status_code}")
    print(f"   响应: {json.dumps(response.json(), indent=2, ensure_ascii=False)}\n")

    # 测试9: 获取库存变动记录
    print("9. 测试获取库存变动记录...")
    response = requests.get(f"{BASE_URL}/api/logs/")
    print(f"   状态码: {response.status_code}")
    logs_response = response.json()
    print(f"   记录数量: {logs_response.get('pagination', {}).get('total', 0)}")
    print(f"   响应: {json.dumps(logs_response, indent=2, ensure_ascii=False)}\n")

    # 测试10: 获取统计信息
    print("10. 测试获取统计信息...")
    response = requests.get(f"{BASE_URL}/api/logs/statistics")
    print(f"   状态码: {response.status_code}")
    print(f"   响应: {json.dumps(response.json(), indent=2, ensure_ascii=False)}\n")

    # 测试11: 更新商品
    print("11. 测试更新商品...")
    update_data = {
        "description": "更新后的商品描述",
        "price": 299.99
    }
    response = requests.put(f"{BASE_URL}/api/products/{product_id}", json=update_data)
    print(f"   状态码: {response.status_code}")
    print(f"   响应: {json.dumps(response.json(), indent=2, ensure_ascii=False)}\n")

    # 测试12: 删除商品
    print("12. 测试删除商品...")
    # 首先清空库存
    adjust_data = {
        "product_id": product_id,
        "quantity": 0,
        "reason": "测试删除前清空库存"
    }
    response = requests.post(f"{BASE_URL}/api/stock/adjust", json=adjust_data)

    # 然后删除商品
    response = requests.delete(f"{BASE_URL}/api/products/{product_id}")
    print(f"   状态码: {response.status_code}")
    print(f"   响应: {json.dumps(response.json(), indent=2, ensure_ascii=False)}\n")

    print("=== API 测试完成 ===")

def test_error_cases():
    """测试错误情况"""
    print("\n=== 错误情况测试 ===\n")

    # 测试无效的商品ID
    print("1. 测试无效商品ID...")
    response = requests.get(f"{BASE_URL}/api/products/99999")
    print(f"   状态码: {response.status_code}")
    print(f"   响应: {json.dumps(response.json(), indent=2, ensure_ascii=False)}\n")

    # 测试创建商品缺少必填字段
    print("2. 测试创建商品缺少必填字段...")
    invalid_data = {
        "name": "无效商品"
        # 缺少 price 和 sku
    }
    response = requests.post(f"{BASE_URL}/api/products/", json=invalid_data)
    print(f"   状态码: {response.status_code}")
    print(f"   响应: {json.dumps(response.json(), indent=2, ensure_ascii=False)}\n")

    # 测试库存不足出库
    print("3. 测试库存不足出库...")
    # 先创建一个商品
    product_data = {
        "name": "库存测试商品",
        "price": 10.00,
        "sku": f"STOCK_TEST_{int(time.time())}"
    }
    response = requests.post(f"{BASE_URL}/api/products/", json=product_data)
    if response.json().get('success'):
        product_id = response.json()['data']['id']

        # 尝试出库比库存多的数量
        stock_out_data = {
            "product_id": product_id,
            "quantity": 100,  # 库存为0，出库100
            "reason": "测试库存不足"
        }
        response = requests.post(f"{BASE_URL}/api/stock/reduce", json=stock_out_data)
        print(f"   状态码: {response.status_code}")
        print(f"   响应: {json.dumps(response.json(), indent=2, ensure_ascii=False)}\n")

        # 清理测试数据
        requests.delete(f"{BASE_URL}/api/products/{product_id}")

if __name__ == "__main__":
    try:
        test_api()
        test_error_cases()
    except requests.exceptions.ConnectionError:
        print("错误: 无法连接到服务器。请确保应用正在运行 (http://localhost:5000)")
    except Exception as e:
        print(f"测试过程中发生错误: {str(e)}")
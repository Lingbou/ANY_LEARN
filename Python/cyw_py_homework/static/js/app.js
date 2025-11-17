// 库存管理系统前端 JavaScript

// 全局变量
let currentPage = 1;
let isLoading = false;

// 工具函数
function showLoading() {
    isLoading = true;
    document.getElementById('loadingOverlay').classList.remove('d-none');
}

function hideLoading() {
    isLoading = false;
    document.getElementById('loadingOverlay').classList.add('d-none');
}

function showAlert(message, type = 'info') {
    // 创建提示框
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show`;
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;

    // 添加到页面顶部
    const container = document.querySelector('.container');
    container.insertBefore(alertDiv, container.firstChild);

    // 自动消失
    setTimeout(() => {
        if (alertDiv.parentNode) {
            alertDiv.remove();
        }
    }, 5000);
}

function formatDateTime(dateTimeString) {
    if (!dateTimeString) return '-';
    const date = new Date(dateTimeString);
    return date.toLocaleString('zh-CN', {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit'
    });
}

function formatCurrency(amount) {
    return new Intl.NumberFormat('zh-CN', {
        style: 'currency',
        currency: 'CNY'
    }).format(amount);
}

function renderPagination(pagination, loadFunction) {
    if (pagination.pages <= 1) return '';

    let html = '<nav aria-label="分页导航"><ul class="pagination justify-content-center">';

    // 上一页
    if (pagination.page > 1) {
        html += `<li class="page-item">
            <a class="page-link" href="javascript:void(0)" onclick="${loadFunction.name}(${pagination.page - 1})">上一页</a>
        </li>`;
    }

    // 页码
    let startPage = Math.max(1, pagination.page - 2);
    let endPage = Math.min(pagination.pages, pagination.page + 2);

    for (let i = startPage; i <= endPage; i++) {
        const activeClass = i === pagination.page ? 'active' : '';
        html += `<li class="page-item ${activeClass}">
            <a class="page-link" href="javascript:void(0)" onclick="${loadFunction.name}(${i})">${i}</a>
        </li>`;
    }

    // 下一页
    if (pagination.page < pagination.pages) {
        html += `<li class="page-item">
            <a class="page-link" href="javascript:void(0)" onclick="${loadFunction.name}(${pagination.page + 1})">下一页</a>
        </li>`;
    }

    html += '</ul></nav>';
    return html;
}

// API 请求封装
class ApiClient {
    static async request(url, options = {}) {
        const defaultOptions = {
            headers: {
                'Content-Type': 'application/json',
            },
        };

        const finalOptions = { ...defaultOptions, ...options };

        try {
            const response = await fetch(url, finalOptions);
            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.message || `HTTP error! status: ${response.status}`);
            }

            return data;
        } catch (error) {
            console.error('API request failed:', error);
            throw error;
        }
    }

    static async get(url) {
        return this.request(url);
    }

    static async post(url, data) {
        return this.request(url, {
            method: 'POST',
            body: JSON.stringify(data),
        });
    }

    static async put(url, data) {
        return this.request(url, {
            method: 'PUT',
            body: JSON.stringify(data),
        });
    }

    static async delete(url) {
        return this.request(url, {
            method: 'DELETE',
        });
    }
}

// 表单验证
function validateForm(formId) {
    const form = document.getElementById(formId);
    const inputs = form.querySelectorAll('input[required], select[required], textarea[required]');

    for (let input of inputs) {
        if (!input.value.trim()) {
            input.focus();
            showAlert(`请填写 ${input.previousElementSibling.textContent}`, 'error');
            return false;
        }
    }

    return true;
}

// 数字格式化
function formatNumber(num) {
    return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

// 本地存储管理
class StorageManager {
    static set(key, value) {
        try {
            localStorage.setItem(key, JSON.stringify(value));
        } catch (error) {
            console.error('Failed to save to localStorage:', error);
        }
    }

    static get(key, defaultValue = null) {
        try {
            const item = localStorage.getItem(key);
            return item ? JSON.parse(item) : defaultValue;
        } catch (error) {
            console.error('Failed to get from localStorage:', error);
            return defaultValue;
        }
    }

    static remove(key) {
        try {
            localStorage.removeItem(key);
        } catch (error) {
            console.error('Failed to remove from localStorage:', error);
        }
    }

    static clear() {
        try {
            localStorage.clear();
        } catch (error) {
            console.error('Failed to clear localStorage:', error);
        }
    }
}

// 用户偏好设置
class UserPreferences {
    static setPageSize(pageSize) {
        StorageManager.set('pageSize', pageSize);
    }

    static getPageSize() {
        return StorageManager.get('pageSize', 10);
    }

    static setTheme(theme) {
        StorageManager.set('theme', theme);
        document.body.className = theme;
    }

    static getTheme() {
        return StorageManager.get('theme', 'light');
    }

    static setRecentProducts(products) {
        StorageManager.set('recentProducts', products);
    }

    static getRecentProducts() {
        return StorageManager.get('recentProducts', []);
    }
}

// 搜索功能
class SearchManager {
    constructor(inputSelector, searchFunction, delay = 300) {
        this.input = document.querySelector(inputSelector);
        this.searchFunction = searchFunction;
        this.delay = delay;
        this.timeout = null;

        if (this.input) {
            this.input.addEventListener('input', (e) => {
                this.handleSearch(e.target.value);
            });
        }
    }

    handleSearch(query) {
        clearTimeout(this.timeout);

        if (query.length < 2) {
            return;
        }

        this.timeout = setTimeout(() => {
            this.searchFunction(query);
        }, this.delay);
    }
}

// 数据导出功能
class DataExporter {
    static exportToCSV(data, filename) {
        const csv = this.convertToCSV(data);
        const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
        const link = document.createElement('a');

        if (link.download !== undefined) {
            const url = URL.createObjectURL(blob);
            link.setAttribute('href', url);
            link.setAttribute('download', filename);
            link.style.visibility = 'hidden';
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        }
    }

    static convertToCSV(data) {
        if (!data || data.length === 0) {
            return '';
        }

        const headers = Object.keys(data[0]);
        const csvHeaders = headers.join(',');

        const csvRows = data.map(row => {
            return headers.map(header => {
                const value = row[header];
                return typeof value === 'string' && value.includes(',')
                    ? `"${value.replace(/"/g, '""')}"`
                    : value;
            }).join(',');
        });

        return [csvHeaders, ...csvRows].join('\n');
    }
}

// 实时数据更新
class RealTimeUpdater {
    constructor(updateInterval = 30000) {
        this.updateInterval = updateInterval;
        this.isRunning = false;
        this.intervalId = null;
    }

    start(updateFunction) {
        if (this.isRunning) return;

        this.isRunning = true;
        this.updateFunction = updateFunction;

        // 立即执行一次
        this.updateFunction();

        // 设置定时更新
        this.intervalId = setInterval(() => {
            this.updateFunction();
        }, this.updateInterval);
    }

    stop() {
        if (!this.isRunning) return;

        this.isRunning = false;
        if (this.intervalId) {
            clearInterval(this.intervalId);
            this.intervalId = null;
        }
    }

    toggle(updateFunction) {
        if (this.isRunning) {
            this.stop();
        } else {
            this.start(updateFunction);
        }
    }
}

// 错误处理
window.addEventListener('error', function(event) {
    console.error('Global error:', event.error);
    showAlert('系统发生错误，请刷新页面重试', 'error');
});

window.addEventListener('unhandledrejection', function(event) {
    console.error('Unhandled promise rejection:', event.reason);
    showAlert('请求处理失败，请稍后重试', 'error');
});

// 页面加载完成后的初始化
document.addEventListener('DOMContentLoaded', function() {
    // 应用用户偏好设置
    const theme = UserPreferences.getTheme();
    if (theme !== 'light') {
        UserPreferences.setTheme(theme);
    }

    // 初始化工具提示
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // 初始化弹出框
    const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });

    // 添加键盘快捷键
    document.addEventListener('keydown', function(event) {
        // Ctrl+R 或 F5: 刷新页面数据
        if ((event.ctrlKey && event.key === 'r') || event.key === 'F5') {
            event.preventDefault();
            location.reload();
        }

        // Esc: 关闭所有模态框
        if (event.key === 'Escape') {
            const modals = document.querySelectorAll('.modal.show');
            modals.forEach(modal => {
                const modalInstance = bootstrap.Modal.getInstance(modal);
                if (modalInstance) {
                    modalInstance.hide();
                }
            });
        }
    });
});

// 防止重复提交
function preventFormSubmission(formId, timeout = 3000) {
    const form = document.getElementById(formId);
    if (!form) return;

    let isSubmitting = false;

    form.addEventListener('submit', function(event) {
        if (isSubmitting) {
            event.preventDefault();
            return;
        }

        isSubmitting = true;
        const submitButton = form.querySelector('button[type="submit"]');
        const originalText = submitButton.textContent;

        submitButton.disabled = true;
        submitButton.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>处理中...';

        setTimeout(() => {
            isSubmitting = false;
            submitButton.disabled = false;
            submitButton.textContent = originalText;
        }, timeout);
    });
}

// 初始化全局实例
window.apiClient = ApiClient;
window.storageManager = StorageManager;
window.userPreferences = UserPreferences;
window.dataExporter = DataExporter;
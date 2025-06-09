package com.Lingbou.TestS;

import java.util.Arrays;

class myStack<T> {
    private Object[] stack;     // 定义
    private int size;           // 长度
    myStack() {                 // 构造函数
        stack = new Object[10];
    }
    public boolean isEmpty() {  // 判断是否为空
        return size == 0;
    }
    public T top() {            // 返回栈顶元素
        T t = null;
        if(size > 0) {
            t = (T) stack[size - 1];
        }
        return t;
    }
    public void push(T t) {     // 压栈
        kuoRong(size + 1);
        stack[size++] = t;
    }
    public T pop() {            // 出栈
        T t = top();
        if(size > 0) {
            stack[size - 1] = null;
            size--;
        }
        return t;
    }
    public void kuoRong(int size) {     // 扩大栈容量
        int len = stack.length;
        if(size > len) {
            size = size * 3 / 2 + 1;
            stack = Arrays.copyOf(stack, size);
        }
    }
}

public class Main5 {
    public static void main(String[] args) {

    }
}

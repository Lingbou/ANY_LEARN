package com.Lingbou.Test4;

public interface Inter {
    public abstract void solve();

    public default void show() {
        System.out.println("默认方法");
    }
}

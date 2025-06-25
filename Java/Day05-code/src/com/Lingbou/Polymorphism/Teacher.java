package com.Lingbou.Polymorphism;

public class Teacher extends Person {

    @Override
    public void show() {
        System.out.println("老师的信息:" + getName() + "," + getAge());
    }
}

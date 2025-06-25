package com.Lingbou.Test3;

public class Dog extends Animal{
    public Dog() {
    }

    public Dog(int age, String color) {
        super(age, color);
    }

    @Override
    public void eat(String something) {
        System.out.println(getAge() + "岁的 " + getColor() + "颜色的狗吃 " + something);
    }

    public void lookhome() {
        System.out.println("狗看家");
    }
}

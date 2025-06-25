package com.Lingbou.Test3;

import javax.sound.midi.Soundbank;

public class Cat extends Animal {
    public Cat() {
    }

    public Cat(int age, String color) {
        super(age, color);
    }

    @Override
    public void eat(String something) {
        System.out.println(getAge() + "岁的 " + getColor() + "颜色的猫吃 " + something);
    }

    public void catchMouse() {
        System.out.println("猫抓老鼠");
    }
}

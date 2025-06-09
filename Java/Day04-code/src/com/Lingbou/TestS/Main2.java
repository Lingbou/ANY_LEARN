package com.Lingbou.TestS;

abstract class Animal {
    abstract void cry();
    abstract void getAnimalName();
}

class Dog extends Animal {
    public void cry() {
        System.out.println("wangwangwang");
    }
    public void getAnimalName() {
        System.out.println("gou");
    }
}

class Cat extends Animal {
    public void cry() {
        System.out.println("miaomiaomiao");
    }
    public void getAnimalName() {
        System.out.println("mao");
    }
}

class Simulator {
    public void playSound(Animal animal) {
        animal.cry();
        animal.getAnimalName();
    }
}

public class Main2 {
    public static void main(String[] args) {
        Dog d = new Dog();
        Cat c = new Cat();
        Simulator s = new Simulator();
        s.playSound(d);
        s.playSound(c);
    }
}

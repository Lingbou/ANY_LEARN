package com.Lingbou.InterfaceL;

public  class Frog extends Animal implements Swim {

    public Frog() {
    }

    public Frog(String name, int age) {
        super(name, age);
    }

    @Override
    public void eat() {
        System.out.println("Frog eat");
    }

    @Override
    public void swim() {
        System.out.println("Frog swim");
    }
}

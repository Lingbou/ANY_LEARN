package com.Lingbou.Test3;

public class Person {
    private String name;
    private int age;

    public Person() {
    }

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public void keepPet(Dog dog, String something) {
        System.out.println(age + name + dog.getColor() + dog.getAge());
        dog.eat(something);
    }

    public void keepPet(Cat cat, String something) {
        System.out.println(age + name + cat.getColor() + cat.getAge());
        cat.eat(something);
    }
}

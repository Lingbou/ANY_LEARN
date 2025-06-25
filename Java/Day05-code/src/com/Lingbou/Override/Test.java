package com.Lingbou.Override;

public class Test {
    public static void main(String[] args) {
        OverseasStudent stu = new OverseasStudent();
        stu.lunch();
    }
}

class Person {
    public void eat() {
        System.out.println("吃饭");
    }

    public void drink() {
        System.out.println("喝水");
    }
}

class Student extends Person {
    public void lunch() {
        this.eat();
        this.drink();
        System.out.println("----------");
        super.eat();
        super.drink();
    }
}

class OverseasStudent extends Person {
    public void lunch() {
        this.eat();
        this.drink();
        System.out.println("----------");
        super.eat();
        super.drink();
    }

    @Override
    public void eat() {
        System.out.println("吃意大利面");
    }

    @Override
    public void drink() {
        System.out.println("喝开水");
    }
}
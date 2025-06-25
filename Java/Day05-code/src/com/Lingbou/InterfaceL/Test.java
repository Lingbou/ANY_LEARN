package com.Lingbou.InterfaceL;

public class Test {
    public static void main(String[] args) {
        Frog f = new  Frog("nima", 1);

        System.out.println(f.getName() +  " " + f.getAge());

        f.eat();
        f.swim();
    }
}

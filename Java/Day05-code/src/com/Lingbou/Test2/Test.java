package com.Lingbou.Test2;

public class Test {
    public static void main(String[] args) {
        Fu a = new Zi();
        System.out.println(a.name);
        a.show();
    }
}

class Fu {
    String name = "Fu";

    public void show() {
        System.out.println("Fu");
    }
}

class Zi extends Fu {
    String name;

    @Override
    public void show() {
        System.out.println("Zi");
    }
}
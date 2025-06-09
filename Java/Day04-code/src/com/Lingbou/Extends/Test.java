package com.Lingbou.Extends;

public class Test {
    public static void main(String[] args) {
        Ragdoll a = new Ragdoll();

        a.eat();
        a.drink();
        a.catchMouse();

        Husky b = new Husky();
        b.eat();
        b.drink();
        b.breakHome();
        b.lookHome();
    }
}

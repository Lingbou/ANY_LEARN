package com.Lingbou.SuperTest;

public class Zi extends Fu2 {
    String name = "Zi";
    public void ziShow() {
        String name = "ziShow";
        System.out.println(name);
        System.out.println(this.name);
        System.out.println(super.name);
    }
}

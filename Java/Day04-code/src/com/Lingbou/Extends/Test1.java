package com.Lingbou.Extends;

class Fu {
    String name = "nima";
}

class Zi extends Fu {
    String name = "nitama";

    public void sol() {
//        String name = "caonimade";
        System.out.println(name);
    }
}

public class Test1 {
    public static void main(String[] args) {
        Zi zi = new Zi();
        zi.sol();
    }
}



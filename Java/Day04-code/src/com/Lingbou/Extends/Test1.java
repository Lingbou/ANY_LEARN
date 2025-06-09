package com.Lingbou.Extends;

class Fu {
    String name = "nima";

    public void sol(){
        System.out.println("nitamade");
    }
}

class Zi extends Fu {
    String name = "nitama";

    @Override
    public void sol() {
        String name = "caonimade";
        System.out.println(name);
        System.out.println(this.name);
        System.out.println(super.name);

    }
}

public class Test1 {
    public static void main(String[] args) {
        Zi zi = new Zi();
        zi.sol();
    }
}



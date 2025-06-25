package com.Lingbou.Test2;

public class Test {
    public static void main(String[] args) {
        Fu a = new Zi();
        System.out.println(a.name);
        a.show();

//        if(a instanceof Zi) {
//           Zi z = (Zi)a;
//        }
        if(a instanceof Zi d) {
           d.BIBIBI();
        }else{
            System.out.println("没有这个子类");
        }

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

    public void BIBIBI() {
        System.out.println("子类的特有功能");
    }
}
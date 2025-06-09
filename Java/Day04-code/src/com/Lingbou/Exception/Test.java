package com.Lingbou.Exception;

public class Test {
    public static void main(String[] args) {
        int a = 10, b = 10;
        int tp = 10;
        try{
            tp = a / b;
        } catch(ArithmeticException e) {
            System.out.println(e);
        }

        System.out.println(tp);
    }
}

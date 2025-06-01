package com.Lingbou.test;

import java.util.Scanner;

public class Palindrome {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int index = n;
        int x = 0;
        while(n != 0) {
            x = x*10 + n%10;
            n/=10;
        }

        if(x == index) {
            System.out.println("true");
        } else {
            System.out.println("false");
        }
    }
}

package com.Lingbou.test;

import java.util.Scanner;

public class PrimePD {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int Flag = 1;
        for(int i=2; i*i <= n; i++) {
            if(n % i == 0) {
                Flag = 0;
                break;
            }
        }

        if(Flag == 0) {
            System.out.println("false");
        } else {
            System.out.println("true");
        }
    }
}

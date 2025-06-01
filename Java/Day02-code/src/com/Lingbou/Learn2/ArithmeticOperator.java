package com.Lingbou.Learn2;

import java.util.Scanner;

public class ArithmeticOperator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();

        for(int i = 1; i <= 3; i++) {
            System.out.println(num % 10);
            num = num / 10;
        }
    }
}

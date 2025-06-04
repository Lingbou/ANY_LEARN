package com.Lingbou.String;

import java.util.Scanner;
import java.util.StringJoiner;

public class StringJoinerLearn {
    public static void main(String[] args) {
        StringJoiner sj = new StringJoiner(", ","[","]");
        Scanner sc = new Scanner(System.in);
        int num  = sc.nextInt();
        for(int i = 0; i < num; i++){
            int x = sc.nextInt();
            sj.add(String.valueOf(x));
        }
        System.out.println(sj);
        System.out.println(sj.length());
    }
}
package com.Lingbou.test;

import java.util.Random;
import java.util.Scanner;

public class RandomGame {
    public static void main(String[] args) {
        Random r = new Random();
        Scanner sc = new Scanner(System.in);

        int n = r.nextInt(10 + 1);

        int x =  sc.nextInt();
        if(x != n){
            while(x != n) {
                if(x < n) {
                    System.out.println("small");
                }else if(x > n) {
                    System.out.println("big");
                }
                x =  sc.nextInt();
                if(x == n){
                    System.out.println("true,right!");
                    break;
                }
            }
        }else{
            System.out.println("true,righr");
        }
    }
}

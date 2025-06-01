package com.Lingbou.Array_L;

import java.util.Random;

public class ArrayLearn2 {
    public static void main(String[] args) {
        Random r = new Random();
        int[] arr = new int[10];
        double sum = 0;
        for(int i = 0; i < arr.length; i++){
            arr[i] = r.nextInt(100)+1;
            System.out.printf("%d ",arr[i]);
            sum += arr[i];
        }
        sum = sum / arr.length;
        System.out.printf("\n%f\n", sum);
        int num = 0;
        for(int i = 0; i < arr.length; i++){
            if(arr[i] < sum) {
                num++;
            }
        }
        System.out.println(num);
    }
}

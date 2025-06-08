package com.Lingbou.ToolsClass;

import java.util.Scanner;

public class TestClass {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[5];
        for (int i = 0; i < arr.length; i++) {
            int x = sc.nextInt();
            arr[i] = x;
        }
        ArrayUtil.printArr(arr);
        System.out.println(ArrayUtil.getAerage(arr));
    }
}

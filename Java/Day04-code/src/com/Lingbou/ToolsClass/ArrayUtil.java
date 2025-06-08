package com.Lingbou.ToolsClass;

import java.util.StringJoiner;

public class ArrayUtil {
    private ArrayUtil() {}


    public static void printArr(int[] Arr) {
        StringJoiner sj = new StringJoiner(", ", "[", "]");

        for (int j : Arr) {
            sj.add(String.valueOf(j));
        }
        System.out.println(sj.toString());
    }

    public static double getAerage(int[] Arr) {
        double sum = 0;
        for(int i = 0; i < Arr.length; i++) {
            sum += Arr[i];
        }
        return sum / Arr.length;
    }
}

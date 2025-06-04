package com.Lingbou.String;

public class String1 {
    public static void main(String[] args) {
        String s1 = new  String("abc");
        String s2 = "abc";
        String s3 = "abc";
        System.out.println(s1 == s2);
        System.out.println(s3 == s2);

        System.out.println(s1.equals(s2));
        System.out.println(s1.equals(s3));
        System.out.println(s3.equals(s2));
    }
}

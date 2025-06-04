package com.Lingbou.String;

public class StringBuilderLearn {
    public static void main(String[] args) {
        StringBuilder sb = new StringBuilder();

        sb.append("true");
        sb.append(false);
        sb.append(1.19);
        System.out.println(sb);
        sb.reverse();
        System.out.println(sb);
        System.out.println(sb.length());

        String str = sb.toString();
        System.out.println(str);

    }
}

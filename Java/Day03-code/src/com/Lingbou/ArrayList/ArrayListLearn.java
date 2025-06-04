package com.Lingbou.ArrayList;

import java.util.ArrayList;

public class ArrayListLearn {
    public static void main(String[] args) {
        // ArrayList<String> list = new ArrayList<String>();
        ArrayList<String> list = new ArrayList<>();

        list.add("aaa");
        list.add("bbb");
        list.add("ccc");
        list.add("ddd");
        list.add("aaa");


        System.out.println(list);

        list.remove("aaa");

        System.out.println(list);
        System.out.println(list);

    }
}

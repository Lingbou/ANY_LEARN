package com.Lingbou.Polymorphism;

public class Test {
    public static void main(String[] args) {
        Student s = new Student();
        s.setAge(10);
        s.setName("nima");

        Teacher t = new Teacher();
        t.setAge(45);
        t.setName("zhangsan");

        Administrator root = new  Administrator();
        root.setAge(8);
        root.setName("root");

        register(s);
        register(t);
        register(root);
    }

    public static void register(Person p) {
        p.show();
    }
}

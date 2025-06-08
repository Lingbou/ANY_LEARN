package com.Lingbou.StaticL;

public class Static01 {
    public static void main(String[] args) {
        Student s1 = new Student();
        Student.teacherName = "zhangsan";

        s1.setAge(12);
        s1.setName("张三");
        s1.setGender("男");
        s1.show();



        Student s2 = new Student();
        s2.setAge(15);
        s2.setName("李四");
        s2.setGender("女");
        s2.show();
    }

}

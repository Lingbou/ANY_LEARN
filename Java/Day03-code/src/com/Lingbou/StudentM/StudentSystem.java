package com.Lingbou.StudentM;

import java.util.Scanner;
import java.util.ArrayList;

public class StudentSystem {
    public static void main(String[] args) {
        ArrayList<Student> list = new ArrayList<>();
        while(true){
            System.out.println("-------------Fuck You!-------------");
            System.out.println("1:添加学生");
            System.out.println("2:删除学生");
            System.out.println("3:修改学生");
            System.out.println("4:查询学生");
            System.out.println("5:退出");
            System.out.println("请输入你的选择：");

            Scanner sc = new Scanner(System.in);

            String choose = sc.next();

            switch(choose) {
                case "1" -> addStudent(list);
                case "2" -> deleteStudent(list);
                case "3" -> updateStudent(list);
                case "4" -> queryStudent(list);
                case "5" -> {
                    System.out.println("退出");
                    System.exit(0);
                }
                default -> System.out.println("没有这个选项");
            }
        }
    }


    //添加学生
    public static void addStudent(ArrayList<Student> list){
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入学生的ID：");
        String id = sc.next();

        System.out.println("请输入学生的姓名：");
        String name = sc.next();

        System.out.println("请输入学生的年龄：");
        int age = sc.nextInt();

        System.out.println("请输入学生的家庭住址：");
        String address = sc.next();

        Student s = new Student(name, id, age, address);

        list.add(s);
    }

    //删除学生
    public static void deleteStudent(ArrayList<Student> list){
        System.out.println("删除学生");
    }

    //修改学生
    public static void updateStudent(ArrayList<Student> list){
        System.out.println("修改学生");
    }

    //查询学生
    public static void queryStudent(ArrayList<Student> list){
        if(list.isEmpty()) {
            System.out.println("当前无学生信息，请添加后查询");
            return ;
        }
        System.out.println("id\t姓名\t年龄\t家庭住址");
        for(int i = 0; i < list.size(); i++) {
            Student stu = list.get(i);
            System.out.println(stu.getId() + "\t" + stu.getName() + "\t" + stu.getAge() + "\t" + stu.getAddress());
        }

    }




}

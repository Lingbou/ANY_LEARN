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
        System.out.println("添加学生");
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
        System.out.println("查询学生");
    }




}

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
        String id = null;
        while(true){
            id = sc.next();
            if(contains(list, id)){
                System.out.println("ID存在，请重新录入：");
                continue;
            }else{
                break;
            }
        }

        System.out.println("请输入学生的姓名：");
        String name = sc.next();

        System.out.println("请输入学生的年龄：");
        int age = sc.nextInt();

        System.out.println("请输入学生的家庭住址：");
        String address = sc.next();

        Student s = new Student(name, id, age, address);

        list.add(s);
        System.out.println("学生信息添加成功");
    }

    //删除学生
    public static void deleteStudent(ArrayList<Student> list){
        Scanner sc = new Scanner(System.in);
        System.out.println("输入要删除学生的ID：");
        String id = sc.next();
        int index = getIndex(list, id);
        if(index >= 0) {
            list.remove(index);
            System.out.println("id为：" + id + "的学生成功删除");
        }else{
            System.out.println("id不存在，删除失败");
        }
    }

    //修改学生
    public static void updateStudent(ArrayList<Student> list){
        Scanner sc = new Scanner(System.in);
        System.out.println("输入要修改学生的ID：");
        String id = sc.next();
        int index = getIndex(list, id);

        if(index == -1) {
            System.out.println("要修改的学生ID：" + id + "不存在，请重新输入");
            return ;
        }

        Student stu = list.get(index);

        System.out.println("请输入要修改学生的姓名：");
        String newName = sc.next();
        stu.setName(newName);

        System.out.println("请输入要修改学生的年龄：");
        int newAge = sc.nextInt();
        stu.setAge(newAge);

        System.out.println("请输入要修改学生的家庭住址：");
        String newAddress = sc.next();
        stu.setAddress(newAddress);

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
    
    public static boolean contains(ArrayList<Student> list, String id) {
        if(getIndex(list, id) >= 0) {
            return true;
        }else{
            return false;
        }
    }

    //通过id获取索引
    public static int getIndex(ArrayList<Student> list, String id) {
        for(int i = 0; i < list.size(); i++) {
            if(list.get(i).getId().equals(id)) {
                return i;
            }
        }
        return -1;
    }
}

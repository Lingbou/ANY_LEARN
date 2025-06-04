package com.Lingbou.String;

import java.util.Scanner;

public class String2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String username = "Lingbou";
        String password = "FuckWorld";

        System.out.println("输入账号：");
        String usernameInput = sc.nextLine();
        if(!username.equals(usernameInput)){
            System.out.println("账号错误");
        }else{
            System.out.println("输入密码：");
            String passwordInput = sc.nextLine();
            if(!password.equals(passwordInput)){
                System.out.println("密码错误");
            }else{
                System.out.println("登陆成功！");
            }
        }

    }
}

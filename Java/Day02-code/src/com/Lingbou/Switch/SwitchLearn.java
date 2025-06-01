package com.Lingbou.Switch;

import java.util.Scanner;

public class SwitchLearn {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int num = input.nextInt();
//        switch (num) {
//            case 1:
//                System.out.println("Fuck You");
//                break;
//            case 2:
//                System.out.println("Fuck you");
//                break;
//            default:
//                System.out.println("nima");
//                break;
//        }

        switch (num) {
            case 1 -> {
                System.out.println("cnm");
            }
            case 2 -> {
                System.out.println("mcn");
            }
            case 3 -> {
                System.out.println("cmn");
            }
            default -> {
                System.out.println("karan");
            }
        }
    }
}

package com.Lingbou.TestS;

class myException extends Exception {
    private String s;

    public myException(String s) {
        this.s = s;
    }

    public void pri() {
        System.out.println(this.s);
    }

}

public class Main4 {
    public static void main(String[] args) {
        try {
            throw new myException("nima");
        } catch(myException e) {
            e.pri();
        }
    }
}

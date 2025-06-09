package com.Lingbou.TestS;

class DangerException extends Exception {
    private static final String msg = "超载";

    public String warnMess() {
        return msg;
    }
}

class CargoBaot {
    private int realContent;
    private int maxContent;

    public void setMaxContent(int c) {
        this.maxContent = c;
    }

    public void loading(int m) throws DangerException {
        if(this.realContent + m > this.maxContent) {
            throw new DangerException();
        } else {
            this.realContent += m;
        }
    }
}

public class Main3 {
    public static void main(String[] args) {
        CargoBaot c = new CargoBaot();
        c.setMaxContent(10);

        try {
            c.loading(9);
            System.out.println("装载成功");
        } catch(DangerException e) {
            System.out.println(e.warnMess());
        } finally {
            System.out.println("启航");
        }
    }
}

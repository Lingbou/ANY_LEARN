package com.Lingbou.Game1;

import java.util.Random;

public class GameOne {
    private String gamerName;
    private int bloodNum;

    public GameOne() {};
    public GameOne(String gamerName, int bloodNum) {
        this.gamerName = gamerName;
        this.bloodNum = bloodNum;
    }

    public void setGamerName(String gamerName) {
        this.gamerName = gamerName;
    }
    public void setBloodNum(int bloodNum) {
        this.bloodNum = bloodNum;
    }
    public String getGamerName() {
        return gamerName;
    }
    public int getBloodNum() {
        return bloodNum;
    }

    public int Atack() {
        Random r = new Random();
        return r.nextInt(20) + 1;
    }
}

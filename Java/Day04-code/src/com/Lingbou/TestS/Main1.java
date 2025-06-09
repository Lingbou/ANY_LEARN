package com.Lingbou.TestS;

class Point {
    protected int x;
    protected int y;

    Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
    public int getY() {
        return this.y;
    }
    public void setPoint(int x, int y) {
        this.x = x;
        this.y = y;
    }
    public int getX() {
        return this.x;
    }

}

class Circle extends Point {
    protected int radius;
    Circle(int x, int y, int radius) {
        super(x, y);
        this.radius = radius;
    }

    public void setRadius(int radius) {
        this.radius = radius;
    }

    public int getRadius() {
        return this.radius;
    }

    public double area() {
        return 3.14*this.radius*this.radius;
    }
}

public class Main1 {
    public static void main(String[] args) {
        Circle c = new Circle(10, 10, 10);
        System.out.println(c.area());
    }
}

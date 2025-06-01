import java.util.Scanner;

/**
 * KeyInput Scanner
 * 
 * @Lingbou
 * @version 1.0
 */
public class KeyInput {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); 
        int inputNum1 = sc.nextInt();
        int inputNum2 = sc.nextInt();
        System.out.println(inputNum1 + inputNum2);
        sc.close();
    }
}

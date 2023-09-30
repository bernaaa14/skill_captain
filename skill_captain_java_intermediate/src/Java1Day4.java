import java.util.Scanner;

public class Java1Day4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int first = sc.nextInt();
        int second = sc.nextInt();

        if (first > second) {
            System.out.println("The larger number is " + first);
        } else {
            System.out.println("The larger number is " + second);
        }
    }
}

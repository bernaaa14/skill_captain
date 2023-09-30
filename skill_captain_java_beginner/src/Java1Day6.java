import java.util.Scanner;

public class Java1Day6 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int input;
        //for loop to print numbers 1-10
        for (int i = 1; i <= 10; i++) {
            System.out.println(i);
        }
        System.out.println();
        //while loop to print out the even numbers between 1 and 20.
        int num = 1;
        while (num <= 20) {
            if (num % 2 == 0) {
                System.out.println(num);
            }
            num++;
        }
        System.out.println();
        //do-while loop to prompt the user to enter a number between 1 and 10, and keeps prompting until a valid number is entered.
        do {
            System.out.println("Enter a number between 1-10");
            input = sc.nextInt();
        }
        while (input <= 10);
    }
}

import java.util.Scanner;

public class Java1Day5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the first number");
        int firstNum = sc.nextInt();
        System.out.println("Enter the second number");
        int secondNum = sc.nextInt();
        System.out.println("Enter operation (+, - , *, /");
        char operation = sc.next().charAt(0);
        int answer = 0;
        //switch case for the chosen operator
        switch (operation) {
            case '+':
                answer = firstNum + secondNum;
                break;
            case '-':
                answer = firstNum - secondNum;
                break;
            case '*':
                answer = firstNum * secondNum;
                break;
            case '/':
                answer = firstNum / secondNum;
                break;

            default:
                System.out.println("Operator invalid! ");
        }
        System.out.println(answer);
    }
}

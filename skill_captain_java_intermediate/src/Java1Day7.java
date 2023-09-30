import java.util.Scanner;
public class Java1Day7 {
    public static void main(String[] args) {
        //assuming that user input is an integer
        Scanner sc = new Scanner(System.in);
        int[] num = new int[5];
        int input;
        int sum = 0;
        double average;
        int maximum;
        int minimum;
        //loop for adding the user input in the arrays
        for (int i = 0; i < num.length; i++) {
            input = sc.nextInt();
            num[i] = input;
            sum += num[i];
        }
        minimum = num[0];
        maximum = num[0];
        //loop to find the max, min, ave
        for (int j = 0; num.length > j; j++) {
            if (num[j] < minimum) {
                minimum = num[j];
            } else if (num[j] > maximum) {
                maximum = num[j];
            }
        }
        average = sum / 5;
        System.out.println("Sum: " + sum + "\n" +
                "Average: " + average + "\n" +
                "Minimum: " + minimum + "\n" +
                "Maximum: " + maximum);
    }
}

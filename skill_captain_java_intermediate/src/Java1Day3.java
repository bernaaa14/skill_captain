import java.util.Scanner;
public class Java1Day3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int age = sc.nextInt();
        sc.nextLine();
        String name = sc.nextLine();

        System.out.println("Hello "+ name + "you are "+ age + "years old");

    }
}

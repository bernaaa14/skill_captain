package Java2Day8;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class UserRegistration {
    public static void main(String[] args) {
        UserRepository users = new UserRepository(); // Create an instance of UserRepository
        Scanner sc = new Scanner(System.in);
        System.out.print("Please enter your name: ");
        String name = sc.nextLine();
        System.out.print("Please enter your email address: ");
        String email = sc.nextLine();
        System.out.print("Please enter your password: ");
        String password = sc.nextLine();
        System.out.print("Please enter your shipping address: ");
        String address = sc.nextLine();

        // Validate user input
        if (name.isEmpty() || email.isEmpty() || password.isEmpty() || address.isEmpty()) {
            System.out.println("Missing information, Please try again.");
        } else if (!isValidEmail(email)) {
            System.out.println("Invalid email address format. Please try again.");
        } else if (users.contains(email)) {
            System.out.println("Email address is already taken.");
        } else {
            // Create a User object and register it in the UserRepository
            User user = new User(name, email, password, address);
            users.addUser(user);
            System.out.println("User registration successful!");
        }
    }


    public static boolean isValidEmail(String email){
        String emailRegex = "^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+$";
        Pattern pattern = Pattern.compile(emailRegex);
        Matcher matcher = pattern.matcher(email);
        return matcher.matches();
    }
}
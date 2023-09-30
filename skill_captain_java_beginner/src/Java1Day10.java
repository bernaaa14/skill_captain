import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;
public class Java1Day10 {
    public static void main(String[] args) {
        //ask user for input
        Scanner sc = new Scanner(System.in);
        //set to store unique numbers
        Set<Integer> uniqueNumbers = new HashSet<>();
        System.out.println("Enter numbers to be stored, leave a blank line and press enter to stop ");
         int input;

         //loop to keep asking user if they hadn't enter a blank line
        while(sc.hasNextInt()){
            input=sc.nextInt();
            // if-statement for checking if duplicate
            if(uniqueNumbers.contains(input)){
                System.out.println(input + ": is a duplicate number");
            }else{
                uniqueNumbers.add(input);
                System.out.println(input + ": is a unique number");
            }
            }
        }
    }






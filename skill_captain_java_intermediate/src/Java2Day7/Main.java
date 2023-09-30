package Java2Day7;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        //ask the user fo input
        Scanner sc = new Scanner(System.in);
        //store the input in the variable text
        System.out.println("Please input the sentence you want to write in the file ");
        String text = sc.nextLine();
        String fileName = "output.txt";
        //FileWriter object writer is created
        try (FileWriter writer = new FileWriter(fileName)) {
            //writes the "text" to a file named fileName
            writer.write(text);
            System.out.println("Input successful!!!");
            //handles error when writing into the file
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
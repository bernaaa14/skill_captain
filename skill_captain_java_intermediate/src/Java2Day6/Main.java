package Java2Day6;

import java.util.Scanner;
import java.nio.file.Paths;

public class Main {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(Paths.get("src/Java2Day6/input.txt"))) {
            //  read the file until all lines have been read
            int count=0;
            while (scanner.hasNextLine()) {
                //  read one line
                String row = scanner.nextLine();
                // print the line that we read
                if(row.toLowerCase().contains("java")){
                        count++;
                }
                System.out.println(row);
            }
            System.out.println("Occurences of Java " + count);
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
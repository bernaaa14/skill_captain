import java.util.HashMap;
import java.util.Scanner;

public class Java1Day9 {
    public static void main(String[] args) {
        //allow the user to input text
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();

        //Create a HashMap to store word-frequency pairs(key is a word)
        //the frequency is then stored in an integer
        HashMap<String, Integer> wordFrequency = new HashMap<>();
        String words[] = input.split(" ");

        //for each loop
        for (String word : words) {
            word = word.toLowerCase();//convert to lowercase(case insensitive)

            //if the wordFrequency map contains the current word, increment frequency by 1
            if (wordFrequency.containsKey(word)) {
                wordFrequency.put(word, wordFrequency.get(word) + 1);
            }
            //if statement to inform the user if they didn't enter anything
            if (input.isEmpty()) {
                System.out.println("The user didn't enter anything");
            }
            //else, if it doesn't, return 1 as its frequency
            else {
                wordFrequency.put(word, 1);
            }
        }
        System.out.println(wordFrequency);
    }

}



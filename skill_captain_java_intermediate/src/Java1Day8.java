import java.util.ArrayList;
import java.util.Scanner;
public class Java1Day8 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<String> groceries = new ArrayList<>();

        // Adding the items to the list
        System.out.println("Hello, Shopper! Please enter the ingredients you'd like to include in your list." +
                "\n" + "To stop adding ingredients, leave a blank line and press Enter.");
        String input;
        while (true) {
            input = sc.nextLine();
            if (input.isEmpty()) {
                break;
            }
            groceries.add(input);
        }

        // Removing items from the list
        System.out.println("Great! Do you want to remove items from the list?" +
                "\n" + "To stop removing ingredients, leave a blank line and press Enter.");
        String removeItem = "";
        while (true) {
            removeItem = sc.nextLine();
            if (removeItem.isEmpty()) {
                break;
            }
            if (groceries.contains(removeItem)) {
                groceries.remove(removeItem);
                System.out.println(removeItem + " successfully removed...");
            } else {
                System.out.println("No item in the grocery list!");
            }
        }

        // Checking an item on the list
        System.out.println("Item you want to check from the grocery list:");
        String searchItem = sc.nextLine();
        if (groceries.contains(searchItem)) {
            System.out.println("It's on the list");
        } else {
            System.out.println("No item in the grocery list!");
        }

        // Printing the current grocery list
        System.out.println("The current grocery list contains: " + groceries);

        // Clearing the entire grocery list
        System.out.println("TASK COMPLETED: Deleting the entire grocery list...");
        groceries.clear();
    }
}










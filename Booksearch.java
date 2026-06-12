import java.util.ArrayList;
import java.util.Scanner;

public class BookSearch {

    public static void main(String[] args) {

        ArrayList<String> books = new ArrayList<>();

        books.add("The Alchemist");
        books.add("Harry Potter");
        books.add("Think and Grow Rich");
        books.add("The Power of Habit");
        books.add("Atomic Habits");

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter word to search: ");
        String word = sc.nextLine().toLowerCase();

        boolean found = false;

        System.out.println("\nMatching books:");

        for (int i = 0; i < books.size(); i++) {
            String book = books.get(i);

            if (book.toLowerCase().contains(word)) {
                System.out.println(book);
                found = true;
            }
        }

        if (!found) {
            System.out.println("No matching books found.");
        }

        sc.close();
    }
}
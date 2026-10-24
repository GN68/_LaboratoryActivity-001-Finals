import java.util.Scanner;

public class Mein {
    static String VALID_SEQUENCE = "<data_type> <identifier> <assignment_operator> <value> <delimiter>";
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter Tokens: ");
        String input = scanner.nextLine().trim();

        if (input.equals(VALID_SEQUENCE)) {
            System.out.println("Syntax is Correct!");
        } else {
            System.out.println("Syntax is Error!");
        }
    }
}
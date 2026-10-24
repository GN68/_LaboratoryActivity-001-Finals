import java.util.Objects;
import java.util.Scanner;
import java.util.stream.IntStream;

public class Main {
    static void error(String msg) {
        System.out.println("[ERROR]: " + msg);
    }

    static final String[] EXAMPLES = {

            // CORRECT SET
            "int x = 5;",
            "long num = 10L;",
            "float fl = 1.2f;",
            "double db = 3.14;",
            "char ch = '7';",
            "String text = \"hello\";",
            "boolean flag = true;",

            // INVALID SET
            "int x = 5",// 1. "the code is missing a semicolon"
            "String text = \"hello;",// 2. "the code has uneven Quotation marks..."
            "x = 5;",// 3. "Missing data type declaration"
            "int x;",// 4. "the code is Incomplete, you've forgotten to add something."
            "int x + 5;",// 5. "Unexpected token..."
            "int x = abc;",// 6. "Invalid int"
            "long x = abc;",// 7. "Invalid long"
            "float x = abc;",// 8. "Invalid float"
            "double x = abc;", // 9. "Invalid double"
            "String text = hello;",// 10. "Invalid String"
    };
    static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("Declare a variable: ");
            String input = scanner.nextLine();

            if (!input.isEmpty()) {
                check(input);
                System.out.println();
            }else{ // dump tests
                for (int i = 0; i < EXAMPLES.length; i++) {
                    check(EXAMPLES[i]);
                    System.out.println();
                }
            }
        }
    }

    static void check(String input) {
        System.out.println(input);

        // [ERROR]: Missing semicolon
        if (input.charAt(input.length()-1) != ';') {
            error("the code is missing a semicolon");
            return;
        }else{
            input = input.substring(0,input.length()-1);
        }


        //--------- GATHER DATA ---------//
        //quick string integrity check
        IntStream input_char = input.chars();
        long quotation_count = input_char.filter(ch -> (ch == '"' || ch == '\'')).count();

        // [ERROR]: Uneven Quotation marks
        if (Math.floorMod(quotation_count,2) != 0) {
            error("the code has uneven Quotation marks, please make sure to close your strings");
            return;
        }

        // serialize string so its easier to parse
        input = input.replace("="," = ");

        // split into separate words
        String[] words = input.split("\\s+");


        // [ERROR]: Missing data type declaration
        if (words.length == 3 && words[1] == " = ") {
            error("Missing data type declaration");
            return;
        }
        // [ERROR]: Incomplete variable declaration
        if (words.length != 4) {
            error("the code is Incomplete, you've forgotten to add something.");
            return;
        }

        String data_type  = words[0];
        //String name       = words[1];
        String assignment = words[2];
        String value      = words[3];

        // [ERROR]: Unexpected assignment operator
        if (!Objects.equals(assignment, "=")) {
            error("Unexpected token \"" + assignment + "\", it should be \"=\"");
            return;
        }

        if (Objects.equals(data_type, "int")) {
            if (!value.matches("[+-]?\\d+")) {
                error("Invalid int");
                return;
            }
        }
        else if (Objects.equals(data_type, "long")) { // handwritten pattern
            if (!value.matches("[+-]?\\d+[lL]?")) {
                error("Invalid long");
                return;
            }
        }
        else if (Objects.equals(data_type, "float")) {// I stole this abomination here https://stackoverflow.com/questions/6754552/regex-to-find-a-float
            if (!value.matches("[+-]?(\\d+|\\d+\\.\\d+|\\.\\d+|\\d+\\.)([eE][+-]?\\d+)?[fF]?")) {
                error("Invalid float");
                return;
            }

        }
        else if (Objects.equals(data_type, "double")) { // the same pattern as float's, but replacaed with dD instead of fF yeahh
            if (!value.matches("[+-]?(\\d+|\\d+\\.\\d+|\\.\\d+|\\d+\\.)([eE][+-]?\\d+)?[dD]?")) {
                error("Invalid double");
                return;
            }
        }
        else if (Objects.equals(data_type, "char")) {// handwritten pattern
            if (!value.matches("'.'")) {
                error("Invalid char");
                return;
            }
        }
        else if (Objects.equals(data_type, "String")) {
            if (!(value.endsWith("\"") && value.startsWith("\""))) {
                error("Invalid String");
                return;
            }
        }
        else if (Objects.equals(data_type, "boolean")) {
            if (!(value.equals("true") || value.equals("false"))) {
                error("Invalid boolean");
                return;
            }
        }
        else {
            error("Unsupported type given: \"" + data_type + "\", only supported types are [int,long,float,double,char,String]");
        }

        System.out.println("Syntax is Correct!");
    }
}

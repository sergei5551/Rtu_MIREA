import java.util.Scanner;

public class GenericStack2Test {
    public static void main(String[] args) {
        GenericStack<String> stack = new GenericStack<>();
        Scanner scanner = new Scanner(System.in);

        System.out.println("введите пять строк:");
        for (int i = 0; i < 5; i++) {
            String input = scanner.nextLine();
            stack.push(input);
        }

        System.out.println("строки в обратном порядке:");
        while (!stack.isEmpty()) {
            System.out.println(stack.pop());
        }

        scanner.close();
    }
}

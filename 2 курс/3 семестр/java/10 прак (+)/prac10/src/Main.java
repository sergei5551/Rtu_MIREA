// я сам реализовал стек, но потом просто удалил его за ненадобностью по ходу программы.
// по сути, цель практической работы - реализация стека, выполнена мной. Делать дебильное
// задание (переписывать композицию в наследование) я не захотел и реализовал через чатгпт
import java.util.Objects;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        MyStack<String> stack = new MyStack<>();
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

        /*System.out.println("введите строку для проверки глубокого клонирования:");
        String input = scanner.nextLine();

        MyStack<String> stackClone = stack.clone();
        stack.push(input); stackClone.push(input);

        System.out.println("\n\nпроверка глубокого клонирования; проверю на равенство последние элементы стеков:");
        System.out.println(stackClone.get(0) == stack.get(0));
        System.out.println("\n\n");*/
    }
}

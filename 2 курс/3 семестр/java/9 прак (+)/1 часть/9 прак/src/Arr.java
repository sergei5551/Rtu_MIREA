import java.util.ArrayList;
import java.util.List;


public class Arr{
    public static void main(String[] args) {
        List<Integer> inputList = new ArrayList<>(List.of(1, 2, 3, 4, 2, 3, 5));
        List<Integer> outputList = Duplicates.removeDuplicates(inputList); // 1

        System.out.println(outputList); // Output: [1, 2, 3, 4, 5]

        System.out.println("Индекс [" + Duplicates.findIndex(outputList, 100) + "]"); // 2
        List<Circle> circl = new ArrayList<>(List.of(
                new Circle(3),
                new Circle(5),
                new Circle(3)
        ));

        System.out.println("max r = " + Circle.findMax(circl).getRadius()); // 3

        // 4
        List<List<Circle>> circleLists = new ArrayList<>();
        // Создаем первую строку двумерного массива
        List<Circle> row1 = new ArrayList<>();
        row1.add(new Circle(1)); // Добавляем круг с радиусом 1
        row1.add(new Circle(2)); // Добавляем круг с радиусом 2
        circleLists.add(row1); // Добавляем первую строку в двумерный массив

        // Создаем вторую строку двумерного массива
        List<Circle> row2 = new ArrayList<>();
        row2.add(new Circle(3)); // Добавляем круг с радиусом 3
        row2.add(new Circle(4)); // Добавляем круг с радиусом 4
        circleLists.add(row2); // Добавляем вторую строку в двумерный массив
        System.out.println("max r = " + Circle.findMax2(circleLists).getRadius()); // 4
    }
}

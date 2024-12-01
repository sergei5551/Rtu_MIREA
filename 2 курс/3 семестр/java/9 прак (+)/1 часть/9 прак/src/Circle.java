import java.util.List;
// Класс Circle, реализующий интерфейс Comparable
class Circle implements Comparable<Circle> {
    private double radius;

    public Circle(double radius) {
        this.radius = radius;
    }

    public double getRadius() {
        return radius;
    }

    public static Circle findMax2(List<List<Circle>> list){
        if (list.isEmpty()) {
            throw new IllegalArgumentException("Список пуст!");
        }

        Circle max = list.get(0).get(0);
        for (int i = 0; i < list.size(); i++) {
            for (int j = 1; j  < (list.get(i).size()); j++ ){
                if (max.compareTo(list.get(i).get(j)) < 0) {
                    max = list.get(i).get(j);
                }
            }
        }
        return max;
    }

    public static Circle findMax(List<Circle> list) {
        if (list.isEmpty()) {
            throw new IllegalArgumentException("Список пуст!");
        }

        Circle max = list.get(0);
        for (int i = 1; i < list.size(); i++) {
            if (max.compareTo(list.get(i)) < 0) {
                max = list.get(i);
            }
        }
        return max;
    }




    @Override
    public int compareTo(Circle o) {
        return Double.compare(this.radius, o.radius);
    }

}
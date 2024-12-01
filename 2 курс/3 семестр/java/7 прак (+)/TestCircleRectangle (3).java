public class TestCircleRectangle {
    public static void main(String[] args) throws InterruptedException {

        // Создаю треугольник

        try {
            Triangle t = new Triangle(1, 2, 10);
        } catch (IllegalTriangleException e) {
            System.out.println("Error: " + e.getMassage() + '\n');
        }

        // 1 круг
        Circle circle1 = new Circle(1);
        circle1.setColor("Red");
        circle1.setFilled(true);

        System.out.println("Круг " + circle1.toString());
        System.out.println("Радиус равен " + circle1.getRadius());
        System.out.println("Площадь равна " + circle1.getArea());
        System.out.println("Диаметр равен " + circle1.getDiameter());

        // 2 круг
        Circle circle2 = new Circle(2);
        System.out.println("\nКруг2 " + circle2.toString());
        System.out.println("Радиус равен " + circle2.getRadius());
        System.out.println("Площадь равна " + circle2.getArea());
        System.out.println("Диаметр равен " + circle2.getDiameter());

        // Какая фигура больше?
        System.out.println("\nМаксимальный " + GeometricObject.max(circle1, circle2).toString());


        // Прямоугольник 1
        Rectangle rectangle1 = new Rectangle(2, 4);
        System.out.println("\nПрямоугольник " + rectangle1.toString());
        System.out.println("Площадь равна " + rectangle1.getArea());
        System.out.println("Периметр равен " + rectangle1.getPerimeter());
        // Прямоугольник 2

        Rectangle rectangle2 = new Rectangle(3, 5);
        rectangle2.setColor("Red");
        rectangle2.setFilled(true);

        System.out.println("\nПрямоугольник2 " + rectangle2.toString());
        System.out.println("Площадь равна " + rectangle2.getArea());
        System.out.println("Периметр равен " + rectangle2.getPerimeter());
        // Какая фигура больше?
        System.out.println("\nМаксимальный " + GeometricObject.max(rectangle1, rectangle2).toString());

        System.out.println("/////////////////////////////////////////");
        GeometricObject[] objects = new GeometricObject[5];
        objects[0] = new Circle(3);
        objects[1] = new Square(5);
        objects[2] = new Rectangle(4, 6);
        try {
            objects[3] = new Triangle(3, 4, 5);
        } catch (IllegalTriangleException e) {
            System.out.println("Error: " + e.getMassage() + '\n');
        }
        objects[4] = new Square(7);

        for (GeometricObject obj : objects) {
            System.out.println(obj);
            System.out.println("Периметр: " + obj.getPerimeter());

            ((Colorable) obj).howToColor();
        }

    }
}
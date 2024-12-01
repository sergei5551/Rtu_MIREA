public class Triangle extends GeometricObject{
    public Triangle(){ // Constructor default
        this.side1 = this.side2 = this.side3 = 1.0;
    }

    public Triangle(double side1, double side2, double side3) throws IllegalTriangleException{ // Constructor with three arguments
        if(!isValidSides(side1, side2, side3)){
            throw new IllegalTriangleException("Две стороны меньше третьей");
        }

        this.side1 = side1;
        this.side2 = side2;
        this.side3 = side3;

    }
    private boolean isValidSides(double... sides) {
        return ((sides[0] + sides[1] > sides[2]) && (sides[1] + sides[2] > sides[0]) && (sides[0] + sides[2] > sides[1]));
    }

    public double side1, side2, side3;
    private final double p = side1 + side2 + side3;
    private final double polP = p/2;
    private final double area = Math.pow(polP*(polP - side1)*(polP - side2)*(polP - side3), 0.5);

    public double getArea(){
        return area;
    }
    @Override
    public double getPerimeter(){
        return p;
    }

    @Override
    public String toString() {
        return  name() + ": сторона1 = " + side3 +
                ", сторона2 = " + side2 +
                ", сторона3 = " + side1;
    }

    @Override
    protected String name() {
        return "Triangle";
    }
}

public class Square extends GeometricObject implements Colorable{
    private double side;
    public Square(){
        this.side = 0;
    }

    public Square(double side){
        this.side = side;
    }
    public double getPerimeter(){
        return side*4;
    }
    @Override
    public void howToColor() {
        System.out.println("Раскрасьте все 4 стороны\n");
    }

    public double getSide() {
        return side;
    }

    public void setSide(double side) {
        this.side = side;
    }

    @Override
    protected String name() {
        return "Square";
    }
}

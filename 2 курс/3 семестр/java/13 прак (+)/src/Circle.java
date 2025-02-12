public class Circle extends Draw_Figures{
    public Circle(Draw_API dr) {
        super(dr);
    }

    public void createFigures(String col){
        System.out.println("Круг ");
        dr.draw(col);
    };
    public void createFigures(){
        createFigures("Зеленый");
    };
}

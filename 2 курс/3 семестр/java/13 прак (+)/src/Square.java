public class Square extends Draw_Figures{
    public Square(Draw_API dr) {
        super(dr);
    }

    public void createFigures(String col){
        System.out.println("Квадрат ");
        dr.draw(col);
    };

    public void createFigures(){
        createFigures("Зеленый");
    };
}

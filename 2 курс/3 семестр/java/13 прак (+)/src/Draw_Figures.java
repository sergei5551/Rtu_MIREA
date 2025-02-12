abstract public class Draw_Figures {
    protected Draw_API dr;
    protected Draw_Figures(Draw_API dr){
        this.dr = dr;
    }
    public abstract void createFigures(String col);

}

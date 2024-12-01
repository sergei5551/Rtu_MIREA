abstract class GeometricObject implements Colorable {
    private String color = "белый";
    private boolean filled;
    private final java.util.Date dateCreated;
    public abstract double getPerimeter(); // Для того чтоб узнать какой объект больше
    /** Создает по умолчанию заданный геометрический объект */
    public GeometricObject() {
        dateCreated = new java.util.Date();
    }

    /** Создает геометрический объект с указанным цветом и заливкой */
    public GeometricObject(String color, boolean filled) {
        dateCreated = new java.util.Date();
        this.color = color;
        this.filled = filled;
    }

    /** Возвращает цвет */
    public String getColor() {
        return color;
    }

    /** Присваивает новый цвет */
    public void setColor(String color) {
        this.color = color;
    }

    /** Возвращает заливку. Поскольку filled типа boolean,
     *  getter-метод называется isFilled */
    public boolean isFilled() {
        return filled;
    }

    /** Присваивает новую заливку */
    public void setFilled(boolean filled) {
        this.filled = filled;
    }

    /** Получает dateCreated */
    public java.util.Date getDateCreated() {
        return dateCreated;
    }

    /** Возвращает строковое представление этого объекта */
    public String toString() {
        return name() + " создан " + dateCreated + ",\nцвет: " + color +
                ", заливка: " + filled ;
    }
    //////////////////////////////////////////////
    public static GeometricObject max(GeometricObject o1, GeometricObject o2) {
        if(o1.getPerimeter() > o2.getPerimeter()){
            return o1;
        }
        else{
            return o2;
        }
    }
    //////////////////////////////////////////////
    @Override
    public void howToColor() {
        System.out.println("Раскрасьте стороны\n");
    }
    protected abstract String name();
}


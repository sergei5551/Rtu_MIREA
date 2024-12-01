public class ComparableCircle extends Circle implements Comparable{
    @Override
    public GeometricObject compareTo(GeometricObject obj){ // Сравнения типа ComparableCircle с любым другим
        return GeometricObject.max(this, obj);
    }
}

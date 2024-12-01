import java.util.ArrayList;

public class GenericStack2<E> {
    private ArrayList<E> list = new ArrayList<>();

    public GenericStack2() {
    }

    public int getSize() {
        return list.size();
    }

    public E peek() {
        if (isEmpty()) {
            throw new RuntimeException("Stack is empty");
        }
        return list.get(getSize() - 1);
    }

    public E pop() {
        if (isEmpty()) {
            throw new RuntimeException("Stack is empty");
        }
        return list.remove(getSize() - 1);
    }

    public void push(E o) {
        list.add(o);
    }

    public boolean isEmpty() {
        return list.isEmpty();
    }

    @Override
    public String toString() {
        return "стек: " + list.toString();
    }
}

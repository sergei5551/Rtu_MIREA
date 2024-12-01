import java.util.ArrayList;

import java.util.ArrayList;

public class MyStack<E> extends ArrayList<E> implements Cloneable{
    public boolean isEmpty() {
        return super.isEmpty();
    }

    public int getSize() {
        return size();
    }

    public E peek() {
        if (isEmpty()) {
            return null;
        } else {
            return get(size() - 1);
        }
    }

    public E pop() {
        if (isEmpty()) {
            return null;
        } else {
            return remove(size() - 1);
        }
    }

    public E push(E o) {
        add(o);
        return o;
    }

    // переопределяю клонирование. Суть глубокого клонирования, которое тут реализовано, в том, чтобы создать клон не только объекта
    // но и всех элементов внутри этого объекта, что я тут и сделал.
    @Override
    public MyStack<E> clone() {
        MyStack<E> clonedStack = (MyStack<E>) super.clone();
        for (int i = 0; i < clonedStack.size(); i++) {
            E element = clonedStack.get(i);
            if (element instanceof Cloneable) {
                try {
                    clonedStack.set(i, (E) element.getClass().getMethod("clone").invoke(element));
                } catch (Exception e) {
                    System.out.println(e.getMessage());
                }
            }
        }
        return clonedStack;
    }
}

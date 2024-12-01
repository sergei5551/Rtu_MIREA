public class GenericStack<E> {
    private E[] elements;
    private int size = 0;
    private static final int INITIAL_CAPACITY = 10;

    @SuppressWarnings("unchecked")
    public GenericStack() {
        elements = (E[]) new Object[INITIAL_CAPACITY];
    }

    public int getSize() {
        return size;
    }

    public E peek() {
        if (isEmpty()) {
            throw new RuntimeException("Стек пустой");
        }
        return elements[size - 1];
    }

    public void push(E o) {
        if (size == elements.length) {
            resize();
        }
        elements[size++] = o;
    }

    public E pop() {
        if (isEmpty()) {
            throw new RuntimeException("Стек пустой");
        }
        E o = elements[--size];
        elements[size] = null; // удаление ссылки для невозможности утечки памяти
        return o;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    // удвоение размера массива
    @SuppressWarnings("unchecked")
    private void resize() {
        E[] newArray = (E[]) new Object[elements.length * 2];
        System.arraycopy(elements, 0, newArray, 0, elements.length);
        elements = newArray;
    }

    @Override
    public String toString() {
        StringBuilder result = new StringBuilder("стек: [");
        for (int i = 0; i < size; i++) {
            result.append(elements[i]);
            if (i < size - 1) {
                result.append(", ");
            }
        }
        result.append("]");
        return result.toString();
    }
}

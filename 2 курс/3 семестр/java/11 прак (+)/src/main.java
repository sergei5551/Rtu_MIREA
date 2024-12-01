import java.util.LinkedList;
import java.util.Queue;

public class main {
    public static void main(String[] args) {
        StackOnQuene stack = new StackOnQuene();
        // Добавления элементов
        stack.push(5);
        stack.push(6);
        stack.push(7);
        stack.print();

        // Удаление элемента и взятие его
        System.out.println(stack.pop());
        stack.print();

        // Возвращение элемента без удаления
        System.out.println(stack.top());
        stack.print();

        // Пустой ли список?
        if(stack.empty()){
            System.out.println("Стек пустой!");
        }
        else {
            System.out.println("Стек не пустой!");
        }

    }
}

class StackOnQuene{
    int giveLastElement(){
        for(int i = 0; i < queue.size(); i++){
            queueAdditional.add( queue.poll() );
        }

        int lastElement = queue.poll();
        while(!queueAdditional.isEmpty()) {
            queue.add(queueAdditional.poll() );
        }
        return lastElement;
    } // Для уменьшения кода
    void print(){ // Выводит элементы стека
        System.out.println(queue);
    }
    private Queue<Integer> queue = new LinkedList<>();
    private Queue<Integer> queueAdditional = new LinkedList<>();
    void push(int x){
        queue.add(x);
    }
    int pop(){
        return giveLastElement();
    }
    int top(){
        int lastElement = giveLastElement();
        queue.add(lastElement);
        return lastElement;
    }
    boolean empty(){ return queue.isEmpty();}
}
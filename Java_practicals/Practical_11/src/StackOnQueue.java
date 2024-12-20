import java.util.LinkedList;
import java.util.Queue;

public class StackOnQueue {
    private Queue<Integer> queue;

    public StackOnQueue() {
        queue = new LinkedList<>();
    }

    // Метод push добавляет элемент на "верх" стека
    public void push(int x) {
        queue.add(x);
        // Реконструируем очередь так, чтобы новый элемент стал первым
        int size = queue.size();
        for (int i = 0; i < size - 1; i++) {
            queue.add(queue.remove());
        }
    }

    // Метод pop удаляет и возвращает верхний элемент стека
    public int pop() {
        if (empty()) {
            throw new RuntimeException("Stack is empty");
        }
        return queue.remove();
    }

    // Метод top возвращает верхний элемент стека без его удаления
    public int top() {
        if (empty()) {
            throw new RuntimeException("Stack is empty");
        }
        return queue.peek();
    }

    // Метод empty проверяет, пуст ли стек
    public boolean empty() {
        return queue.isEmpty();
    }

    // Метод для строкового представления стека
    @Override
    public String toString() {
        return queue.toString();
    }
}


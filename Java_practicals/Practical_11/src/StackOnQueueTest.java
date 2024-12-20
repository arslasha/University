public class StackOnQueueTest {
    public static void main(String[] args) {
        StackOnQueue stack = new StackOnQueue();

        // Добавляем два значения в стек
        stack.push(10);
        System.out.println("Состояние стека после добавления 10, 20 и 30: " + stack);

        // Выводим объект на вершине без удаления
        System.out.println("Верхний элемент стека (без удаления): " + stack.top());

        // Выводим и удаляем объект на вершине
        System.out.println("Удаляем верхний элемент стека: " + stack.pop());

        // Проверяем, пуст ли стек
        System.out.println("Стек пуст? " + stack.empty());

        // Выводим оставшиеся элементы в стеке
        System.out.println("Оставшиеся элементы в стеке: " + stack);
    }
}

import java.util.Stack;

public class BinaryOperationsWithStack {

    // Стек для хранения значений
    private Stack<Integer> stack;

    // Конструктор инициализирует стек
    public BinaryOperationsWithStack() {
        this.stack = new Stack<>();
    }

    // Операция push добавляет значение в стек
    public void push(int value) {
        stack.push(value);
    }

    // Операция сложения: достаем два верхних элемента, складываем и помещаем результат обратно в стек
    public void add() {
        int b = stack.pop();
        int a = stack.pop();
        stack.push(a + b);
    }

    // Операция вычитания: достаем два верхних элемента, вычитаем и помещаем результат обратно в стек
    public void subtract() {
        int b = stack.pop();
        int a = stack.pop();
        stack.push(a - b);
    }

    // Операция побитового И: достаем два верхних элемента, применяем &, помещаем результат обратно в стек
    public void bitwiseAnd() {
        int b = stack.pop();
        int a = stack.pop();
        stack.push(a & b);
    }

    // Операция побитового ИЛИ: достаем два верхних элемента, применяем |, помещаем результат обратно в стек
    public void bitwiseOr() {
        int b = stack.pop();
        int a = stack.pop();
        stack.push(a | b);
    }

    // Операция сдвига вправо: достаем два верхних элемента, выполняем сдвиг, помещаем результат обратно в стек
    public void rightShift() {
        int shift = stack.pop(); // Число позиций для сдвига
        int a = stack.pop();
        stack.push(a >> shift);
    }

    // Операция деления: достаем два верхних элемента, делим, помещаем результат обратно в стек
    public void divide() {
        int b = stack.pop();
        int a = stack.pop();
        if (b == 0) {
            throw new ArithmeticException("Division by zero");
        }
        stack.push(a / b);
    }

    // Получение результата из верхушки стека
    public int getResult() {
        return stack.peek();
    }
}

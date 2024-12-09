import java.util.function.BinaryOperator;

public class StackExample {
    private static int[] stack = new int[5]; // стек с фиксированным размером
    private static int sp = 0; // указатель на вершину стека

    public static void push(int x) {
        sp++;
        stack[sp] = x;
    }

    public static int pop() {
        int x = stack[sp];
        sp--;
        return x;
    }

    public static void bop(BinaryOperator<Integer> f) {
        int rhs = pop();
        int lhs = pop();
        push(f.apply(lhs, rhs));
    }

    public static void main(String[] args) {
        int x = 4;
        int y = 4;

        push(y);
        push(2);
        bop((a, b) -> a >> b); // Сдвиг вправо
        push(2);
        bop(Integer::sum); // Сложение
        push(x);
        bop(Integer::sum); // Сложение
        push(10);
        bop((a, b) -> a - b); // Вычитание
        push(5);
        bop((a, b) -> a / b); // Деление
        push(3);
        bop((a, b) -> a & b); // Побитовое И

        System.out.println(pop());
    }
}

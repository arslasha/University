public class Main {

    public static void main(String[] args) {
        BinaryOperationsWithStack operations = new BinaryOperationsWithStack();

        // Примеры операций
        operations.push(10); // Добавляем 10 в стек
        operations.push(3);  // Добавляем 3 в стек

        operations.add(); // Складываем верхние два элемента стека (10 + 3)
        System.out.println("Addition result: " + operations.getResult()); // Ожидаем 13

        operations.push(8); // Добавляем 8 в стек
        operations.subtract(); // Вычитаем верхние два элемента (13 - 8)
        System.out.println("Subtraction result: " + operations.getResult()); // Ожидаем 5

        operations.push(6); // Добавляем 6 в стек
        operations.bitwiseAnd(); // Применяем побитовое И (5 & 6)
        System.out.println("Bitwise AND result: " + operations.getResult()); // Ожидаем 4

        operations.push(2); // Добавляем 2 в стек
        operations.bitwiseOr(); // Применяем побитовое ИЛИ (4 | 2)
        System.out.println("Bitwise OR result: " + operations.getResult()); // Ожидаем 6

        operations.push(1); // Добавляем 1 в стек для сдвига
        operations.rightShift(); // Выполняем сдвиг вправо (6 >> 1)
        System.out.println("Right Shift result: " + operations.getResult()); // Ожидаем 3

        operations.push(3); // Добавляем 3 в стек
        operations.divide(); // Делим (3 / 1)
        System.out.println("Division result: " + operations.getResult()); // Ожидаем 3

        
    }
}

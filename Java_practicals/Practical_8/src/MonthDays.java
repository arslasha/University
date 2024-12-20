import java.util.Scanner;

public class MonthDays {
    public static void main(String[] args) {
        // Массивы для названий месяцев и количества дней в каждом месяце
        String[] months = {"Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
                "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"};
        int[] days = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

        Scanner scanner = new Scanner(System.in);
        System.out.print("Введите целое число от 1 до 12: ");

        // Проверяем, что введено целое число
        if (scanner.hasNextInt()) {
            int monthNumber = scanner.nextInt();

            try {
                // Проверка, выбрал ли пользователь февраль
                if (monthNumber == 2) {
                    // Получить год от пользователя
                    System.out.print("Введите год для проверки на високосность: ");
                    if (scanner.hasNextInt()) {
                        int year = scanner.nextInt();
                        // Проверка високосности года
                        if (isLeapYear(year)) {
                            System.out.println("Месяц: " + months[monthNumber - 1]);
                            System.out.println("Количество дней: 29");
                        } else {
                            System.out.println("Месяц: " + months[monthNumber - 1]);
                            System.out.println("Количество дней: 28");
                        }
                    } else {
                        System.out.println("Ошибка: необходимо ввести год в виде целого числа.");
                    }
                } else {
                    // Вывод для всех остальных месяцев
                    System.out.println("Месяц: " + months[monthNumber - 1]);
                    System.out.println("Количество дней: " + days[monthNumber - 1]);
                }
            } catch (ArrayIndexOutOfBoundsException e) {
                // Если число вне диапазона 1-12
                System.out.println("Недопустимое число.");
            }
        } else {
            // Сообщение о неверном вводе, если введено не целое число
            System.out.println("Ошибка: необходимо ввести целое число.");
        }

        scanner.close();
    }

    // Метод для проверки, является ли год високосным
    public static boolean isLeapYear(int year) {
        return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
    }
}

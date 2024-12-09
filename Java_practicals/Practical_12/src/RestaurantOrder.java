import java.util.Scanner;

// Основной класс
public class RestaurantOrder {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        OrderBuilder builder = new OrderBuilder();

        // Ввод основного блюда
        System.out.print("Введите основное блюдо: ");
        String mainDish = scanner.nextLine();
        builder.setMainDish(mainDish);

        // Ввод гарнира
        System.out.print("Введите гарнир (или оставьте пустым): ");
        String sideDish = scanner.nextLine();
        if (!sideDish.isEmpty()) {
            builder.setSideDish(sideDish);
        }

        // Ввод напитка
        System.out.print("Введите напиток: ");
        String drink = scanner.nextLine();
        builder.setDrink(drink);

        // Ввод десерта
        System.out.print("Введите десерт (или оставьте пустым): ");
        String dessert = scanner.nextLine();
        if (!dessert.isEmpty()) {
            builder.setDessert(dessert);
        }

        // Сборка заказа
        Order order = builder.build();

        // Вывод заказа
        System.out.println("\nВаш заказ:");
        System.out.println(order);
    }
}


public class Main {
    public static void main(String[] args) {
        // Создаем экземпляры класса Car с использованием разных конструкторов
        Car car1 = new Car("Merсedes GlE ", "A777AA", "Space black", 2023);
        Car car2 = new Car();
        Car car3 = new Car("BMW M5", 2020);

        // Выводим информацию об автомобилях с помощью метода toString
        System.out.println("Car 1: " + car1.toString());
        System.out.println("Car 2: " + car2.toString());
        System.out.println("Car 3: " + car3.toString());

        // Используем сеттеры для изменения данных
        car2.setModel("Honda Civic");
        car2.setLicense("XY9876ZT");
        car2.setColor("Blue");
        car2.setYear(2018);

        // Вывод обновленной информации о car2
        System.out.println("Updated Car 2: " + car2.toString());

        // Получаем возраст автомобилей
        final int currentYear = 2024; // Текущий год
        System.out.println("Car 1 Age: " + car1.getCarAge(currentYear) + " years");
        System.out.println("Car 2 Age: " + car2.getCarAge(currentYear) + " years");
        System.out.println("Car 3 Age: " + car3.getCarAge(currentYear) + " years");
    }
}

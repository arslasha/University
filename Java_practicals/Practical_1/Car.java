public class Car {
    // Поля класса Car
    private String model;
    private String license;
    private String color;
    private int year;

    // Конструктор, который включает все поля класса
    public Car(String model, String license, String color, int year) {
        this.model = model;
        this.license = license;
        this.color = color;
        this.year = year;
    }

    // Конструктор по умолчанию
    public Car() {
        this.model = "Unknown Model";
        this.license = "Unknown License";
        this.color = "Unknown Color";
        this.year = 2000; // Пример года по умолчанию
    }

    // Конструктор по выбору (с полями модель и год)
    public Car(String model, int year) {
        this.model = model;
        this.license = "Unknown License";
        this.color = "Unknown Color";
        this.year = year;
    }

    // Методы-геттеры для получения значений полей
    public String getModel() {
        return model;
    }

    public String getLicense() {
        return license;
    }

    public String getColor() {
        return color;
    }

    public int getYear() {
        return year;
    }

    // Методы-сеттеры для установки значений полей
    public void setModel(String model) {
        this.model = model;
    }

    public void setLicense(String license) {
        this.license = license;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public void setYear(int year) {
        this.year = year;
    }

    // Метод, который возвращает возраст автомобиля
    public int getCarAge(int currentYear) {
        if (currentYear < this.year)
            return -1;
        else
            return currentYear - this.year;
    }

    // Метод toString() для вывода значений полей экземпляра
    @Override
    public String toString() {
        return "Model: " + model + ", License: " + license + ", Color: " + color + ", Year: " + year;
    }
}

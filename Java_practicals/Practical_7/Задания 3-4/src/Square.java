public class Square extends GeometricObject implements Colorable {
    // Поле данных для стороны квадрата
    private double side;

    // Конструктор по умолчанию, задающий сторону 0
    public Square() {
        this.side = 0.0;
    }

    // Конструктор, задающий сторону квадрата
    public Square(double side) {
        this.side = side;
    }

    // Getter для стороны квадрата
    public double getSide() {
        return side;
    }

    // Setter для стороны квадрата
    public void setSide(double side) {
        this.side = side;
    }

    // Метод для вычисления площади квадрата
    public double getArea() {
        return side * side;
    }

    // Метод для вычисления периметра квадрата
    public double getPerimeter() {
        return 4 * side;
    }

    // Реализация метода howToColor() из интерфейса Colorable
    @Override
    public void howToColor() {
        System.out.println("Раскрасьте все четыре стороны.");
    }

    @Override
    public String toString() {
        return "Квадрат: сторона = " + side;
    }
}

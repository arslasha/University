public class Circle extends GeometricObject {
    private double radius;

    /** Создает по умолчанию заданный круг */
    public Circle() {
    }

    /** Создает круг с указанным радиусом */
    public Circle(double radius) {
        this.radius = radius;
    }

    /** Возвращает радиус */
    public double getRadius() {
        return radius;
    }

    /** Присваивает новый радиус */
    public void setRadius(double radius) {
        this.radius = radius;
    }

    /** Возвращает площадь */
    @Override
    public double getArea() {
        return Math.PI * Math.pow(radius, 2);
    }

    /** Возвращает диаметр */
    public double getDiameter() {
        return 2 * radius;
    }

    /** Возвращает периметр */
    @Override
    public double getPerimeter() {
        return 2 * Math.PI * radius;
    }

    /** Отображает информацию о круге */
    @Override
    public String toString() {
        return "Круг: радиус = " + radius;
    }
}

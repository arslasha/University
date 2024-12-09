public class TestColorable {
    public static void main(String[] args) {

        GeometricObject[] objects = new GeometricObject[5];
        objects[0] = new Square(3.0);  // Квадрат
        objects[1] = new Square(5.0);  // Квадрат
        objects[2] = new Circle(2.0);  // Круг
        objects[3] = new Rectangle(4.0, 6.0);  // Прямоугольник
        objects[4] = new Square(4.0);  // Квадрат

        for (GeometricObject object : objects) {
            System.out.println("Площадь объекта: " + object.getArea());

            // Проверяем, является ли объект Colorable
            if (object instanceof Colorable) {
                ((Colorable) object).howToColor();
            }
        }
    }
}

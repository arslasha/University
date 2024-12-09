import java.util.Objects;
import java.util.Scanner;

public class TestTriangle {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        try {
            System.out.print("Введите первую сторону треугольника: ");
            double side1 = input.nextDouble();

            System.out.print("Введите вторую сторону треугольника: ");
            double side2 = input.nextDouble();

            System.out.print("Введите третью сторону треугольника: ");
            double side3 = input.nextDouble();

            System.out.print("Треугольник закрашен (д/н)? ");
            boolean isFilled = Objects.equals(input.next(), "д");

            String color = null;
            if (isFilled) {
                System.out.print("Введите цвет треугольника: ");
                color = input.next();
            }

            Triangle triangle = new Triangle(side1, side2, side3);
            triangle.setColor(color);
            triangle.setFilled(isFilled);

            System.out.println("\n" + triangle);
            System.out.println("Площадь: " + triangle.getArea());
            System.out.println("Периметр: " + triangle.getPerimeter());

            String filledSummary = triangle.isFilled() ? "да" : "нет";
            System.out.println("Закрашен: " + filledSummary);
            if (triangle.isFilled()) {
                System.out.println("Цвет: " + triangle.getColor());
            }
        } catch (IllegalTriangleException e) {
            System.out.println("Ошибка: " + e.getMessage());
        }
    }
}

public abstract class GeometricObject implements Comparable<GeometricObject> {
    private String color;
    private boolean filled;

    public GeometricObject() {
        this("white", false);
    }

    public GeometricObject(String color, boolean filled) {
        this.color = color;
        this.filled = filled;
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = (color != null) ? color : "отсутствует";
    }

    public boolean isFilled() {
        return filled;
    }

    public void setFilled(boolean filled) {
        this.filled = filled;
    }

    // Абстрактные методы, которые должны быть реализованы в подклассах
    public abstract double getArea();
    public abstract double getPerimeter();

    // Реализация интерфейса Comparable для сравнения по площади
    @Override
    public int compareTo(GeometricObject o) {
        return Double.compare(this.getArea(), o.getArea());
    }

    // Метод для нахождения максимального объекта
    public static GeometricObject max(GeometricObject o1, GeometricObject o2) {
        return (o1.compareTo(o2) >= 0) ? o1 : o2;
    }

    @Override
    public String toString() {
        return "GeometricObject[color=" + color + ", filled=" + filled + "]";
    }
}

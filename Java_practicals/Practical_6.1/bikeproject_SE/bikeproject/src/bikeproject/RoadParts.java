package bikeproject;

public interface RoadParts {
    String TERRAIN = "track_racing"; // Константа для типа местности

    int getTyreWidth(); // Метод для получения ширины шин
    void setTyreWidth(int newValue); // Метод для установки ширины шин

    int getPostHeight(); // Метод для получения высоты стойки
    void setPostHeight(int newValue); // Метод для установки высоты стойки
}

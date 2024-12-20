public interface BikeParts {
    String MAKE = "Oracle Cycles";
    default String getMake() {  // Метод для получения названия производителя
        return MAKE;
    }
}

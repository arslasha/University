// Класс Order, представляющий заказ
class Order {
    private String mainDish; // Основное блюдо
    private String sideDish; // Гарнир
    private String drink;    // Напиток
    private String dessert;  // Десерт

    public void setMainDish(String mainDish) {
        this.mainDish = mainDish;
    }

    public void setSideDish(String sideDish) {
        this.sideDish = sideDish;
    }

    public void setDrink(String drink) {
        this.drink = drink;
    }

    public void setDessert(String dessert) {
        this.dessert = dessert;
    }

    @Override
    public String toString() {
        return "Order {" +
                "Main Dish='" + mainDish + '\'' +
                ", Side Dish='" + sideDish + '\'' +
                ", Drink='" + drink + '\'' +
                ", Dessert='" + dessert + '\'' +
                '}';
    }
}

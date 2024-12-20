package bikeproject;

public class BikeDriver {

	public static void main(String[] args) {

		RoadBike bike1 = new RoadBike();
		bike1.setPostHeight(20); // Обновлённая высота стойки

		RoadBike bike2 = new RoadBike("drop", "tourer", "semi-grip", "comfort", 14, 25, 18);
		MountainBike bike3 = new MountainBike();
		Bike bike4 = new Bike();

		bike1.printDescription();
		bike2.printDescription();
		bike3.printDescription();
		bike4.printDescription();

		System.out.println("Updated post height for bike1: " + bike1.getPostHeight()); // Вывод значения высоты стойки
	}//end method main
}//end class BikeDriver

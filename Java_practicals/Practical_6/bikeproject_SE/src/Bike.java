public class Bike implements BikeParts {

	private String handleBars, frame, tyres, seatType;
	private int NumGears;

	public Bike(){}

	public Bike(String handleBars, String frame, String tyres, String seatType, int numGears) {
		this.handleBars = handleBars;
		this.frame = frame;
		this.tyres = tyres;
		this.seatType = seatType;
		NumGears = numGears;
    }//end constructor

	protected void printDescription()
	{
		System.out.println("\n" + MAKE + "\n"
				+ "This bike has " + this.handleBars + " handlebars on a "
				+ this.frame + " frame with " + this.NumGears + " gears."
				+ "\nIt has a " + this.seatType + " seat with " + this.tyres + " tyres.");
	}//end method printDescription

	@Override
	public String getMake() {
		return MAKE; // Реализация метода из интерфейса
	}

}//end class Bike

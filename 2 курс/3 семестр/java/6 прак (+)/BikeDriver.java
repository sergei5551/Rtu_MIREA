package bikeproject;

public class BikeDriver {

	public static void main(String[] args) {
		
		RoadBike bike1 = new RoadBike();
		RoadBike bike2 = new RoadBike("drop", "tourer", "semi-grip", "comfort", 14, 25, 18);		
		MountainBike bike3 = new MountainBike();
		Bike bike4 = new Bike();
		
		bike1.printDescription();
		bike2.printDescription();
		bike3.printDescription();
		bike4.printDescription();

		///////////////////////////////////
		for(int i = 0; i < 100; i++) {
			System.out.print("--");
		}
		System.out.println();
		///////////////////////////////////

		bike1.setPostHeight(20);
		bike1.printDescription();
	}//end method main

}//end class BikeDriver

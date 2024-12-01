package app;
import vehicles.Car;
import vehicles.ElectricCar;
import vehicles.Vehicl;

public class TestCar {
    public static void main(String[] args){


        Vehicl car_ordin = new Car();
        Vehicl car_elec = new ElectricCar();

        car_ordin.setColor("Yellow");
        car_ordin.setLicense("AB102");
        car_ordin.setModel("Haval Jolion");
        car_ordin.setOwnerName("Михаил");
        car_ordin.setYear(2016);

        car_elec.setColor("White");
        car_elec.setLicense("DS43C");
        car_elec.setModel("Lada Vesta");
        car_elec.setOwnerName("Константин");
        car_elec.setYear(2005);

        System.out.println(car_ordin.toString() + "\n" + car_elec.toString());


    }
}



package app;

import vehicles.Car;
import vehicles.ElectricCar;
import vehicles.Vehicl;

public class TestCar {
    public static void main(String[] args){

        //1
        Vehicl car_ordin = new Car();
        ElectricCar car_elec = new ElectricCar();

        //2 и 3
        car_ordin.setOwnerName("Михаил");
        car_ordin.setYear(2016);
        car_ordin.setLicense("AB102");

        car_elec.setOwnerName("Константин");
        car_elec.setYear(2005);
        car_elec.setLicense("DS43C");

        //4
        System.out.println("Батарея электрокара: " + car_elec.getBatteryCapacity());
        //5
        System.out.println(car_ordin.toString() + "\n" + car_elec.toString());


    }
}



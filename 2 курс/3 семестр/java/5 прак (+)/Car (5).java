package vehicles;


public class Car extends Vehicl {
    protected String engineType;

    public Car(){
        engineType = "Combustion";
    }

    @Override
    public String vehiclType(){
        return "Car";
    };

}
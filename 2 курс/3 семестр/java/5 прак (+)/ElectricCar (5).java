package vehicles;

public class ElectricCar extends Car implements ElectricVehicle {
    private int batteryCapacity;

    public ElectricCar(){
        this.engineType = "Electric";
    }

    @Override
    public int getBatteryCapacity(){
        return batteryCapacity;
    };
    @Override
    public void setBatteryCapacity(int batteryCapacity){
        this.batteryCapacity = batteryCapacity;
    };

    @Override
    public String vehiclType(){
        return "Electric Car";
    }

}
package vehicles;

public class ElectricCar extends Car{


    @Override
    public String vehiclType(){
        return "Electric Car";
    }

    private int batteryCapacity;

    public int getBatteryCapacity() {
        return batteryCapacity;
    }

    public void setBatteryCapacity(int batteryCapacity) {
        this.batteryCapacity = batteryCapacity;
    }
}
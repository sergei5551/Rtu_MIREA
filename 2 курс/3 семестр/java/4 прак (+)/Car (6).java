package vehicles;

public class Car extends Vehicl {
    protected String engineType;

    @Override
    public String vehiclType(){
        return "Car";
    };

    @Override
    public String toString() {
        return "Машина: {" +
                "engineType='" + this.vehiclType() + '\'' +
                ", model='" + model + '\'' +
                ", license='" + license + '\'' +
                ", color='" + color + '\'' +
                ", year=" + year +
                ", ownerName='" + ownerName + '\'' +
                '}';
    }
}
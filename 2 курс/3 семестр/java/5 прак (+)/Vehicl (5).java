package vehicles;

public abstract class Vehicl {

    protected String model;
    protected String license;
    protected String color;
    protected int year;
    protected String ownerName;
    protected String insuranceNumber;
    private String engineType;

    protected abstract String vehiclType();

    public int getYear() {
        return year;
    }

    public String getColor() {
        return color;
    }

    public String getLicense() {
        return license;
    }

    public String getModel() {
        return model;
    }

    public String getOwnerName() {
        return ownerName;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public void setLicense(String license) {
        this.license = license;
    }

    public void setModel(String model) {
        this.model = model;
    }

    public void setOwnerName(String ownerName) {
        this.ownerName = ownerName;
    }

    public void setYear(int year) {
        this.year = year;
    }

    public String getInsuranceNumber() {return insuranceNumber;}

    public void setInsuranceNumber(String insuranceNumber) {this.insuranceNumber = insuranceNumber;}

    @Override
    public String toString() {
        return "Vehicl{" +
                "model='" + model + '\'' +
                ", license='" + license + '\'' +
                ", color='" + color + '\'' +
                ", year=" + year +
                ", ownerName='" + ownerName + '\'' +
                ", insuranceNumber='" + insuranceNumber + '\'' +
                ", engineType='" + vehiclType() + '\'' +
                '}';
    }
}
package vehicles;

public abstract class Vehicl {

    protected String model;
    protected String license;
    protected String color;
    protected int year;
    protected String ownerName;
    private String engineType;

    abstract String vehiclType();

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


}
package Java2Day4;

class Motorcycle extends Vehicle {
    private boolean hasSidecar;
    private int engineCapacity;

    public Motorcycle(String make, String model, int year, double price, boolean hasSidecar, int engineCapacity) {
        super(make, model, year, price);
        this.hasSidecar = hasSidecar;
        this.engineCapacity = engineCapacity;
    }

    public void setHasSidecar(boolean hasSidecar) {
        this.hasSidecar = hasSidecar;
    }

    public boolean getHasSidecar() {
        return hasSidecar;
    }

    public void setEngineCapacity(int engineCapacity) {
        this.engineCapacity = engineCapacity;
    }
    public int getEngineCapacity(){
        return engineCapacity;
    }
    @Override
    public String details() {
        return "-----CAR DETAILS-----" + "\n" +
                "Material: " + make + "\n" +
                "Model: " + model + "\n" +
                "Year: " + year + "\n" +
                "Price: " + price + "\n" +
                "Has A Sidecar " + hasSidecar + "\n" +
                "Engine capacity: " + engineCapacity;
    }

    public void calculateSpeed() {

    }
}

package Java2Day4;

abstract class Vehicle {
    protected String make;
    protected String model;
    protected int year;
    protected double price;

    public Vehicle(String make, String model, int year, double price){
    this.make = make;
    this.model = model;
    this.year = year;
    this.price = price;
    }
    //setter for make
    public void setMake(String make){
        this.make = make;
    }
    //getter for make
    public String getMake() {
        return make;
    }
    //setter for model
    public void setModel(String model){
        this.model= model;
    }
    //getter for model
    public String getModel() {
        return model;
    }
    //setter for year
    public void setYear(int year){
        this.year = year;
    }
    //getter for year
    public int getYear() {
        return year;
    }
    //setter for price
    public void setPrice(int price){
        this.price = price;
    }
    //getter for price
    public double getPrice() {
        return price;
    }
    public abstract String details();


}

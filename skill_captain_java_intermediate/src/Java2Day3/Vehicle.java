package Java2Day3;

public class Vehicle {
    //instance variables
    public String brand;
    public String model;
    public int year;
    public int rentalPrice;

    //setter for brand
    public void setBrand(String brand){
        this.brand = brand;
    }
    //getter for brand
    public String getBrand(String brand){
       return brand;
    }
    //setter for model
    public void setModel(String model){
       this.model = model;
    }
    //getter for model
    public String getModel(){
        return  model;
    }
    //setter for year
    public void setYear(int year){
         this.year = year;
    }
    public int getYear(int  year){
        return year;
    }
    //setter for rental price
    public void setRentalPrice(int rentalPrice){
         this.rentalPrice = rentalPrice;
    }
    public int getRentalPrice(int rentalPrice){
        return rentalPrice;
    }

    public String toString() {
 return "Brand: " + brand + "\n" +
         "Model: " + model +"\n" +
         "Year: " + year + "\n" +
         "Rental Price: " + rentalPrice;
    }
}
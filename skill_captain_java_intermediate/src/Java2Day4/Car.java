package Java2Day4;

 class Car extends Vehicle{
    private int numDoors;
    private String fuelType;

    public Car(String make, String model, int year, double price, int numDoors, String fuelType ){
        super(make, model, year, price);
        this.numDoors = numDoors;
         this.fuelType = fuelType;


    }
    public void setNumDoors(int numDoors){
        this.numDoors= numDoors;
    }
    public int getNumDoors(){
        return numDoors;
    }
     public void setFuelType(String fuelType){
         this.numDoors= numDoors;
     }
     public String getFuelType(){
         return fuelType;
     }
    public int calculateMileage(){
        return 0;
    }
 @Override
     public String details(){
     return "-----CAR DETAILS-----"+"\n"+
             "Material: "+ make + "\n" +
             "Model: " + model + "\n" +
             "Year: " + year + "\n" +
             "Price: "+ price+"\n"+
              "Number of doors: " +numDoors+ "\n"+
              "Fuel Type: " + fuelType;
 }
}

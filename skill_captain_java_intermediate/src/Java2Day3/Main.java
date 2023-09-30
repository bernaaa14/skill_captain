package Java2Day3;

public class Main {
    public static void main(String[] args) {
        Car car = new Car();
        car.setBrand("Maserati");
        car.setModel("MC20");
        car.setYear(2022);
        car.setRentalPrice(10000);
        car.setNumOfSeats(5);

        Motorcycle motorcycle = new Motorcycle();
        motorcycle.setBrand("Honda");
        motorcycle.setModel("CBR650R ");
        motorcycle.setYear(2021);
        motorcycle.setRentalPrice(2000);
        motorcycle.setEngineCapacity(1000);

        //display information
        System.out.println(car);
        System.out.println("------------");
        System.out.println(motorcycle);
    }
}

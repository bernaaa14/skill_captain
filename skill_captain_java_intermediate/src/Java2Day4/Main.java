package Java2Day4;

import java.util.ArrayList;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Vehicle> inventory = new ArrayList<>();
        //ask user for input for the inventory functionalities
        while (true) {
            System.out.println("Please select an option");
            System.out.println("1: Add Car");
            System.out.println("2: Add Motorcycle");
            System.out.println("3: Display Inventory Details");
            System.out.println("4: Update the vehicle details");
            System.out.println("5: Search for a vehicle based on given attributes");
            System.out.println("6: Remove a vehicle");
            System.out.println("0: Exit");

            int choice = sc.nextInt();
            sc.nextLine();
            switch (choice) {
                //case for adding car
                case 1:
                    System.out.println("Enter Car details (Make, Model, Year, Price, Number of Doors, Fuel Type):");
                    String carInput = sc.nextLine();
                    //array to store car details
                    String[] carDetails = carInput.split(",");
                    //ensure to have 6 parts for input and trim any whitespace
                    if (carDetails.length == 6) {
                        String carMake = carDetails[0].trim();
                        String carModel = carDetails[1].trim();
                        int carYear = Integer.parseInt(carDetails[2].trim());
                        double carPrice = Double.parseDouble(carDetails[3].trim());
                        int carNumOfDoors = Integer.parseInt(carDetails[4].trim());
                        String carFuelType = carDetails[5].trim();
                        // create a Car object and add it to the inventory
                        inventory.add(new Car(carMake, carModel, carYear, carPrice, carNumOfDoors, carFuelType));
                    } else {
                        System.out.println("Invalid format");
                    }
                    break;
                case 2:
                    System.out.println("Enter Motorcycle details (Make, Model, Year, Price, Has Sidecar, Engine Capacity):");
                    //array to store motorcycle details
                    String motorcycleInput = sc.nextLine();
                    String[] motorcycleDetails = motorcycleInput.split(",");
                    //ensure to have 6 parts for input and trim any whitespace
                    if (motorcycleDetails.length == 6) {
                        String motorcycleMake = motorcycleDetails[0].trim();
                        String motorcycleModel = motorcycleDetails[1].trim();
                        int motorcycleYear = Integer.parseInt(motorcycleDetails[2].trim());
                        double motorcyclePrice = Double.parseDouble(motorcycleDetails[3].trim());
                        boolean motorcycleHasSidecar = Boolean.parseBoolean(motorcycleDetails[4].trim());
                        int motorcycleEngineCapacity = Integer.parseInt(motorcycleDetails[5].trim());
                        inventory.add(new Motorcycle(motorcycleMake, motorcycleModel, motorcycleYear, motorcyclePrice, motorcycleHasSidecar, motorcycleEngineCapacity));
                    } else {
                        System.out.println("Invalid input");
                    }
                    break;
                case 3:
                    System.out.println("Current Inventory List:");
                    //iterate over the list and print
                    for (Vehicle vehicle : inventory) {
                        System.out.println(vehicle.details());
                    }
                    break;
                case 4:
                    System.out.println("Enter the index of the vehicle you want to update; starting from 0 (first input) to 1 and so on and so forth");
                    int updateIndex = sc.nextInt();
                    //ensuring that the index is within the bounds
                    if (updateIndex >= 0 && updateIndex < inventory.size()) {
                        //get the index of the vehicle to be updated
                        Vehicle vehicleToUpdate = inventory.get(updateIndex);
                        System.out.println("Enter updated details for the vehicle:");
                        System.out.print("Make: ");
                        //setMake method to update the vehicle attributes
                        vehicleToUpdate.setMake(sc.next());
                        System.out.print("Model: ");
                        vehicleToUpdate.setModel(sc.next());
                        System.out.print("Year: ");
                        vehicleToUpdate.setYear(sc.nextInt());
                        System.out.print("Price: ");
                        vehicleToUpdate.setPrice((int) sc.nextDouble());
                        sc.nextLine();
                        //test if the object is an instance of a Car
                        if (vehicleToUpdate instanceof Car) {
                            //access car specified methods
                            Car carToUpdate = (Car) vehicleToUpdate;
                            //ask the user for the update of the number of doors
                            System.out.print("Number of Doors: ");
                            carToUpdate.setNumDoors(sc.nextInt());
                            //ask the user for the update of the number of fuel type
                            System.out.print("Fuel Type: ");
                            carToUpdate.setFuelType(sc.next());
                        }
                        //test if the object is an instance of a Motorcycle
                        else if (vehicleToUpdate instanceof Motorcycle) {
                            Motorcycle motorcycleToUpdate = (Motorcycle) vehicleToUpdate;
                            System.out.print("Has Sidecar (Yes/No): ");
                            motorcycleToUpdate.setHasSidecar(sc.nextBoolean());
                            System.out.print("Engine Capacity: ");
                            motorcycleToUpdate.setEngineCapacity(sc.nextInt());
                        }
                        System.out.println("Vehicle details updated successfully.");
                    } else {
                        System.out.println("Invalid index.");
                    }
                    break;
                case 5:
                    System.out.println("Search for a vehicle based on given attributes:");
                    System.out.println("1: Search by Make");
                    System.out.println("2: Search by Model");
                    System.out.println("3: Search by Price Range");
                    int searchOption = sc.nextInt();
                    sc.nextLine();
                    switch (searchOption) {
                        case 1:
                            System.out.print("Enter Make: ");
                            String searchMake = sc.nextLine();
                            //iterate on the list, retrieve the value
                            //make case-insensitive, print the details of the matching vehicle
                            for (Vehicle vehicle : inventory) {
                                if (vehicle.getMake().equalsIgnoreCase(searchMake)) {
                                    vehicle.details();
                                }
                            }
                            break;
                        case 2:
                            System.out.print("Enter Model: ");
                            String searchModel = sc.nextLine();
                            //iterate over the list, if current model matches search model print the details
                            for (Vehicle vehicle : inventory) {
                                if (vehicle.getModel().equalsIgnoreCase(searchModel)) {
                                    vehicle.details();
                                }
                            }
                            break;
                        case 3:
                            System.out.print("Enter price: ");
                            double searchPrice = sc.nextDouble();
                            //iterate over the list, if current price matches the search price, print the details
                            for (Vehicle vehicle : inventory) {
                                if (vehicle.getPrice()==searchPrice) {
                                    System.out.println(vehicle.details());
                                }
                            }
                            break;
                        default:
                            System.out.println("Invalid search option.");
                            break;
                    }
                    break;
                case 6:

                    System.out.println("Enter the index of the vehicle you want to remove:");
                    int removeIndex = sc.nextInt();
                    //ensuring that the index is within the bounds, once true use remove method to remove given index
                    if (removeIndex >= 0 && removeIndex < inventory.size()) {
                        Vehicle removedVehicle = inventory.remove(removeIndex);
                        System.out.println("Removed the following vehicle:");
                        removedVehicle.details();
                    } else {
                        System.out.println("Invalid index.");
                    }
                    break;
                case 0:
                    System.out.println("Exiting the program.");
                    sc.close();
                    System.exit(0);
                    break;
                default:
                    System.out.println("Invalid option. Please try again.");
                    break;
            }
        }
    }
}


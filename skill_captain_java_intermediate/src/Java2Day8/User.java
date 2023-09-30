package Java2Day8;

public class User {
    //instance variables
    String name;
    String email;
    String password;
    String address;

    //constructor for the User class
    public User(String name, String email, String password, String address) {
        this.name = name;
        this.email = email;
        this.password = password;
        this.address = address;
    }

    //setter for name
    public void setName(String name) {
        this.name = name;
    }

    //getter for name
    public String getName() {
        return name;
    }

    //setter for email
    public void setEmail(String email) {
        this.email = email;
    }

    //getter for email
    public String getEmail() {
        return email;
    }

    //setter for password
    public void setPassword(String name) {
        this.password = password;
    }

    //getter for password
    public String getPassword() {
        return password;
    }

    //setter for address
    public void setAddress(String name) {
        this.address = address;
    }

    //getter for address
    public String getAddress() {
        return address;
    }


}

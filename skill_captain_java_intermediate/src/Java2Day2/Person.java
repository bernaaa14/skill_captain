package Java2Day2;

public class Person {
    //instance variables
    private String name;
    private int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    //setters
    public void setName(String newName) {
        this.name = newName;

    }

    public void setAge(int newAge) {
        this.age = newAge;

    }

    //getters
    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    //print the output
    public String toString() {
        return "Name: " + getName() + " you are " + getAge() + " years old";
    }
}

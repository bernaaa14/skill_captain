package Java2Day8;

import java.util.ArrayList;

public class UserRepository {
    private ArrayList<User> users = new ArrayList<>();

    public void addUser(User user) {
        users.add(user);
    }

    public User getUser(String email) {
        for (User user : users) {
            if (user.getEmail().equals(email)) {
                return user; // Return the user if the email matches
            }
        }
        return null; // Return null if no user with the given email is found
    }

    public boolean contains(String email) {
        for (User user : users) {
            if (user.getEmail().equals(email)) {
                return true; // Email is already registered
            }
        }
        return false;
    }

    public ArrayList<User> getAllUsers() {
        return users;
    }
}
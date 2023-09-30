package Java2Day5;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

//implement the MusicPlayer interface
class MyMusicPlayer implements MusicPlayer {
    private List<String> playlist; //store the songs
    private Scanner sc; //ask for user input

    //constructor for this class
    public MyMusicPlayer() {
        playlist = new ArrayList<>();
        sc = new Scanner(System.in);
    }

    //to be called in the main method
    public void start() {
        System.out.println("Starting Music Player....");

        boolean isRunning = true;
        while (isRunning) {
            menuOptions();//display menu options as long as its running
            int choice = sc.nextInt();
            sc.nextLine();

            switch (choice) {
                case 1:
                    play();
                    break;
                case 2:
                    pause();
                    break;
                case 3:
                    stop();
                    break;
                case 4:
                    addSong();
                    break;
                case 5:
                    removeSong();
                    break;
                case 6:
                    display();
                    break;
                case 7:
                    shuffle();
                    break;
                case 0:
                    isRunning = false;
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }
    }

    //method to list the menu options
    private void menuOptions() {
        System.out.println("Please select an option");
        System.out.println("1: Play song");
        System.out.println("2: Pause song");
        System.out.println("3: Stop song");
        System.out.println("4: Add song");
        System.out.println("5: Remove Song");
        System.out.println("6: Display current playlist");
        System.out.println("7: Shuffle playlist");
        System.out.println("0: Exit");
    }

    //implement play method from the MusicPlayer Interface
    @Override
    public void play() {
        System.out.println("Playing...");
    }

    //implement stop method from the MusicPlayer Interface
    @Override
    public void pause() {
        System.out.println("Pausing...");
    }

    //implement stop method from the MusicPlayer Interface
    @Override
    public void stop() {
        System.out.println("Stopped...");
    }

    @Override
    public void addSong(String song) {
        //empty method, not used in class
    }

    @Override
    public void removeSong(String song) {
        //empty method, not used in class
    }

    //add songs to the playlist
    public void addSong() {
        System.out.println("Enter a song to add: ");
        String addSong;
        while (true) {
            addSong = sc.nextLine();
            if (addSong.isEmpty()) {
                break;
            }
            playlist.add(addSong);
        }
    }

    //remove songs to the playlist
    public void removeSong() {
        System.out.println("Enter a song you want to remove: ");
        String removeSong = sc.nextLine();
        boolean removed = playlist.remove(removeSong);
        if (removed) {
            System.out.println(removeSong + " has been removed from the playlist.");
        } else {
            System.out.println(removeSong + " was not found in the playlist.");
        }
    }

    //method to iterate and display each elements
    public void display() {
        System.out.println("Current Playlist:");
        for (String song : playlist) {
            System.out.println(song);
        }
    }

    //method to shuffle the playlist
    public void shuffle() {
        Collections.shuffle(playlist);
        System.out.println("Playlist shuffled.");
    }
}
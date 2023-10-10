import threading

# Function for Jimmy Page playing acoustic guitar intro
def guitar_intro():
    print("Jimmy Page: Playing acoustic guitar intro...")

# Function for Robert Plant starting vocals after the guitar intro
def vocal_begins():
    print("Robert Plant: Starts vocals  after the intro... ")

# Function for John Bonham adding drum beats
def adding_drums():
    print("John Bonham: Adds rocking drum beats...")

# Creating a thread for each person involved in the task
jimmy_page_thread = threading.Thread(target=guitar_intro())
robert_plant_thread = threading.Thread(target=vocal_begins())
john_bonham_thread = threading.Thread(target=adding_drums())

# Start each thread to run independently and concurrently with other threads
jimmy_page_thread.start()
robert_plant_thread.start()
john_bonham_thread.start()

# Tells our main thread to wait for another thread to finish
jimmy_page_thread.join()
robert_plant_thread.join()
john_bonham_thread.join()

# Message to print once all the threads are finished executing
print("Hope you enjoyed one of the greatest rock song ever written")
print("\m/  (  -_-   )  \m/")

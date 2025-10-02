# Artist Setlist & Tour Location Prediction Program
A program (Python) that predicts a music artist's setlist based on song popularity and the tour locations based on region popularity from past limited Spotify Data. 

DETAILS: 
The program will take a Spotify data file and determine tour locations (amount based on user input of how many stops they want) and a setlist (length based on user input on how many songs they want). The program will determine the tour locations by selecting n-amount of locations with the highest music streams. Similarly, the program will select n-amount of songs based on the highest amount of streams. The output would be a file containing the location list and the setlist. 
 
INSTRUCTIONS:
1. When running the code, you will be prompted to enter a music artist’s name. If the code does not accept the input, it will output “Artist Not Found”, and you will have to rerun the program to “try-again”. Check capitalization/format of the artist’s name.  
2. If the artist is found in the dataset, it will prompt the user to provide an integer for the number of songs they want on the predicted setlist. If the number of songs input exceeds the number of songs (by the selected artist) in the dataset, the program will output “ERROR SETLIST_LENGTH EXCEEDS SONGS AVAILABLE”, which means the user will have to restart the program to “try-again”. 
3. Lastly, the program will prompt the user to provide an integer for the number of locations they want in the tour-stops. If the number of locations input exceeds the number of locations in the dataset, the program will output “ERROR TOURLIST_LENGTH EXCEEDS LOCATIONS AVAILABLE”, which means the program will end. 
4. If all inputs are acceptable, the program will run as intended and store the Setlist and Tour-list in a separate file. The output will be “Setlist and Tourlist stored in {artist}_TOURLIST_AND_SETLIST.txt file”.  

* Please note that this dataset contains limited data on specific artists [Ex: The Beatles, only has 1 song stored in the database]
  
* Includes an example output file

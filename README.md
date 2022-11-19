# weather-app

## The process I followed

### Step 1: Learn more about CLI apps

My first focus was to understand the option to build CLI apps in python. 

The two popular options I came came across: 
* [click](https://click.palletsprojects.com/)
* [typer](https://typer.tiangolo.com/)

I chose click because the package page had example code which I can understand. 

### Step 2: Understanding the openweather.org api

I wanted to understand how the API works, as well as looking at examples of others using the API I came across [this video](https://www.youtube.com/watch?v=jpsmNr4-v4Y&t=324s) by pythonology. 

Although it covered a lot it did not solve the following problems:
* Grabbing the Lat Long coordinates, they use city name.
* The solution didn't read in user arguments. It does show it at the beginning of the video, but the tutorial doesn't show you how to read in user arguments.
* The solution does not do any file handling.

### Step 3: Coding

As I said above, I used the knowledge from the video to understand how the API works.

From there I solved the problem in the following order: 

1. Extracting the lat long
2. Creating a filename that will be formatted the same regardless if the user uses "Cape Town" or "cape town", also taking into account that it is not best practice to use whitespace characters in file names.
3. Connected to my two chosen APIs and pulled that data from them.
4. Added the funciton to check if the file exists or not.
5. Added functionality to check the last modified date of the file and subtract that from todays epoch time
6. Added else clause that will populate the text file.
7. Enhanced the formatting of the text file.
8. Completed the if statement to retrieve the existing file and display that file.

### Step 4: Documentation and Comments

My last step was to convert my single functions into two smaller functions, as well as adding docstrings to them. This might not be necessary for an app as small as this, but I wanted to demonstrate my ability to document functions.

Lastly, I added comments to make the code easier for another developer to read. 

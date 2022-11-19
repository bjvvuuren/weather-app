import click
import requests
import os
import datetime

# Using decorators to initiate the clicks package to ask the user for their city
@click.command()
@click.option('--city_name', prompt='What is the name of your city?')


def get_weather(city_name):
    """
        Uses a user argument to pull Weather Data from openweathermap.org; saves that data to a file, and prints it.
      
        Arguments:
          city_name: a user provided string
          
    """
    app_id = '83b49d3c8386ed41b745a115b0f21470'
  
  
    def get_data(app_id, city_name):
        """
          Pulls Airpolution and Current Weather Data from openweathermap.org
      
          Arguments:
              app_id: a string
              city_name: a string
          
          Returns:
              A filename, the airpolution data, and the current weather data
        """

    
        # Gets the latitude and longditude of the city
        lat_log_url = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={app_id}'  
        lat_long_data = requests.get(lat_log_url).json()
        lat = lat_long_data[0]['lat']
        long = lat_long_data[0]['lon']
        
        # Replaced whitespaces with _ and converts cityname to lowercast
        city = city_name.replace(" ","_").lower()
        file_name = f'{city}_{lat}_{long}.txt'
      
        # Gets the airpolution and weather data from openweather.org
        airpolution_url =f'http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={long}&appid={app_id}'
        current_weather_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={app_id}&units=metric'
        airpolution_data = requests.get(airpolution_url).json()
        current_weather_data = requests.get(current_weather_url).json()
    

        return file_name, airpolution_data, current_weather_data



      def file_creation(file_name, airpolution_data, current_weather_data):
          """
          Checks if a file that is less than 3 hours old already exists, if it doesn't it populates a file with weather data.
      
          Arguments:
              file_name: A String
              airpolution_data: JSON Output
              current_weather_data: JSON Output
          
          """
      
          # Checks if file exists and is not older than 3 hours then displays that file.
          file_exists = os.path.isfile(file_name)
          if file_exists and datetime.datetime.now().timestamp() -os.path.getmtime(file_name) < 10800:
            
            f = open(file_name, "r")
            print(f.read())
      
          else:
            # Extracts the relevant data from the JSON output and formats that output to be added to a txt file
            aqi = 'Air Quality Index : ' + str(airpolution_data['list'][0]['main']['aqi']) + '\n'
            no2 = 'NO2 Levels: ' + str(airpolution_data['list'][0]['components']['no2']) + '\n'
            pm10 = 'PM10 Levels: ' + str(airpolution_data['list'][0]['components']['pm10'])+'\n'
            conditions = 'Current Conditions: ' + str(current_weather_data['weather'][0]['main']) + '\n'
            temperature = 'Current Temprateure: ' + str(current_weather_data['main']['temp']) + ' Celius \n'
        
            # h1 & h2 are user friendly headings to give context to the data
            h1 = f'Current Weather in {city_name} \n'
            h2 = f'Current Air Quality in {city_name} \n'
            
            # Creates/updated the file with data
            f = open(file_name, "a+")
            f.writelines([h1,conditions,temperature,'\n',h2,aqi,no2,pm10])
        
            # Prints the output of the file to the terminal
            f = open(file_name, "a+")
            print(f.read())


  current_file, airpolution_data, current_weather_data= get_data(app_id,city_name)
  file_creation(current_file, airpolution_data, current_weather_data)


if __name__ == '__main__':
    get_weather()
    
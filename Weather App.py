# import necessary libraries
from bs4 import BeautifulSoup
import requests

# set headers for requests to prevent being blocked by Google
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# define function to retrieve weather information for a given city


def weather(city):
    # replace any spaces in the city name with '+', as required by Google search URL format
    city = city.replace(" ", "+")
    # perform a search on Google for the given city's weather information, using requests and the headers defined above
    res = requests.get(
        f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
    # print message indicating that a search is being performed
    print("Searching in google......\n")
    # create a BeautifulSoup object with the response text from the Google search
    soup = BeautifulSoup(res.text, 'html.parser')
    try:
        # extract location, time, weather condition, and temperature from the parsed HTML
        location = soup.select('#wob_loc')[0].getText().strip()
        time = soup.select('#wob_dts')[0].getText().strip()
        info = soup.select('#wob_dc')[0].getText().strip()
        weather = soup.select('#wob_tm')[0].getText().strip()
        # print the extracted information
        print(location)
        print(time)
        print(info)
        print(weather+"°C")
    except IndexError:
        print("Could not retrieve weather information for the specified city.")


# get user input for city name
print("Enter the city name:")
city = input()
# add "weather" to the end of the city name to search for weather information specifically
city = city + " weather"
# call the weather function with the specified city
weather(city)

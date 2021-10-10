import requests
import json

url = 'https://api.openweathermap.org/'     #seting endpoint url to a variable
api_key = '01825e3d313c9231507224f41e2ed4ea'   #setting api key to a variable
country_code = 'USA'        #setting country code to a variable
print('Welcome to Open Weather Map!')   #printing a welcome message to user


def connection_test():   #function to test connection to server using a try block
    response = requests.get(url)
    r = response.status_code
    try:
        print('You are connected!')
    except:
        print('Connection failed, please try again')


connection_test()  #calling the connection function to run


def cityWeather():  #created a function for searching by city
    city = input('Please type the name of the city:')
    state = input('Please enter the 2 digit state code i.e NE:')
    city_data = {'q': city, state + 'appid': api_key}
    response = requests.get(url, city_data)
    print(response.json())   #printing weather based on city inputed by user


def zipWeather(): #created a function for searching by zip code
    zip_code = input('Please enter your 5 digit zip code:')
    zip_data = {'zip':zip_code, 'aapid':api_key}
    response = requests.get(url,zip_data)
    print(response.json())   #printing weather based on zip code inputed by user


def search_type():   #function to prompt user to select what they would like to search by
    type = input('Would you like to search by City or Zip Code?:')
    if type == 'City' or 'city':
        cityWeather()
    elif type == 'Zip Code' or 'zip code':
        zipWeather()

search_type()    #calling function to prompt user for weather information

def reRun():  #function to prompt user if they would like to rerun program
    again = input('Would you like to check the weather for a different locations?')
    if again == 'Yes' or 'yes':
        search_type()
    elif again =='No' or 'no':
        print('Thank you for using Open Weather Maps! Please visit again soon.')

reRun()
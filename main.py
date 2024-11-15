from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook

#vars
prep_time_list = []
cook_time_list = []
additional_time_list = []
total_time_list = []
serving_size_list = []

#gets data like cook time and serving size
def get_initial_recipe_info(url):

    #get list of data
    initial_recipe_info = (url.find_all('div', class_="mm-recipes-details__value"))
    initial_recipe_labels = (url.find_all('div', class_="mm-recipes-details__label"))

    #prep time
    format_data(initial_recipe_info, prep_time_list, 0)

    #cook time
    format_data(initial_recipe_info, cook_time_list, 1)

    #additional time
    if initial_recipe_labels[2].text == 'Additional Time:':
        format_data(initial_recipe_info, additional_time_list, 2)

        #offset is one if the recipe has additional time data
        offset = 1  
    else:
        offset = 0
        additional_time_list.append(0)

    #total time
    format_data(initial_recipe_info, total_time_list, 2 + offset)

    #serving size
    serving_size_data = int(initial_recipe_info[3 + offset].text)
    serving_size_list.append(serving_size_data)

#formats data from hr 'hrs' min 'mins' to a single integer representing total numbers
def format_data(initial_recipe_info, total_data_list, index):
    data_list = initial_recipe_info[index].text.split()
    data = int(data_list[0])

    if 'hr' in data_list or 'hrs' in data_list:
        data *= 60
        if 'mins' in data_list:
            data += int(data_list[2])

    total_data_list.append(data)

#access home page
html_text = requests.get("https://www.allrecipes.com/search?Chicken=Chicken&offset=0&q=Chicken").text
soup = BeautifulSoup(html_text, 'lxml')
urls = soup.find_all('a', class_="mntl-card-list-card--extendable")

#loop through recipes and get data
for url in urls:
    url = BeautifulSoup(requests.get(url.get('href')).text, 'lxml')

    #initial recipe info
    get_initial_recipe_info(url)
    
print(prep_time_list)
print(cook_time_list)
print(additional_time_list)
print(total_time_list)
print(serving_size_list)
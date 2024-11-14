from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook

#vars
<<<<<<< HEAD
calorie_data_list = []
fats_data_list = []
carbs_data_list = []
protein_data_list = []

#Get individual recipe page
=======
prep_time_list = []
cook_time_list = []
total_time_list = []
serving_size_list = []

#access home page
>>>>>>> initial-recipe-info
html_text = requests.get("https://www.allrecipes.com/search?Chicken=Chicken&offset=0&q=Chicken").text
soup = BeautifulSoup(html_text, 'lxml')
urls = soup.find_all('a', class_="mntl-card-list-items")

for url in urls:
    url = BeautifulSoup(requests.get(url.get('href')).text, 'lxml')
<<<<<<< HEAD

    #nutrition info
    nutrition_data = url.find('div', id="mm-recipes-nutrition-facts_1-0").find_all('td')

    calories_data = int(nutrition_data[0].text)
    fat_data = int(nutrition_data[2].text.replace('g', ''))
    carbs_data = int(nutrition_data[4].text.replace('g', ''))
    protein_data = int(nutrition_data[6].text.replace('g', ''))

    calorie_data_list.append(calories_data)
    fats_data_list.append(fat_data)
    carbs_data_list.append(carbs_data)
    protein_data_list.append(protein_data)

# print(calorie_data_list)
# print(fats_data_list)
# print(carbs_data_list)
# print(protein_data_list)
=======
    initial_recipe_info = (url.find_all('div', class_="mm-recipes-details__value"))
    
    prep_time_data_list = initial_recipe_info[0].text.split()
    prep_time_data = int(prep_time_data_list[0])
    if 'hr' in prep_time_data_list or 'hrs' in prep_time_data_list:
        prep_time_data *= 60
        if 'mins' in prep_time_data_list:
            prep_time_data += int(prep_time_data_list[2])

    cook_time_data_list = initial_recipe_info[1].text.split()
    cook_time_data = int(cook_time_data_list[0])
    if 'hr' in cook_time_data_list or 'hrs' in cook_time_data_list:
        cook_time_data *= 60
        if 'mins' in cook_time_data_list:
            cook_time_data += int(cook_time_data_list[2])

    total_time_data_list = initial_recipe_info[2].text.split()
    total_time_data = int(total_time_data_list[0])
    if 'hr' in total_time_data_list or 'hrs' in total_time_data_list:
        total_time_data *= 60
        if 'mins' in total_time_data_list:
            total_time_data += int(total_time_data_list[2])
    
    serving_size_data = initial_recipe_info[3].text

    prep_time_list.append(prep_time_data)
    cook_time_list.append(cook_time_data)
    total_time_list.append(total_time_data)
    serving_size_list.append(serving_size_data)

print(prep_time_list)
print(cook_time_list)
print(total_time_list)
print(serving_size_list)
    
>>>>>>> initial-recipe-info

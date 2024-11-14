from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook

#vars
calorie_data_list = []
fats_data_list = []
carbs_data_list = []
protein_data_list = []

#Get individual recipe page
html_text = requests.get("https://www.allrecipes.com/search?Chicken=Chicken&offset=0&q=Chicken").text
soup = BeautifulSoup(html_text, 'lxml')
urls = soup.find_all('a', class_="mntl-card-list-card--extendable")

for url in urls:
    url = BeautifulSoup(requests.get(url.get('href')).text, 'lxml')

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


print(calorie_data_list)
print(fats_data_list)
print(carbs_data_list)
print(protein_data_list)
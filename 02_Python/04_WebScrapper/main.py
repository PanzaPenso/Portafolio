import requests
from bs4 import BeautifulSoup

listDates = []
listNames = []
listDescriptions = []

url = 'https://www.forumcph.dk/?lang=en'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
event_section = soup.find('div', class_='E6jjcn')

div_dates = event_section.find_all('div', class_='HcOXKn c9GqVL QxJLC3 comp-jy99ju1w wixui-rich-text')

for date in div_dates:
    #print(date.text)
    listDates.append(date)

div_names = event_section.find_all('div', class_='HcOXKn SxM0TO QxJLC3 comp-jyfw0jbd wixui-rich-text')

for name in div_names:
    #print(name.text)
    listNames.append(name)

div_descriptions = event_section.find_all('div', class_='HcOXKn SxM0TO QxJLC3 comp-jy99ju4r wixui-rich-text')

for description in div_descriptions:
    #print(description.text)
    listDescriptions.append(description)

for index in range(0, len(listDates)):
    print('***')
    print(f'Name of the Event: {listNames[index].text}')
    print(f'Date of the Event: {listDates[index].text}')
    print(f'Description of the Event: {listDescriptions[index].text}')
    print('***\n')
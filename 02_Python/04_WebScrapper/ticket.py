import requests

id = 'Z698xZC4Z17fy8y'
apiKey = 'vWHUHQA25KoN21W5nUtPGAfjiiKTgsUH'
url = 'https://app.ticketmaster.com/discovery/v2/events.json?countryCode=DK'
startDate = '2024-07-01T00:00:00Z'
endDate ='2024-07-31T23:00:00Z'

response = requests.get(f'{url}&startDateTime={startDate}&endDateTime={endDate}&apikey={apiKey}')
result_json = response.json()
events = result_json['_embedded']['events']

print('***')
print(f'For July we found {len(events)} events')
print('***\n')

for i in range(0,len(events)):
    print('***')
    print(f"The name of the event: {events[i]['name']}")
    print(f"The url of the event: {events[i]['url']}")
    #print(f"The Event is on the {events[i]['dates']['start']['localDate']} at {events[i]['dates']['start']['localTime']}")
    #print(f"With the Following prices: \n")
    #print(events[i]['priceRanges'])
    print('***\n')
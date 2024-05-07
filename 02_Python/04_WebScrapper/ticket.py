import requests
import psycopg2

# Connection DB
connection = psycopg2.connect(user="ub4rt6if1v93na",
                              password="pb133f7ff80309974fa8a76f92d4f2d4ecd9c8caf2ab4bb6d02c3307647bf1780",
                              host="c7lei8p1it7v6j.cluster-czz5s0kz4scl.eu-west-1.rds.amazonaws.com",
                              port="5432",
                              database="d9rd65tngv1n6u")

# API TicketMaster
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


#print(events[0]['images'][0]['url'])


for i in range(0,len(events)):
    print(f'*** Event Number {i}:')
    print(f"The name of the event: {events[i]['name']}")
    print(f"The url of the event: {events[i]['url']}")
    print(events[i]['dates'])
    print('***\n')

    if (events[i]['dates']['start']['dateTBD'] == False and events[i]['dates']['start']['dateTBA'] == False and events[i]['dates']['start']['timeTBA'] == False):
        #'INSERTAR TODOS LOS DATOS'
        with connection.cursor() as cur:
            cur.execute('INSERT INTO public.event_details (name, url, img, date, time) VALUES (%s, %s, %s, %s, %s)', (events[i]['name'], events[i]['url'], events[i]['images'][0]['url'], events[i]['dates']['start']['localDate'], events[i]['dates']['start']['localTime']))
            connection.commit()


    elif (events[i]['dates']['start']['dateTBD'] == False and events[i]['dates']['start']['dateTBA'] == False and events[i]['dates']['start']['timeTBA'] == True):
        #'INSERTAR TODOS LOS DATOS EXCEPTO LOS TIEMPOS'
        with connection.cursor() as cur:
            cur.execute('INSERT INTO public.event_details (name, url, img, date) VALUES (%s, %s, %s, %s)', (events[i]['name'], events[i]['url'], events[i]['images'][0]['url'] , events[i]['dates']['start']['localDate']))
            connection.commit()
    else :
        with connection.cursor() as cur:
            cur.execute('INSERT INTO public.event_details (name, url, img) VALUES (%s, %s, %s)', (events[i]['name'], events[i]['url'], events[i]['images'][0]['url']))
            connection.commit()



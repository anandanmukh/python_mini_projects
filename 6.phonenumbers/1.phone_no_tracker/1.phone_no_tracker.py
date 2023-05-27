import phonenumbers
import folium
number=input("Enter your phone number with country code: ")

from phonenumbers import geocoder

key='34d1f963b4a841dc96ad416a7b89e8e6'

sanNumber=phonenumbers.parse(number)
yourLocation=geocoder.description_for_number(sanNumber,"en")
print(yourLocation)

#name of service provider
from phonenumbers import carrier
service_provider=phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,"en"))

from opencage.geocoder import OpenCageGeocode
geocoder=OpenCageGeocode(key)
query=str(yourLocation)
results=geocoder.geocode(query)
#print(results)

lat=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']

print('latitude',lat,'   longitude',lng)

myMap=folium.Map(location=[lat,lng], zoom_start=9)

folium.Marker([lat,lng],popup=yourLocation).add_to(myMap)

#save map in html file

myMap.save("myLocation.html")






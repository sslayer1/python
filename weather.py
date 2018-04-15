#dowload pyown from Github and install using
# pip install pyowm
##import pyowm


###get api key from https://openweathermap.org/
##owm = pyowm.OWM(API_key = 'b8383ac7926986e39bd0936b8cd7bf98')
##
##
### Search for current weather in London (UK)
##observation = owm.weather_at_place('Brunei,BWN')
##w = observation.get_weather()
##
### Weather details
##detailed_status = w.get_detailed_status()
##wind = w.get_wind()                  
##humidity = w.get_humidity()          
##temperature = w.get_temperature('celsius')  
##sunrisetime = w.get_sunrise_time('iso')
##sunsettime = w.get_sunset_time('iso')
##
##print (w)
##print (detailed_status)
##print (wind)
##print (humidity)
##print (temperature)
##print (sunrisetime)
##print (sunsettime)                               
##
##tomorrow = pyowm.timeutils.tomorrow()
##print (tomorrow)
##
##

#dowload pyown from Github and install using
# pip install pyowm
import pyowm

      
class Weather():

    local_api = 'b8383ac7926986e39bd0936b8cd7bf98'
    myapikey = pyowm.OWM(local_api)
        
    def __init__(self, location, temperature = '', wind = ''):
        self.location = location
        self.temperature = temperature
        self.wind = wind
   
    def getweatheratplace (self, location):
        return self.myapikey.weather_at_place (location)
        
        
    def getweather (self):
        return get_weather()

    def gettemperature (self):
        return get_temperature ()
    
#Usage    
weather_brunei = Weather('Brunei')
print (weather_brunei)

weatherobsatlocation = weather_brunei.getweatheratplace ('Brunei')
print ("Obs at locale", weatherobsatlocation)

weatherdetails = weatherobsatlocation.get_weather ()
print ("Weather details = ", weatherdetails)

weather_brunei.temperature = weatherdetails.get_temperature ()
print ("Temperature ", weather_brunei.temperature)





import pyowm
a=input('Город?')
owm = pyowm.OWM('60f45d88e7552897e6188ffbcb1baac3')
observation = owm.weather_at_place(a)
w = observation.get_weather()
w.get_wind()                  
w.get_humidity()              
x=w.get_temperature('celsius')
print('Там ',x['temp'],' градусов')




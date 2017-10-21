import pyowm
a=input('City?')
owm = pyowm.OWM('60f45d88e7552897e6188ffbcb1baac3')
observation = owm.weather_at_place(a)
w = observation.get_weather()
x=w.get_temperature('celsius')
print('There is ',x['temp'],' degrees in the ','a')

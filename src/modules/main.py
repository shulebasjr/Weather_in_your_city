from pyowm import OWM              

owm = OWM('626fc1698f8a355b4e8ed609c24f22d5')
mgr = owm.weather_manager()

place = input("input your city?:")

observation = mgr.weather_at_place(place)
w = observation.weather

temp = w.temperature('celsius')['temp']

print("In " + place + " now " + w.detailed_status)
print("The temperature now is about " + str(temp))

if temp < 10:
    print('It is very cold outside, you would better put something warm on you')
elif temp < 20:
    print('It is pretty cold outside, put something on you')
else:
    print('The temperature is okay, you can put whatever you want on you')
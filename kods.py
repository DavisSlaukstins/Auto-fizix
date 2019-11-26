import smbus2
import bme280
import math

port = 1
address = 0x76
bus = smbus2.SMBus(port)

calibration_params = bme280.load_calibration_params(bus, address)

data = bme280.sample(bus, address, calibration_params)

#pieprasa vielas nosaukumu

while True:
    try:
        w = str (input ("Gādā gāzē atradas mērinstruments : "))
        break
    except ValueError:
        print("Tāda vērtība nestrādā")

#pieprasa tilpumu

while True:
    try:
        v = float (input ("Ievadi trauka/telpas tilpumu : "))
        break
    except ValueError:
        print("Tāda vērtība nestrādā")

#pieprasa vielas molmasu

while True:
    try:
        M = float (input ("Ievadi gāzes molmasu : "))
        break
    except ValueError:
        print("Tāda vērtība nestrādā")

# w = vielas nosaukums, v = tilpums, m = molmasa.
#tilpums *spiediens = masa/ mol masa * konstante *temperatura
#masa = (tilpums * spiediens / (konstante * temperatura)) / mol masa
#v2 = 3RT/M

#definēju lietas

r = 8.31
t = data.temperature
p = data.pressure
t = t+273
#veicu apreikinus

m1 = v*p
m2 = r*t
m3 = m1/m2
m = m3/M
v2 = 3*r*t/M
v = math.sqrt(v2)

#paradu nepieciesamo

print("")
print(w," masa ir ", m)
print("")
print(w," ātrums ir ", v)
print("")
#print(data.timestamp)
#print(data.temperature)
#print(data.pressure)
#print(data.humidity)

print(data)
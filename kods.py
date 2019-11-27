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
        v = float (input ("Ievadi trauka/telpas tilpumu m3: "))
        break
    except ValueError:
        print("Tāda vērtība nestrādā")

#pieprasa vielas molmasu

while True:
    try:
        M1 = float (input ("Ievadi gāzes molmasu g/mol: "))
        break
    except ValueError:
        print("Tāda vērtība nestrādā")

# w = vielas nosaukums, v = tilpums, m = molmasa.
#tilpums *spiediens = masa/ mol masa * konstante *temperatura
#masa = spiediens*tilpums*molmasa/r*t
#v2 = 3RT/M

#definēju lietas
M = M1/1000
r = 8.31
T = data.temperature
p1 = data.pressure
t = T+273
#veicu apreikinus
p = p1*100
m1 = v*p*M
m2 = r*t
m = m1/m2
v2 = 3*r*t/M
v = math.sqrt(v2)

#paradu nepieciesamo

print("")
print(w," masa ir ", m,"g")
print("")
print(w," ātrums ir ", v,"m/s")
print("")
#print(data.timestamp)
#print(data.temperature)
#print(data.pressure)
#print(data.humidity)

print(data)
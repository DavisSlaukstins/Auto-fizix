import RPi.GPIO as GPIO
import time
import random
import smbus2
import bme280
import math

port = 1
address = 0x76
bus = smbus2.SMBus(port)

calibration_params = bme280.load_calibration_params(bus, address)

data = bme280.sample(bus, address, calibration_params)

buzzer_pin = 27

#NOTIS
notes = {
	'B0' : 31,
	'C1' : 33, 'CS1' : 35,
	'D1' : 37, 'DS1' : 39,
	'EB1' : 39,
	'E1' : 41,
	'F1' : 44, 'FS1' : 46,
	'G1' : 49, 'GS1' : 52,
	'A1' : 55, 'AS1' : 58,
	'BB1' : 58,
	'B1' : 62,
	'C2' : 65, 'CS2' : 69,
	'D2' : 73, 'DS2' : 78,
	'EB2' : 78,
	'E2' : 82,
	'F2' : 87, 'FS2' : 93,
	'G2' : 98, 'GS2' : 104,
	'A2' : 110, 'AS2' : 117,
	'BB2' : 123,
	'B2' : 123,
	'C3' : 131, 'CS3' : 139,
	'D3' : 147, 'DS3' : 156,
	'EB3' : 156,
	'E3' : 165,
	'F3' : 175, 'FS3' : 185,
	'G3' : 196, 'GS3' : 208,
	'A3' : 220, 'AS3' : 233,
	'BB3' : 233,
	'B3' : 247,
	'C4' : 262, 'CS4' : 277,
	'D4' : 294, 'DS4' : 311,
	'EB4' : 311,
	'E4' : 330,
	'F4' : 349, 'FS4' : 370,
	'G4' : 392, 'GS4' : 415,
	'A4' : 440, 'AS4' : 466,
	'BB4' : 466,
	'B4' : 494,
	'C5' : 523, 'CS5' : 554,
	'D5' : 587, 'DS5' : 622,
	'EB5' : 622,
	'E5' : 659,
	'F5' : 698, 'FS5' : 740,
	'G5' : 784, 'GS5' : 831,
	'A5' : 880, 'AS5' : 932,
	'BB5' : 932,
	'B5' : 988,
	'C6' : 1047, 'CS6' : 1109,
	'D6' : 1175, 'DS6' : 1245,
	'EB6' : 1245,
	'E6' : 1319,
	'F6' : 1397, 'FS6' : 1480,
	'G6' : 1568, 'GS6' : 1661,
	'A6' : 1760, 'AS6' : 1865,
	'BB6' : 1865,
	'B6' : 1976,
	'C7' : 2093, 'CS7' : 2217,
	'D7' : 2349, 'DS7' : 2489,
	'EB7' : 2489,
	'E7' : 2637,
	'F7' : 2794, 'FS7' : 2960,
	'G7' : 3136, 'GS7' : 3322,
	'A7' : 3520, 'AS7' : 3729,
	'BB7' : 3729,
	'B7' : 3951,
	'C8' : 4186, 'CS8' : 4435,
	'D8' : 4699, 'DS8' : 4978
}



melody = [
  notes['E7'], notes['E7'], 0, notes['E7'],
  0, notes['C7'], notes['E7'], 0,
  notes['G7'], 0, 0,  0,
  notes['G6'], 0, 0, 0,
 
  notes['C7'], 0, 0, notes['G6'],
  0, 0, notes['E6'], 0,
  0, notes['A6'], 0, notes['B6'],
  0, notes['AS6'], notes['A6'], 0,
 
  notes['G6'], notes['E7'], notes['G7'],
  notes['A7'], 0, notes['F7'], notes['G7'],
  0, notes['E7'], 0, notes['C7'],
  notes['D7'], notes['B6'], 0, 0,
 
  notes['C7'], 0, 0, notes['G6'],
  0, 0, notes['E6'], 0,
  0, notes['A6'], 0, notes['B6'],
  0, notes['AS6'], notes['A6'], 0,
 
  notes['G6'], notes['E7'], notes['G7'],
  notes['A7'], 0, notes['F7'], notes['G7'],
  0, 0, notes['C7'], notes['E7'],
  notes['G7'], notes['A7'], notes['B7'], notes['C8']
]
tempo = [
  24, 24, 24, 24,
  24, 24, 24, 24,
  24, 24, 24, 24,
  24, 24, 24, 24,
 
  24, 24, 24, 24,
  24, 24, 24, 24,
  24, 24, 24, 24,
  24, 24, 24, 24,
 
  29, 29, 29,
  24, 24, 24, 24,
  24, 24, 24, 24,
  24, 24, 24, 24,
 
  24, 24, 24, 24,
  24, 24, 24, 24,
  24, 24, 24, 24,
  24, 24, 24, 24,
 
  29, 29, 29,
  24, 24, 24, 24,
  24, 4, 12, 12,
  12, 24, 24, 4,
]


def buzz(frequency, length):	 #create the function "buzz" and feed it the pitch and duration)

	if(frequency==0):
		time.sleep(length)
		return
	period = 1.0 / frequency 		 #in physics, the period (sec/cyc) is the inverse of the frequency (cyc/sec)
	delayValue = period / 2		 #calcuate the time for half of the wave
	numCycles = int(length * frequency)	 #the number of waves to produce is the duration times the frequency
	
	for i in range(numCycles):		#start a loop from 0 to the variable "cycles" calculated above
		GPIO.output(buzzer_pin, True)	 #set pin 27 to high
		time.sleep(delayValue)		#wait with pin 27 high
		GPIO.output(buzzer_pin, False)		#set pin 27 to low
		time.sleep(delayValue)		#wait with pin 27 low
	


def setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(buzzer_pin, GPIO.IN)
	GPIO.setup(buzzer_pin, GPIO.OUT)
	GPIO.setwarnings(False)
	
def destroy():
	GPIO.cleanup()				# Release resource
	

def play(melody,tempo,pause,pace=0.800):
	
	for i in range(0, len(melody)):		# Play song
		
		noteDuration = pace/tempo[i]
		buzz(melody[i],noteDuration)	# Change the frequency along the song note
		
		pauseBetweenNotes = noteDuration * pause
		time.sleep(pauseBetweenNotes)
	
	

if __name__ == '__main__':		# Program start from here
	try:
		setup()

		while True:
			try:
				w = str (input ("Gādā gāzē atradas mērinstruments : "))
				break
			except ValueError:
				print("Tāda vērtība nestrādā")
				GPIO.output(27,GPIO.HIGH)
				time.sleep(0.5)
				GPIO.output(27,GPIO.LOW)
				time.sleep(0.5)
				GPIO.output(27,GPIO.HIGH)
				time.sleep(0.5)
				GPIO.output(27,GPIO.LOW)
		GPIO.output(27,GPIO.HIGH)
		time.sleep(0.5)
		GPIO.output(27,GPIO.LOW)
#pieprasa tilpumu

		while True:
			try:
				v = float (input ("Ievadi trauka/telpas tilpumu m3: "))
				break
			except ValueError:
				print("Tāda vērtība nestrādā")
				GPIO.output(27,GPIO.HIGH)
				time.sleep(0.5)
				GPIO.output(27,GPIO.LOW)
				time.sleep(0.5)
				GPIO.output(27,GPIO.HIGH)
				time.sleep(0.5)
				GPIO.output(27,GPIO.LOW)
		GPIO.output(27,GPIO.HIGH)
		time.sleep(0.5)
		GPIO.output(27,GPIO.LOW)

#pieprasa vielas molmasu

		while True:
			try:
				M1 = float (input ("Ievadi gāzes molmasu g/mol: "))
				break
			except ValueError:
				print("Tāda vērtība nestrādā")
				GPIO.output(27,GPIO.HIGH)
				time.sleep(0.5)
				GPIO.output(27,GPIO.LOW)
				time.sleep(0.5)
				GPIO.output(27,GPIO.HIGH)
				time.sleep(0.5)
				GPIO.output(27,GPIO.LOW)
		GPIO.output(27,GPIO.HIGH)
		time.sleep(0.5)
		GPIO.output(27,GPIO.LOW)

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
		print("Veicu apreikinus")
		print("")
		play(melody, tempo, 0.3, 0.800)
		print("")
		print("Pabeidzu!")
		print("")
		print("")
		print(w," masa ir ", m,"kg")
		print("")
		print(w," ātrums ir ", v,"m/s")
		print("")
#print(data.timestamp)
#print(data.temperature)
#print(data.pressure)
#print(data.humidity)

		print(data)
		
		
		destroy()
	except KeyboardInterrupt:  	# When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()
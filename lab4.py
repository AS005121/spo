from gpio import *
from time import *


def main():
	sensor_pin = 0
	cold_pin = 3
	hot_pin = 4

	pinMode(sensor_pin, IN)
	pinMode(cold_pin, OUT)
	pinMode(hot_pin, OUT)

	while True:
		d_cel = float(analogRead(sensor_pin)) / 1023 * 200 - 100

		if d_cel > 25:
			digitalWrite(cold_pin, HIGH)
			digitalWrite(hot_pin, LOW)
		elif d_cel < 20:
			digitalWrite(cold_pin, LOW)
			digitalWrite(hot_pin, HIGH)


if __name__ == "__main__":
	main()

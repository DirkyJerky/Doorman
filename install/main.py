from doorman import doorman
import pins

try:
    pins.red_led.low()
    doorman()
except Exception as e:
    print(e)
    pins.red_led.high()
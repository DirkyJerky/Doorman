from machine import Pin

relay_vp = Pin(2, Pin.OUT)
relay_signal = Pin(3, Pin.OUT)

red_led = Pin(16, Pin.OUT)
yellow_led = Pin(17, Pin.OUT)
green_led = Pin(15, Pin.OUT)
# blue_led = Pin(14, Pin.OUT)

board_led = Pin("LED", Pin.OUT)
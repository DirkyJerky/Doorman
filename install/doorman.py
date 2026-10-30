from microdot import Microdot
import mm_wlan

from machine import Pin, Timer
import time

import pins

import auth

# led = Pin('LED', Pin.OUT)
def doorman():
    pins.relay_vp.high()

    lowTimer = Timer()
    heartbeatTimer = Timer()
    app = Microdot()

    mm_wlan.connect_to_network(auth.ssid, auth.password, retries=20)

    def low(t):
        pins.green_led.low()
        pins.relay_signal.low()
        print('CLOSE')

    def heartbeat(t):
        if not mm_wlan.is_connected():
            pins.red_led.high()
            try:
                mm_wlan.connect_to_network(auth.ssid, auth.password, retries=20)
                pins.red_led.low()
            except:
                pass
        pins.board_led.high()
        time.sleep(1)
        pins.board_led.low()

    @app.route('/unlock')
    async def index(request):
        pins.green_led.high()
        pins.relay_signal.high()
        print('OPEN')

        lowTimer.init(mode=Timer.ONE_SHOT, period=3000, callback=low)

        return 'Where did I put my keys?'

    print('Doorman online')
    heartbeat(None)
    heartbeatTimer.init(mode=Timer.PERIODIC, period=5000, callback=heartbeat)
    app.run(port=80)

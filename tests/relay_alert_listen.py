# Relay test: listen for real SafePing alerts that a Fob sends over LoRa.
# Each alert is printed as one line starting with SAFEPING_MSG, the same line the Fob
# prints on its own console, followed by who sent it and how strong the signal was.
# Run it from Thonny on the Relay board and leave it open. Ctrl+C stops it.

from machine import Pin, SPI  # type: ignore
import json
import time
import sx127x

spi = SPI(1, baudrate=1000000, polarity=0, phase=0,
          sck=Pin(10), mosi=Pin(8), miso=Pin(9))
cs = Pin(26, Pin.OUT, value=1)
reset = Pin(6, Pin.OUT, value=1)

radio = sx127x.SX127x(spi, cs, reset)
radio.begin()

got = 0
print("Listening for SafePing alerts. Press Ctrl+C to stop.")

try:
    while True:
        # Long window on purpose. Each time receive() times out it switches the radio
        # off for a moment, which would cut a packet that is still arriving.
        try:
            packet = radio.receive(timeout_ms=60000)
        except OSError as err:
            # The radio reset or stopped answering. Set it up again and keep listening.
            print("Relay radio problem:", err)
            print("Setting the Relay radio up again")
            time.sleep_ms(500)
            try:
                radio.begin()
                print("Relay radio OK again")
            except OSError as err2:
                print("Relay radio still not answering:", err2)
            continue
        if packet is None:
            continue
        data, rssi, snr = packet
        try:
            text = data.decode()
            msg = json.loads(text)
            if not isinstance(msg, dict) or "sig" not in msg:
                raise ValueError
        except (ValueError, UnicodeError):
            print("ignored a packet that is not a SafePing alert")
            continue
        got += 1
        print("SAFEPING_MSG " + text)
        print("  from", msg.get("id"), "type", msg.get("type"), "ctr", msg.get("ctr"),
              "signal", rssi, "dBm, snr", snr)
except KeyboardInterrupt:
    print("received", got, "alerts")
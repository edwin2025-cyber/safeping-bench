IO0 = GPIO 0, confirmed
IO1 = GPIO 1, confirmed
IO2 = GPIO 2, confirmed
IO3 = GPIO 3, confirmed
IO4 = GPIO 4, confirmed
IO5 = GPIO 5, confirmed

Lesson 4: Fob sends, Relay receives. Signal -15 to -52 dBm at about 1 to 2 m, 10 of 11 received.

Indoor, 30 cm: all received, battery works, signal -6 to -52 dBm.

Nov 6. Full Fob main.py now runs on the real board. Presses give STATUS, SUSPICIOUS, MEDICAL and SILENT, and a quick tap in the 2 second window cancels. With WiFi off, every alert goes out over LoRa and the Relay reads it. Fixed: WiFi state error, and the Relay was cutting packets because it listened in 1 second windows (now 60 seconds). GPS wing is wired in. Indoors it gets a fix but is 150 to 200 ft off, which is expected indoors. Not done yet: outdoor GPS check, motor circuit, WiFi and server, real secret key, NTP clock, battery reading.

## 2026-11-06 (night)

- Start checks passed. Fob main.py is the full program (21,663 bytes) on the board. Relay now runs relay_alert_listen.py as main.py.
- Added tests/field_log.py. Logs both boards to logs/ (raw, CSV, summary). Desk test: 4 of 4 received, 1 cancel sent nothing.
- Outdoor GPS (small area, practice run, not formal DT-10): fix on every press, acc 3 to 6 m, position stayed within about 1 to 3 m. Indoor was about 25 m.
- Outdoors every LoRa send timed out until I replugged the Fob. Lid test and wiggle test did not reproduce it. Cause not proven.
- Found a worse bug: after _radio.reset() the radio goes to mode 0x09 and lora_send() returns True, but the Relay hears nothing. False "sent".
- Fix written (sx127x check(), lora_send retry, Relay recovery). Applied to the repo. NOT on the boards yet, NOT tested on hardware.
- Battery is 420 mAh (label), not 500.
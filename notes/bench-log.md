IO0 = GPIO 0, confirmed
IO1 = GPIO 1, confirmed
IO2 = GPIO 2, confirmed
IO3 = GPIO 3, confirmed
IO4 = GPIO 4, confirmed
IO5 = GPIO 5, confirmed

Lesson 4: Fob sends, Relay receives. Signal -15 to -52 dBm at about 1 to 2 m, 10 of 11 received.

Indoor, 30 cm: all received, battery works, signal -6 to -52 dBm.

Nov 6. Full Fob main.py now runs on the real board. Presses give STATUS, SUSPICIOUS, MEDICAL and SILENT, and a quick tap in the 2 second window cancels. With WiFi off, every alert goes out over LoRa and the Relay reads it. Fixed: WiFi state error, and the Relay was cutting packets because it listened in 1 second windows (now 60 seconds). GPS wing is wired in. Indoors it gets a fix but is 150 to 200 ft off, which is expected indoors. Not done yet: outdoor GPS check, motor circuit, WiFi and server, real secret key, NTP clock, battery reading.
# supla-rpi-arduino-hcsr04
distance sensor in supla-dev


1. arduino gets distance using hc-sr04
2. sends the result to rpi using ttyACM0
3. supla-dev sends the result to supla-cloud

distance.ino - arduino application to gets distance, and present it using LED, 7seg display and buzzer

distance_reader.py - gets distance value from ttyACM0 and store it in /tmp/distance (/usr/bin/distance_reader.py)

supla-dev - implementation od distance sensor in supla  

#!/usr/bin/python

from __future__ import division
import subprocess 
import time


subprocess.Popen("cat /dev/ttyACM0 > /tmp/tty", shell=True, stdout=subprocess.PIPE)
time.sleep(7)
file = open("/tmp/tty", "r")
content = file.read()
last  = content[-5:]
trimmed = last.strip().replace("\r", " ").replace("\n", " ")
x = trimmed.find("\r")
if x > 0:
  distance = trimmed[x:]
else:
  distance = trimmed
cmd = ["echo", distance, ">", "/tmp/distance"]# % distance
subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

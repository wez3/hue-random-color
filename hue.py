#!/usr/bin/python

from phue import Bridge
import random

b = Bridge('') 
b.connect()
saturation=random.randint(200,255)                    # 0-255
hue=random.randint(1,65534)                           # 0-65535
brightness=random.randint(1,254)                      # 0-255
b.set_light(1, 'hue', hue)
b.set_light(1, 'sat', saturation)

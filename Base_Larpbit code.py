#basic script for LARP:bit. Works with microbit w/ 7 light neopixel strip or neoixel jewel 
from microbit import *
import neopixel, random 
led = neopixel.NeoPixel(pin0, 7)
bag = [ (0,255,0) , (255,0,0) , (255,0,0) , (255,0,0) , (0,0,255) , (0,0,255) , (0,0,255) , (0,0,255) , (255,255,255) , (255,255,255) ]

# function for shuffling the bag. Proabably better than the psudeo random picking (RIP L.t Gold)
def shuffle(list): 
  for i in range(0,len(list)):
    for i in range(0,10): 
      t1 = random.randint(0,len(list)-1)
      t2 = random.randint(0,len(list)-1)
      temp = list[t1] 
      list[t1] = list[t2]
      list[t2] = temp 
return list 

# function for pulling a bead from the bag
def bead_pull(bag):
    global led
    for i in range (0,7):
        led[i] = bag[0]
        led.show()
    sleep(4000)
    bag.remove(bag[0])
    for i in range (0,7):
        led[i] = (0,0,0)
        led.show()
       
shuffle(bag)
        
while True:
     if button_a.was_pressed():
         bead_pull(bag)
         
     if button_b.was_pressed():
        bag = [ (0,255,0) , (255,0,0) , (255,0,0) , (255,0,0) , (0,0,255) , (0,0,255) , (0,0,255) , (0,0,255) , (255,255,255) , (255,255,255) ]
        shuffle(bag)

    
    

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.set_rotation(270)

back_col1=(255,0,0)
back_col2=(0,0,255)
col1= (0,255,255) # set to desired color
col2 =(255,0,0)

# message to astronauts
sense.show_message("I hope you're doing great!",
                    scroll_speed=0.01,
                    text_colour=col1,back_colour=back_col1)
sense.show_message("My name should be Nikola Tesla",scroll_speed=0.01,
                    text_colour=col2,back_colour=back_col2) 

# image for astronauts
w = (255, 255, 255)
b = (0, 0, 0)
y = (255,255,0)

picture = [
   b, b, b, b, b, b, b, b,
   b, b, b, b, w, w, b, b,
   b, b, b, b, y, y, b, b,
   b, b, w, w, w, w, w, w,
   b, b, b, b, w, w, b, b,
   b, b, b, b, w, w, b, b,
   b, b, b, b, w, w, b, b,
   b, b, b, w, w ,w, w ,b  
 ]
sense.set_pixels(picture)
sleep(1)

#measure humidity
humid = round(sense.get_humidity(), 1)
sense.show_message( "It is " + str(humid) + " %" )
o=(255,130,0)
l=(0,0,255)
c=(0,150,255)
e=(80,80,80)
g=(0,255,0)
y=(255,255,0)
wet = [
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, o, b, o, o, o, b, b,
  b, o, o, o, o, e, o, b,
  b, o, o, o, o, o, o, b,
  b, o, b, o, o, o, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b
]


dry = [
  c, c, g, g, c, g, c, c,
  c, c, g, g, c, g, c, c,
  g, c, g, g, c, g, c, c,
  g, c, g, g, g, g, c, c,
  g, g, g, g, c, c, c, c,
  c, c, g, g, c, c, c, c,
  y, y, y, y, y, y, y, y,
  y, y, y, y, y, y, y, y
  ]

#display symbols for humidity
humid = sense.get_humidity()
if humid >= 40:
    sense.set_pixels(wet)
else:
    sense.set_pixels(dry)

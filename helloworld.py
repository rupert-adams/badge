import os
import time
from lib.waveshare_epd import epd2in13_V2
from PIL import Image, ImageDraw, ImageFont

pic_dir = 'pic' # Points to pic directory .

try:
    # Display init, clear
    display = epd2in13_V2.EPD()
    display.init(display.FULL_UPDATE)
    display.Clear(0xFF) # 0: Black, 255: White
    w = display.height
    h = display.width
    print('width:', w)
    print('height:', h)
    # Display text
    body = ImageFont.truetype(os.path.join(pic_dir, 'HKGrotesk-Bold.ttf'), size=26)
    body_sub = ImageFont.truetype(os.path.join(pic_dir, 'HKGrotesk-Bold.ttf'), size=16)
    image = Image.new(mode='1', size=(w,h), color=255)
    draw = ImageDraw.Draw(image)
    print("Drawing Text")
    draw.text((w/3, h/8), 'Rupert Adams',
          font=body, fill=0, align='left')
    display.display(display.getbuffer(image))
    draw.text((w/3, h/2), 'DevOps Engineer',
          font=body_sub, fill=0, align='left')
    display.display(display.getbuffer(image))
    # Show pattern image.
    time.sleep(3) # Pause for 3 seconds.
    print("drawing image")
    with Image.open('pic/pattern1.png') as pattern:
      pattern.thumbnail(size=(w,h), reducing_gap=3.0)
      image.paste(pattern, (0, 0))
    display.display(display.getbuffer(image)) # Update display
    time.sleep(10)
    display.Clear(0xFF)
except IOError as e:
    print(e)

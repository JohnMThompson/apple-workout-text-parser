import re
from PIL import Image
import pytesseract as pyt
from datetime import datetime


image = Image.open('img2.jpeg')
txt = pyt.image_to_string(image)

# Date & Start Time
date = datetime.today().strftime('%Y-%m-%d')
startTime = re.findall("(\d{2}[:]\d{2})[-]",txt)[0]
timestamp = date+' '+startTime+':00'

# Duration and Total Distance
duration = re.findall("(\d{1,2}[:]\d{2}[:]\d{2})\s.{3,6}YD",txt)[0]
totalDistance = re.findall("\d{1,2}[:]\d{2}[:]\d{2}\s(.{3,6})YD",txt)[0]

# Location
location = re.findall("[4]\s(\w*)",txt)[0]

# Strokes and Distance
breaststrokeDistance = re.findall("Breaststroke\s[(](.*)[y][d]",txt)[0]
freestyleDistance = re.findall("Freestyle\s[(](.*)[y][d]",txt)[0]

# Avg Heart Rate
avgHeartRate = re.findall("(\d{2,3})BPM",txt)[0]

print(timestamp, location)
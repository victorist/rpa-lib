import os
import cv2
import pytesseract
from PIL import Image

working_dir = "/Users/vistratov/dev_repos/rpa-lib/pdf_processing/"
f_name = "MANIFEST_v300.png"
path = os.path.join(working_dir, f_name)

if os.path.exists(path) is False:
    raise ValueError(f"Input file not found! {path}")

img_cv = cv2.imread(path)
print(pytesseract.image_to_string(img_cv))

# By default OpenCV stores images in BGR format and since pytesseract assumes RGB format,
# we need to convert from BGR to RGB format/mode:
img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(img_rgb))


# OR
img_rgb = Image.frombytes('RGB', img_cv.shape[:2], img_cv, 'raw', 'BGR', 0, 0)
print(pytesseract.image_to_string(img_rgb))


# List of available languages
print("_"*80)
"""
print(pytesseract.get_languages(config=''))
print("_"*80)



# Simple image to string
print(pytesseract.image_to_string(Image.open(file4ocr)))
print("_"*80)

# Get ALTO XML output
xml = pytesseract.image_to_alto_xml(file4ocr)
print("_"*80)
print("XML _______")
print(xml)
print("_"*80)
"""

# Get bounding box estimates
# print(pytesseract.image_to_boxes(Image.open(file4ocr)))
from PIL import Image, ImageDraw, ImageFont, ImageChops
import textwrap
from string import ascii_letters

origin_path = "C:\\Users\\arda.kutlu\\Pictures\\vehSkytrainRef_ldv_v001.jpg"
origin_img = Image.open(origin_path)

resolution = origin_img.size
bar_size = 100
margin = 10
font = ImageFont.truetype( "C:\\Windows\\Fonts\\Arial\\ariblk.ttf", 20)

overlay = Image.new('RGB', resolution, (128,128,128))
mask = ImageDraw.Draw(overlay)

mask.rectangle((0, bar_size, resolution[0], resolution[1]-bar_size), fill=(230, 230, 230), outline=None)

text1 = "Very very very verrrrryyyyyy long text testing situation"
avg_char_width = sum(font.getsize(char)[0] for char in ascii_letters) / len(ascii_letters)
max_char_count = int(resolution[0] * .333 / avg_char_width)
text1 = textwrap.fill(text=text1, width=max_char_count)

mask.text(xy=(10,10), text=text1, font=font, fill=(255,255,255), anchor='la')


text2 = "ne diyem mahmut mu diyem"
avg_char_width = sum(font.getsize(char)[0] for char in ascii_letters) / len(ascii_letters)
max_char_count = int(resolution[0] * .333 / avg_char_width)
text2 = textwrap.fill(text=text2, width=max_char_count)

mask.text(xy=(resolution[0]-10,10), text=text2, font=font, fill=(255,255,255), anchor='ra')



overlay.show()

# class Overlay(object):
#     def __init__(self):
#         super(Overlay, self).__init__()
#
#         self._barSize = 100
#         self._textMargin = 10
#         self._resolution = None
#         self._originPath = file
#
#     @property
#     def bar_size(self):
#         return self._barSize
#
#     @bar_size.setter
#     def bar_size(self, val):
#         self._barSize = val
#
#     @property
#     def text_margin(self):
#         return self._textMargin
#
#     @text_margin.setter
#     def text_margin(self, val):
#         self._textMargin = val
#
#     @property
#     def resolution(self):
#         return self._resolution or origin_img.size
#
#     @resolution.setter
#     def resolution(self, val):
#         self._resolution = val
#
#
#
#     def create_mask(self):
import sys

origin_path = "C:\\Users\\arda.kutlu\\Pictures\\vehSkytrainRef_ldv_v001.jpg"
output_path = "C:\\Users\\arda.kutlu\\Pictures\\vehSkytrainRef_ldv_v001_TEST.jpg"
font_path = "C:\\Windows\\Fonts\\Arial\\ariblk.ttf"

# from PIL import Image, ImageDraw
#
# with Image.open("C:\\Users\\arda.kutlu\\Pictures\\vehSkytrainRef_ldv_v001.jpg") as im:
#
#     draw = ImageDraw.Draw(im)
#     draw.line((0, 0) + im.size, fill=128)
#     draw.line((0, im.size[1], im.size[0], 0), fill=128)
#
#     # write to stdout
#     im.save("C:\\Users\\arda.kutlu\\Pictures\\vehSkytrainRef_ldv_v001_TEST.png")

######################################################
#
# from PIL import Image, ImageDraw, ImageFont
# # get an image
# with Image.open(origin_path).convert("RGBA") as base:
#
#     # make a blank image for the text, initialized to transparent text color
#     txt = Image.new("RGBA", base.size, (255,255,255,0))
#
#     # get a font
#     fnt = ImageFont.truetype(font_path, 40)
#     # get a drawing context
#     d = ImageDraw.Draw(txt)
#
#     # draw text, half opacity
#     d.text((10,10), "Hello", font=fnt, fill=(255,255,255,128))
#     # draw text, full opacity
#     d.text((10,60), "World", font=fnt, fill=(255,255,255,255))
#
#     out = Image.alpha_composite(base, txt)
#
#     out.show()


##########################################################

# from PIL import Image, ImageDraw, ImageFont
# for x in range(50):
#     resolution = [1920, 1080]
#
#     bar_length = 100
#     bar_color = (0, 0, 0, 128)
#     text_color = (255, 255, 255, 128)
#
#     # create an image
#     out = Image.new("RGB", (resolution[0], bar_length), bar_color)
#
#     # get a font
#     fnt = ImageFont.truetype(font_path, 40)
#     # get a drawing context
#     d = ImageDraw.Draw(out)
#
#     # draw multiline text
#     d.multiline_text((10,10), "Hello World", font=fnt, fill=text_color)
#
#     # out.show()
#     out.save("C:\\Users\\arda.kutlu\\Pictures\\vehSkytrainRef_ldv_v001_TEST.%s.png" %(str(x).zfill(4)))
#     print(x)

from PIL import Image, ImageDraw, ImageFont, ImageChops

resolution = [1920, 1080]

bar_length = 100
bar_color = (128, 128, 128, 128)
text_color = (255, 255, 255, 128)

# create an image
out = Image.new("RGB", (resolution[0], bar_length), bar_color)

# get a font
fnt = ImageFont.truetype(font_path, 40)
# get a drawing context
d = ImageDraw.Draw(out)

# draw multiline text
d.multiline_text((10,10), "Hello World", font=fnt, fill=text_color)

# out.show()

background = Image.open(origin_path)


im3 = ImageChops.composite(background, out)
im3.show()
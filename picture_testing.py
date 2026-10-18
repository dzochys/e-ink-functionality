from PIL import Image, ImageDraw, ImageFont

image = Image.new('1', (800, 480), 255)

draw = ImageDraw.Draw(image)

# text
font = ImageFont.truetype(r"C:\Users\jachs\AppData\Local\Microsoft\Windows\Fonts\Futura Bold Italic font.ttf", 11)
draw.text(
    xy = (50, 80),
    text = 'Toto je testovací program vykreslování na e-Paper displej.',
    font = font,
    fill = 0
    )


draw.rectangle((0, 200, 300, 240), fill = 0)
draw.line((0, 245, 300, 245), fill = 0)


image.save(r"obrazek.jpg", "JPEG")
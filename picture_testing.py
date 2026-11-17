from PIL import Image, ImageDraw, ImageFont

black_image = Image.new('1', (800, 480), 255)
red_image = Image.new('1', (800, 400), 255)

# Drawing the black image
draw_black = ImageDraw.Draw(black_image)

# text
font = ImageFont.truetype(r"C:\Users\jachs\AppData\Local\Microsoft\Windows\Fonts\Futura Bold Italic font.ttf", 11)
draw_black.text(
    xy = (50, 80),
    text = 'Toto je testovací program vykreslování na e-Paper displej.',
    font = font,
    fill = 0
    )


draw_black.rectangle((0, 200, 300, 240), fill = 0)
draw_black.line((0, 245, 300, 245), fill = 0)


black_image.save("black_picture.jpg", "JPEG") # Saving the black image

# Drawing the red image
draw_red = ImageDraw.Draw(red_image)

draw_red.rectangle((350, 150, 360, 160), fill = 0)

red_image.save("red_picture.jpg", "JPEG") # Saving the red image
from PIL import Image, ImageDraw, ImageFont

def add_watermark(image_path, watermark_text, output_path):
    base_image = Image.open(image_path)
    watermark = Image.new('RGBA', base_image.size, (0, 0, 0, 0))

    size = 2
    n_font = ImageFont.truetype('arial.ttf', size)
    n_width, n_height = n_font.getsize(watermark_text)
    while n_width+n_height < watermark.size[0]:
        size += 2
        n_font = ImageFont.truetype('arial.ttf', size)
        n_width, n_height = n_font.getsize(watermark_text)
    draw = ImageDraw.Draw(watermark, 'RGBA')
    draw.text(((watermark.size[0] - n_width) / 2,
               (watermark.size[1] - n_height) / 2),
              watermark_text, font=n_font, fill="#ffffff")

    watermarked = Image.alpha_composite(base_image.convert('RGBA'), watermark)
    watermarked.save(output_path, 'JPEG')

add_watermark('wallpaper.jpg', 'Your Watermark', 'output.jpg')
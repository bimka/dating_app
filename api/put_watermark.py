from PIL import Image

def watermark_avatar(input_avatar_path):
    """Add watermark on the avatar"""
    watermark_image_path = 'static/images/watermark.png'
    base_image = Image.open(input_avatar_path)
    watermark = Image.open(watermark_image_path)
    base_image.paste(watermark, (0,0), mask=watermark)
    #base_image.save(output_avatar_path)
    return base_image
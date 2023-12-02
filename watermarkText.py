from PIL import Image, ImageDraw, ImageFont


def add_watermark(input_image_path, output_image_path, watermark_text):
    # Open the input image
    original_image = Image.open(input_image_path)
    # Create a drawing object
    draw = ImageDraw.Draw(original_image)
    # Load a font
    font = ImageFont.truetype("arial.ttf", 55)
    # Specify the position and text of the watermark
    #watermark_position = (10, 10)
    #trying to move it to another side of the screen
    #watermark_position = (x, y)    
    watermark_position = (900, 10)

    watermark_color = (255, 255, 255)  # White color
    # Add the watermark to the image
    draw.text(watermark_position, watermark_text, font=font, fill=watermark_color)
    # Save the image with the watermark
    original_image.save(output_image_path)
    original_image.show()


if __name__ == "__main__":
    # Replace these paths with your actual file paths
    input_image_path = "fall_michigan.png"
    output_image_path = "output_image_with_watermark.png"
    watermark_text = "CIS 451/515"
    add_watermark(input_image_path, output_image_path, watermark_text)

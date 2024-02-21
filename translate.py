# ck
import yaml
from google.cloud import vision
from google.cloud import translate_v2 as translate
from PIL import Image, ImageDraw, ImageFont
import os

def load_config(config_file):
    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)
    return config

# Func to translate text
def translate_text(text, target_language='en'):
    translation = client_translate.translate(text, target_language=target_language)
    return translation['translatedText']

# OCR and Translation on an image
def translate_image(image_path, output_dir, target_language='en'):
    # Load the image
    with open(image_path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)

    # OCR text detection
    response = client_vision.text_detection(image=image)
    texts = response.text_annotations

    if texts:
        original_text = [annotation.description for annotation in texts]
        translated_text = [translate_text(text, target_language=target_language) for text in original_text]

        # Overlay translated text on the image
        img = Image.open(image_path)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("Ubuntu-R.ttf", size=font_size)

        # Replace original text with translated text
        for i in range(1, len(texts)):
            text = translated_text[i]
            bounds = [(vertex.x, vertex.y) for vertex in texts[i].bounding_poly.vertices]
            
            bbox = draw.textbbox(bounds[0], text, font=font)
            draw.rectangle(bbox, fill=text_background)

            draw.text(bounds[0], text, fill=text_color, font=font)

        # Save the translated image
        output_path = os.path.join(output_dir, os.path.basename(image_path))
        img.save(output_path)
        print(f"Translated image saved: {output_path}")
    else:
        print(f"No text detected in {image_path}")



config = load_config("config.yaml")

# Google Cloud credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = config["google_credentials"]

# Initialize the Google Cloud clients
client_vision = vision.ImageAnnotatorClient()
client_translate = translate.Client()

input_dir = config["input_folder"]
output_dir = config["output_folder"]
target_language = config["target_language"]
font_size = config["font_size"]
text_background = config["text_background"]
text_color = config["text_color"]

# Translate images in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(".png") or filename.endswith(".jpeg") or filename.endswith(".jpg"):
        image_path = os.path.join(input_dir, filename)
        translate_image(image_path, output_dir, target_language=target_language)

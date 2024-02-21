# translate-images-in-bulk-gc-vision
Translates images in bulk on the google cloud vision

It allows you to translate texts on your multiple images at once.

## How
Create Google Cloud account and enable Cloud Vision API and Translate API on your application.
![Screenshot from 2024-02-21 20-42-03](https://github.com/cankurttekin/translate-images-in-bulk-gc-vision/assets/29798399/88922d65-def3-4f88-b0b0-562aa1e0d5f3)

Create key and download credentials file.

## Configuration
Edit config.yaml to point your credentials file and desired translation language and some other configs.
```
google_credentials: "./credentials.json"
font_size: 19
text_background: "red"
text_color: "black"
input_folder: "./images"
output_folder: "./output"
target_language: "tr"
```
## Example 
![image](https://github.com/cankurttekin/translate-images-in-bulk-gc-vision/blob/main/images/Screenshot%20from%202024-02-21%2018-58-39.png)

![image](https://github.com/cankurttekin/translate-images-in-bulk-gc-vision/blob/main/output/Screenshot%20from%202024-02-21%2018-58-39.png)

## Todo
1. improve translation 
2. improve overlays & readability

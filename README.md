A simple Python script that processes image files by converting them to grayscale, rotating them, resizing them, and saving them in JPEG format.
- Converts all images to grayscale
- Rotates each image 90 degrees clockwise
- Resizes images to 128x128 pixels
- Saves processed images as `.jpeg` in the `~/upd_images` directory

- **Input folder**: `~/images`  
  Place your source images here. Supports most common image formats.
- **Output folder**: `~/upd_images`  
  Processed images will be saved here in `.jpeg` format.

## How to Use

1. Make sure you have Python 3 installed.
2. Install the required Python library. Pillow (Python Imaging Library):

```bash
pip install pillow
```

3. Create the images directory in your home folder and add your image files:

```bash
mkdir ~/images
```

4. Run the script:

```bash
chmod +x edit_image.py
./edit_image.py
```

Or run it with Python:

```bash
python3 edit_image.py
```

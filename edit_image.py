#!/usr/bin/env python3

from pathlib import Path           # For handling filesystem paths
from PIL import Image              # For image processing

# Create the output directory for processed images if it doesn't exist
upd_images_dir = Path.home() / 'upd_images'
upd_images_dir.mkdir(exist_ok=True)

# Define the input directory where original images are located
old_image_dir = Path.home() / 'images'

# Define supported image file formats. Add '' if old file doesn't have extension.
supported_formats = (
    '.png', '.jpg', '.jpeg', '.bmp',
    '.gif', '.tiff', '.webp'
)

# Iterate through all files in the input directory
for image in old_image_dir.iterdir():
    # Check if it's a file, not hidden, and has a supported image extension
    if image.is_file() and not image.name.startswith('.') and image.suffix.lower() in supported_formats:
        try:
            # Open the image file
            with Image.open(image) as im:
                # Convert the image to grayscale for successful .jpeg convertion
                # Rotate it 90 degrees clockwise (by rotating -90 degrees counterclockwise)
                # Resize it to 128x128 pixels
                processed = im.convert('L').rotate(-90).resize((128, 128))

                # Create a new filename with .jpeg extension
                new_name = image.stem + '.jpeg'

                # Build the full path for the output file
                output_path = upd_images_dir / new_name

                # Save the processed image in JPEG format
                processed.save(output_path, format='JPEG')

        # Handle any image processing errors (e.g., corrupted files)
        except Exception as e:
            print(f'Failed to process {image.name}: {e}')

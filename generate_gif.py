import os
from PIL import Image

# Define the image formats to be included
image_formats = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp')

# Get list of image files in the root directory
image_files = [f for f in os.listdir('.') if f.lower().endswith(image_formats)]

# Check if there are any image files
if not image_files:
    print("No image files found in the root directory.")
else:
    # Sort image files by filename
    image_files.sort()

    # Load images
    images = [Image.open(f) for f in image_files]

    # Save as GIF
    images[0].save(
        'Signage.gif',
        save_all=True,
        append_images=images[1:],
        duration=500,
        loop=0
    )

    print("Signage.gif has been generated successfully.")

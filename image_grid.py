from PIL import Image
import math
import os

def split_image_for_instagram(image_name='bg.png'):
    """
    Splits an image into multiple parts for Instagram posting.

    Args:
        image_name (str): The name of the image file to split. Defaults to 'bg.png'.

    Returns:
        None

    Raises:
        IOError: If there is an error in processing the image.

    """
    if not os.path.exists(image_name):
        print(f"Image '{image_name}' not found in the current directory.")
        return

    try:
        img = Image.open(image_name)
        img_width, img_height = img.size

        # Calculate square size for 3 columns
        square_size = img_width // 3  # Integer division to get whole number
        num_columns = 3
        num_rows = math.ceil(img_height / square_size)

        # Splitting and numbering the image for Instagram posting
        count = 1
        for row in range(num_rows):
            for col in range(num_columns):
                left = col * square_size
                top = row * square_size
                right = left + square_size
                bottom = top + square_size

                # Check if bottom exceeds image height
                if bottom > img_height:
                    bottom = img_height

                # Check if there is an image section to crop
                if right > left and bottom > top:
                    split_img = img.crop((left, top, right, bottom))
                    split_img.save(f'instagram_post_{count}.png', 'PNG')
                    count += 1

        print(f"Image successfully split into {count - 1} parts.")
    except IOError:
        print("Error in processing the image. Please check the image path and try again.")

if __name__ == "__main__":
    split_image_for_instagram()

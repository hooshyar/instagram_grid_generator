# Instagram Image Splitter

## This readme is automated, I didn't even read it

## Overview
This Python script, `split_image_for_instagram.py`, is designed to split any given image into multiple square parts for aesthetically pleasing Instagram posting. It creates a grid of images that, when uploaded in sequence, will display as one large, cohesive image on your Instagram profile.

## Features
- Splits an image into a 3xN grid (3 columns, N rows).
- Adjusts the number of rows based on the image size.
- Saves each section of the grid as a separate file for easy posting.

## Requirements
- Python 3.x
- Pillow Library

## Installation
Before running the script, ensure you have Python installed on your system and install the Pillow library using pip:
```
pip install Pillow
```

## Usage
1. Place the `split_image_for_instagram.py` script in the same directory as the image you want to split.
2. If your image is named differently than `bg.png`, you'll need to specify the image name when calling the function.
3. Run the script:
   ```
   python split_image_for_instagram.py
   ```
4. The script will generate multiple images named `instagram_post_1.png`, `instagram_post_2.png`, etc., in the same directory.

## Example
To split an image named `my_photo.png`, edit the `main` function call at the bottom of the script like this:
```python
if __name__ == "__main__":
    split_image_for_instagram('my_photo.png')
```
Then run the script.

## Troubleshooting
If you encounter any issues, ensure that:
- The image file is in the same directory as the script.
- The image file name is correctly spelled in the script.
- You have the necessary permissions to read the image file and write new files in the directory.

## Contributing
Contributions to this script are welcome. Please feel free to fork the repository, make your changes, and submit a pull request.

## License
This script is released under the [MIT License](https://opensource.org/licenses/MIT).

---

This `README.md` file should provide a clear understanding of what the script does, how to set it up, and how to use it. Adjust as necessary to fit the specific context or additional features of your script.
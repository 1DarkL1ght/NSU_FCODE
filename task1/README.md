# Task 1
## Overview
This module demonstared usage of color transforms by using HSV color space:
1. Loads example image
2. Converts to HSV
3. Changes S (saturation) channel to lower and higher value
4. Converts back to BGR
5. Visualize results
## Execution
1. Create python venv `python -m venv venv`
2. Activate venv. Win: `venv/Scripts/activate`. Linux: `source venv/bin/activate`
3. Install requirements `pip install -r task1/requirements.txt`
4. Run `python task1/main.py --image_path <example.png>`. `--image path` is optional. If not specified default skimage.astronaut() will be used
5. To quit press `q`
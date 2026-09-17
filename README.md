# Real-Time Edge Detection using OpenCV

## Project Overview

This project is a Computer Vision application developed using Python and OpenCV. It detects edges in an image using the Canny Edge Detection algorithm. The user can adjust the detection thresholds in real time using sliders and save the output image.

## Features

- Detects edges using the Canny algorithm
- Interactive threshold adjustment
- Displays original and processed images
- Saves the output image
- Runs completely from the command line

## Project Structure

edge-detection-cv/
│── images/
│   └── sample.jpg
│── output/
│── src/
│   └── edge_detector.py
│── requirements.txt
│── README.md

## Requirements

- Python 3.10 or above
- OpenCV
- NumPy

## Installation

Open a terminal inside the project folder and install dependencies:

```bash
pip install -r requirements.txt
```

## How to Run

Run the following command:

```bash
python src/edge_detector.py
```

## Controls

- Move the sliders to change edge detection sensitivity.
- Press **S** to save the output image.
- Press **ESC** to exit.

## Output

The processed image is saved in:

output/edge_output.png

## Technologies Used

- Python
- OpenCV
- NumPy
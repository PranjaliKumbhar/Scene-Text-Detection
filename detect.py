import argparse

import matplotlib.pyplot as plt

from lib.text_detection import TextDetection
from lib.utils import plt_show
from lib.config import Config

## Arguments
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", type=str, required=True, help="Path to the input image")

args = vars(parser.parse_args())
IMAGE_FILE = args["input"]


if __name__ == "__main__":
    config = Config()
    td = TextDetection(IMAGE_FILE, config, direction='both+',details=True)
    res = td.detect()
    plt_show((td.img, "Original"), (td.final, "Final"), (res, "Mask"))
       
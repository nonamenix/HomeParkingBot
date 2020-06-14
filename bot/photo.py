import time
from datetime import datetime
from os.path import join
from typing import Tuple

import cv2

FONT = cv2.FONT_HERSHEY_SIMPLEX


def make_photo(path="/tmp/photos") -> Tuple[str, str]:
    camera_port = 0
    camera = cv2.VideoCapture(camera_port)
    time.sleep(0.2)  # let the camera wake up
    now = datetime.now()
    return_value, image = camera.read()

    # datetime text
    org = (15, 460)
    text = now.strftime("%Y.%m.%d %H:%M:%S")
    image = cv2.putText(
        image,
        text,
        org,
        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
        fontScale=0.5,
        color=(255, 255, 255),
        thickness=1,
        lineType=cv2.LINE_AA,
    )
    filename = "{filename}.jpg".format(filename=now.strftime("%Y%m%d_%H%M%S"))
    filepath = join(path, filename)
    cv2.imwrite(filepath, image)

    return filepath, text


if __name__ == "__main__":
    make_photo()

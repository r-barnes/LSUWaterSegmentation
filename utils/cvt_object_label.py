import numpy as np
import cv2

def cvt_object_label(img, ori_label_color, dst_label_color=None):

    if dst_label_color is None:
        dst_label_color = ori_label_color

    height, width, channels = img.shape
    blue_mask = np.ones([height, width, 1], dtype=np.uint8) * ori_label_color[0]
    green_mask = np.ones([height, width, 1], dtype=np.uint8) * ori_label_color[1]
    red_mask = np.ones([height, width, 1], dtype=np.uint8) * ori_label_color[2]
    color_mask = cv2.merge((blue_mask, green_mask, red_mask))

    # Set label_color to 0
    img = cv2.bitwise_xor(img, color_mask)

    # Set label_color to 255
    img = cv2.bitwise_not(img)

    # Set other pixel to 0
    mask = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)

    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(mask, np.array(dst_label_color))

    return img
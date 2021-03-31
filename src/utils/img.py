import cv2

def img_get_piece(img, x, y, cell_size=50, size=16):
    u = cell_size
    crop = img[y*u:y*u+u, x*u:x*u+u]
    return cv2.resize(crop, (size, size))

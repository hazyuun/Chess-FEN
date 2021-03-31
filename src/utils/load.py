
import os
import cv2
import numpy as np

from utils.fen import *


def get_filenames(dir, n):
    out = []
    for dir, _, files in os.walk(dir):
        for f in files:
            if(not n):
                return out
            n -= 1
            out.append((f.split('.')[0], os.path.join(dir, f)))
    return out


def load_train_test_datasets(dir_path, N, cell_size=50, FEN_delim='-', downscaled_size=32):
    FENs, paths, = tuple(zip(*get_filenames(dir_path, N)))
    X, Y = [], []
    u = cell_size
    for i in range(N):
        img = cv2.imread(paths[i], cv2.IMREAD_GRAYSCALE)
        for x in range(8):
            for y in range(8):
                crop = img[y*u:y*u+u, x*u: x*u+u]
                X.append(cv2.resize(crop, (downscaled_size, downscaled_size)))
                Y.append(FEN_get_piece(x, y, FENs[i], FEN_delim))
    middle = (N * 64 * 80) // 100

    train_x, train_y, test_x, test_y = np.array(X[:middle]), np.array(
        Y[:middle]), np.array(X[middle:]), np.array(Y[middle:])
    train_x = train_x.reshape(train_x.shape[0], downscaled_size**2)
    test_x = test_x.reshape(test_x.shape[0], downscaled_size**2)
    return train_x, train_y, test_x, test_y

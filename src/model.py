from sklearn import svm
from sklearn import metrics

from joblib import load, dump

from utils.img import *
from utils.fen import *

import matplotlib.pyplot as plt

def make_model(train_x, train_y, test_x, test_y):
    svc = svm.SVC(gamma=0.0000001, C=500)
    svc.fit(train_x, train_y)
    return svc, svc.score(test_x, test_y)


def plot_confusion(model, test_x, test_y):
    fig, ax = plt.subplots(figsize=(12, 12))
    metrics.plot_confusion_matrix(model, test_x, test_y, ax=ax)


def predict(model, image, delim='/'):
    board = []
    for i in range(8):
        for j in range(8):
            piece = img_get_piece(image, j, i)
            piece = piece.reshape(1, 16*16)
            p = model.predict(piece)
            board.append(str(p[0]))
    board = np.array(board)
    return FEN_from_board(board.reshape(8, 8), delim)


def export_model(model, path):
    dump(model, path)


def load_model(path):
    return load(path)

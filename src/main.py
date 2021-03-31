import argparse

from utils.data import *
from utils.load import *
from utils.fen import *
from utils.img import *

from model import *

MODEL_FILE = "CHESS_FEN.model"


def handle_args():
    parser = argparse.ArgumentParser(
        description='Predicts FEN given a chess board image')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--predict', help='The input image file')
    group.add_argument('--train', help='Path to a floder of training images')
    return vars(parser.parse_args())


def m_train(args):
    data_path = args["train"]
    train_x, train_y, test_x, test_y = load_train_test_datasets(
        data_path, 2000, downscaled_size=16)
    train_x, train_y = data_balance2(train_x, train_y)
    test_x, test_y = data_balance2(test_x, test_y)
    model, score = make_model(train_x, train_y, test_x, test_y)
    export_model(model, MODEL_FILE)


def m_predict(args):
    input_image_path = args["predict"]
    model = load_model(MODEL_FILE)
    img = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)
    print(predict(model, img, delim='/'))


def main():
    args = handle_args()
    if args["train"] != None:
        m_train(args)
    elif args["predict"] != None:
        m_predict(args)

if __name__ == "__main__":
    main()

import numpy as np
import pickle
from skimage.feature import hog
from skimage.io import imread
from skimage.transform import resize

def get_res(val):
    if val==0:
        return "Safe Driving"
    elif val==1:
        return "Texting - Right"
    elif val==2:
        return "Talking on the phone - Right"
    elif val==3:
        return "Texting - Left"
    elif val==4:
        return "Talking on the phone - Left"
    elif val==5:
        return "Operating the Radio"
    elif val==6:
        return "Drinking"
    elif val==7:
        return "Reaching Behind"
    elif val==8:
        return "Hair and Makeup"
    elif val==9:
        return "Talking to Passenger"


def get_hog(images, name='hog', save=False):
    result = np.array([hog(img, block_norm='L2',orientations=9, pixels_per_cell=(8, 8), cells_per_block=(3, 3)) for img in images])
    return result


def detect(path):
    Xv=[]
    img = imread(path)
    new_img = resize(img, (64, 128))
    Xv.append(new_img)
    Xv=np.array(Xv)

    hog_input = get_hog(Xv, name='hog_train', save=True)

    pca_reload = pickle.load(open("pca_dump.pkl",'rb'))
    norm_reload = pickle.load(open("norm_dump.pkl",'rb'))
    model = pickle.load(open("knn_pca_dump.pkl",'rb'))

    norm_hog_input = norm_reload.transform(hog_input)
    pca_norm_hog_train = pca_reload.transform(norm_hog_input)
    driver_pred = model.predict(pca_norm_hog_train)

    res = get_res(driver_pred[0])
    return res
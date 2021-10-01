import glob
import os
import numpy as np

current_dir_path = os.getcwd()

so2sat_data_all = os.path.join(current_dir_path, 'so2sat_pop_sample_data')  # path to So2Sat POP data folder
so2sat_data_train = os.path.join(so2sat_data_all, 'train')   # path to train folder
so2sat_data_test = os.path.join(so2sat_data_all, 'test')  # path to test folder


def get_fnames_labels(folder_path, data):
    """
    :param folder_path: path to so2sat sub folder test/train
    :param data: name of the data folder, ex: 'dem', 'lu', ...
    :return: give the paths of all the tifs and its corresponding class labels for given data
    """
    city_folders = glob.glob(os.path.join(folder_path, "*"))  # list all the cities in folder_path
    f_names_all = np.array([])
    labels_all = np.array([])
    for each_city in city_folders:
        data_folder = os.path.join(each_city, data)  # list the specified data folders for each city city
        class_folders = glob.glob(os.path.join(data_folder, "*"))  # list all the class folders of the data folder
        for folder in class_folders:
            f_names = np.array([x for x in glob.glob(os.path.join(folder, "*.tif"))])  # list all the tif files
            labels = np.full(len(f_names), os.path.basename(folder))  # list all the folder names
            f_names_all = np.append(f_names_all, f_names, axis=0)
            labels_all = np.append(labels_all, labels, axis=0)
    return f_names_all, labels_all


# get all the files and their corresponding for "dem" data in "train" folder
f_names_dem, labels_dem = get_fnames_labels(so2sat_data_train, data='dem')

# get all the files and their corresponding for "lcz" data in "test" folder
f_names_lcz, labels_lcz = get_fnames_labels(so2sat_data_test, data='lcz')

print('Finished')


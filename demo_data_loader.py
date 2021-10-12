"""
Generic data reader.
Returns path to all the patches of a given data and
its corresponding class labels and population counts.

Note: Reads from so2sat_pop_sample_data folder
"""

import glob
import os

import numpy as np
import pandas as pd

current_dir_path = os.getcwd()

so2sat_data_all = os.path.join(current_dir_path, 'so2sat_pop_sample_data')  # path to So2Sat POP data folder
so2sat_data_train = os.path.join(so2sat_data_all, 'train')   # path to train folder
so2sat_data_test = os.path.join(so2sat_data_all, 'test')  # path to test folder


def get_fnames_labels(folder_path, data):
    """
    :param folder_path: path to so2sat sub folder test/train
    :param data: name of the data folder, ex: 'dem', 'lu', ...
    :return: the paths of all the tifs and its corresponding pop count and class labels for given data
    """
    city_folders = glob.glob(os.path.join(folder_path, "*"))  # list all the cities in folder_path
    f_names_all = np.array([])  # file names
    c_labels_all = np.array([])  # class labels
    p_count_all = np.array([])  # population counts
    for each_city in city_folders:
        data_path = os.path.join(each_city, data)  # path to the specifies data folder
        csv_path = os.path.join(each_city, each_city.split(os.sep)[-1:][0] + '.csv')  # path to the cvs file of the city
        city_df = pd.read_csv(csv_path)  # read csv as dataframe
        ids = city_df['GRD_ID']  # get the id of each patch
        pop = city_df['POP']  # corresponding pop count
        classes = city_df['Class']  # corresponding Class
        classes_str = [str(x) for x in classes]
        classes_paths = [data_path + '/Class_' + x + '/' for x in classes_str]
        for index in range(0, len(classes_paths)):
            f_names = [classes_paths[index] + ids[index] + '_' + data + '.tif']  # creating full path for each id
            f_names_all = np.append(f_names_all, f_names, axis=0)  # append file names together
            pop_count = [pop[index]]
            p_count_all = np.append(p_count_all, pop_count, axis=0)   # append pop count together
            class_label = [classes[index]]
            c_labels_all = np.append(c_labels_all, class_label, axis=0)  # append class labels together

    return f_names_all, p_count_all, c_labels_all


if __name__ == "__main__":

    # get all the files and their corresponding for "dem" data in "train" folder
    f_names_dem, p_count_train, c_labels_train = get_fnames_labels(so2sat_data_train, data='dem')

    # get all the files and their corresponding for "sen2_rgb_autumn" data in "train" folder
    f_names_sen2_rgb_autumn,  p_count_train, c_labels_train = get_fnames_labels(so2sat_data_train, data='sen2_rgb_autumn')

    # get all the files and their corresponding for "lcz" data in "test" folder
    f_names_lcz,  p_count_test, c_labels_test = get_fnames_labels(so2sat_data_test, data='lcz')

    print('Finished')

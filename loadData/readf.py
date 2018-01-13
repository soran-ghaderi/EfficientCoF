import pandas as pd

from loadData.helpers import helper as hl

class LoadData:
    def readf(self, path):
        """
        Import data from the csv file and drop ir-related columns.
        :param path: Path to the csv file
        :return: Sorted-test-set/Sorted-train-set dictionaries
        """
        dataframe = pd.read_csv(path, '\t')
        dataframe.drop('timestamp', axis=1, inplace=True)
        print(dataframe['rating'].describe())
        # hl.MyPlotter.plot(dataframe)
        sorted_test_set, sorted_trainSet = hl.Split.split(dataframe)
        return sorted_trainSet, sorted_test_set

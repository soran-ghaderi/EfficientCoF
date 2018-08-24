import pandas as pd

from loadData.helpers import helper as hl


class LoadData:
    def readf(path):
        '''

        :param path: Read the specified file from path
        :return: Train and test set
        '''
        df = pd.read_csv(path, '\t')
        df.drop('timestamp', axis=1, inplace=True)
        print(df['rating'].describe())
        # hl.MyPlotter.plot(df)
        sorted_testSet, sorted_trainSet = hl.Split.split(df)
        return sorted_trainSet, sorted_testSet


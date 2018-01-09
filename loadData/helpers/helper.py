from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

class Split:
    def split(self, df):
        """

        :param df:
        :return:
        """
        trainingSet, testSet = train_test_split(df, test_size=0.2)
        sorted_trainSet = trainingSet.sort_values('user_id')
        sorted_testSet = testSet.sort_values('user_id')
        return sorted_testSet, sorted_trainSet
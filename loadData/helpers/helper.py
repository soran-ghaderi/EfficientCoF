from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

class Split:
    def split(self, df):
        """
        Split and sort train/test sets
        :param df: Dataframe containing training data
        :return: Sorted-test-set/Sorted-train-set dictionaries
        """
        trainingSet, testSet = train_test_split(df, test_size=0.2)
        sorted_trainSet = trainingSet.sort_values('user_id')
        sorted_testSet = testSet.sort_values('user_id')
        return sorted_testSet, sorted_trainSet

class MyPlotter:
    def plot(self, df):
        """
        Plot dataframe distributions:
            1. Distribution of ratings
            2. Distribution of ratings count per user
        :return:
        """
        df['item_id'].hist(grid=True)
        plt.xlabel('Items')
        plt.ylabel('Frequency')
        plt.title('Distribution of ratings')
        plt.show()
        plt.xlabel('Number of ratings per user')
        plt.ylabel('Frequency')
        plt.title('Distribution of ratings count per user')
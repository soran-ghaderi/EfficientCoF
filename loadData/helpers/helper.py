from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


class Split:
    def split(self, dataframe):
        """
        Split and sort train/test sets
        :param dataframe: Dataframe containing training data
        :return: Sorted-test-set/Sorted-train-set dictionaries
        """
        training_set, test_set = train_test_split(dataframe, test_size=0.2)
        sorted_train_set = training_set.sort_values('user_id')
        sorted_test_set = test_set.sort_values('user_id')
        return sorted_test_set, sorted_train_set


class MyPlotter:
    def plot(self, dataframe):
        """
        Plot dataframe distributions:
            1. Distribution of ratings
            2. Distribution of ratings count per user
        :return:
        """
        dataframe['item_id'].hist(grid=True)
        plt.xlabel('Items')
        plt.ylabel('Frequency')
        plt.title('Distribution of ratings')
        plt.show()
        plt.xlabel('Number of ratings per user')
        plt.ylabel('Frequency')
        plt.title('Distribution of ratings count per user')

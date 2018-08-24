from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

class Split:


    def split(df):
        '''

        :param df: Dataframe to be splited
        :return: Sorted list of dataframe's splited list
        '''
        trainingSet, testSet = train_test_split(df, test_size=0.2)
        sorted_trainSet = trainingSet.sort_values('user_id')
        sorted_testSet = testSet.sort_values('user_id')
        return sorted_testSet, sorted_trainSet

class MyPlotter:

    def plot(df):
        '''

        :param df: Datafram to be ploted
        :return: Plots the dataframes different distributions
        '''
        df['item_id'].hist(grid=True)
        plt.xlabel('Items')
        plt.ylabel('Frequency')
        plt.title('Distribution of ratings')
        plt.show()

        # df = pd.DataFrame(R).replace('0', np.nan).count(axis=1)  # count number of ratings per user
        binwidth = 10
        # df.hist(bins=np.arange(min(df), max(df) + binwidth, binwidth))
        plt.xlabel('Number of ratings per user')
        plt.ylabel('Frequency')
        plt.title('Distribution of ratings count per user')
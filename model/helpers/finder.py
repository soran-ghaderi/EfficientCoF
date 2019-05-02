import pandas as pd
from model.helpers import helper as mhl



class Finder:

    def find_commons_in_one_list(user, mlist, interestinga):
        '''

        :param user: Neighbour user to find common items with current user's subspace
        :param list: Current user's subspace
        :return: The number of common items found with current user's subspace
        '''
        count = 0
        try:
            for j in range(interestinga[user].__len__()):
                if interestinga[user][j] in mlist:
                    count += 1
        except:
            print('passed')
        return count

    def find_nearest_neighbours(user, reducedlist, listOfUsers):
        '''

        Finding nearest neighbours in descending order
            Input:  :param user: Current user to find its neighbours
                    :param reducedlist: The unique and redundancy removed subspaces of items
                    :param listOfUsers: The list of rated items by userers: interesting, NIU, uninteresting

            Output: :return a dataframe of nearest neighbours in descending order

        '''
        nearestuserers = []
        dicOfsortedNearests = {}
        listIndex = mhl.neighbors.find_subspace(user, reducedlist, listOfUsers)
        subspacelist = reducedlist[listIndex]
        maximum = 0
        nearuserer = 0
        for i in (listOfUsers):
            if not i == user:
                # print('i',i)
                niegbourmax = Finder.find_commons_in_one_list(i, subspacelist, listOfUsers)
                dicOfsortedNearests.update({i: niegbourmax})
                dtf = pd.DataFrame(list(dicOfsortedNearests.items()), columns=['user', 'num'])
                so = dtf.sort_values('num', ascending=False)
                if niegbourmax > maximum:
                    maximum = niegbourmax
                    nearuserer = i
        print(nearuserer, max, subspacelist)
        # print(so)
        for row in range(so.__len__()):
            # if row.loc[1]== max:
            if so.iloc[row]['num'] == maximum:
                # print(so.ilocrow)
                nearestuserers.append(so.iloc[row]['user'])

        return nearestuserers


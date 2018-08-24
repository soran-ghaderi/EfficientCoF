from model.helpers import helper as mhl


class ReducedListGenerator:
    def generate_reduced(list_to_be_reduced):
        '''

        :param list_to_be_reduced: Every subspace of each global table that was created in the previous step may be a
        subset of a greater subspace, so this willlead to great redundancy. Therefore,the redundancy should be removed.
        :return: Reduced subspace returned
        '''
        reducedlist = []
        listOfWords = []
        listoflists = []
        toberemoved = []
        commondic = {}
        words = list_to_be_reduced.keys()
        # print(print('kk',set.intersection(*(set(list_to_be_reduced[word]) for word in words))))
        for w in words:
            listOfWords.append(w)
        for i in range(listOfWords.__len__()):
            if 1 + 1 < listOfWords.__len__():
                for j in range(i + 1, listOfWords.__len__()):
                    # print(list_to_be_reduced[l[i]],interesting[l[j]])
                    commondic.update(
                        {i: mhl.neighbors.common_elements(list_to_be_reduced[listOfWords[i]],
                                                          list_to_be_reduced[listOfWords[j]])})
        # print(commondic)
        for k in commondic:
            listoflists.append(commondic[k])
        # print('list of lists length', listoflists.__len__())
        for i in range(listoflists.__len__()):
            if i + 1 < listoflists.__len__():
                for j in range(i + 1, listoflists.__len__()):
                    if len(listoflists[i]) < len(listoflists[j]):
                        # print(listoflists[i],listoflists[j],set(listoflists[i]).issubset(listoflists[j]))
                        if set(listoflists[i]).issubset(listoflists[j]):
                            if not toberemoved.__contains__(i):
                                toberemoved.append(i)
                                # print(i)
                    else:
                        # print(listoflists[i],listoflists[j],set(listoflists[j]).issubset(listoflists[i]))
                        if set(listoflists[j]).issubset(listoflists[i]):
                            if not toberemoved.__contains__(j):
                                toberemoved.append(j)
                                # print(j)

        ''' Extract main collection of items'''
        for i in range(listoflists.__len__()):
            if not i in toberemoved:
                reducedlist.append(listoflists[i])
        return reducedlist


from model.helpers import finder as fd

class neighbors:
    def common_elements(list1, list2):
        """
        Args:
            list2:
        """
        result = []
        for element in list1:
            if element in list2:
        """
        Args:
            mlist:
            interestinga:

        Returns:
            The number of common items found with current user's subspace
        """
            reducedlist: Reduced list of specified subspace lists( Interesting,
                NIU, Uninteresting)
            interestingr: Specified list encompassing rating values

        Returns:
            Related subspace to each user will be returned
        """
        subspace_dict = {}
        maximum = 0
        listIndex = 0
        for s in range(reducedlist.__len__()):
            count = 0
            for j in range(interestingr[user].__len__()):
                if interestingr[user][j] in reducedlist[s]:
                    count += 1
                    # print(item,s,count)

            if count > maximum:
                maximum = count
                listIndex = s

        subspace_dict.update({user: {}})
        subspace_dict[user].update({listIndex: maximum})

        return listIndex

    def level_1and2_neighbours(user, reducedlist, mlist):
        """
        Args:
            reducedlist: cluserters of interesting, NIU, uninteresting lists
            mlist:

        Returns:
            level 1 and level 2 neighbours as a dictionary
        """
        level1and2N = {}
        nearest_neighbours = fd.Finder.find_nearest_neighbours(user, reducedlist, mlist)
        level1and2N.update({1: nearest_neighbours})
        for nearest in nearest_neighbours:
            if not fd.Finder.find_nearest_neighbours(nearest, reducedlist, mlist) in level1and2N[1]:
                if level1and2N.keys().__contains__(2):
                    level1and2N[2].update({nearest: fd.Finder.find_nearest_neighbours(nearest, reducedlist, mlist)})
                else:
                    level1and2N.update({2: {nearest: fd.Finder.find_nearest_neighbours(nearest, reducedlist, mlist)}})
        # print('Neibours:', level1and2N)
        # print('reduced list', reducedlist)
        # print('list', list)
        return level1and2N

    def extract_neighbours(neighbours_list):
        """
        Returns:
            Splited level 1 and level 2 neighbors
        """
        list_of_indirect = []
        list_of_direct = neighbours_list[1]
        for miter in list_of_direct:
            try:
                for sec in neighbours_list[2][miter]:
                    if not ((sec in list_of_direct) or (sec in list_of_indirect)):
                        list_of_indirect.append(sec)
            except:
                print('passed')
        return list_of_direct, list_of_indirect


class Constructor:
    def construct_train_lists(msorted):
        """Objective: Calculating and figuring out cluserters based on " A new method to find neighbor interesting that
            improves the performance of Collaborative Filtering" paper.

        Steps done in this function:
            Extracting ratings and devide them into three categories:
                1. Interesting
                2. NIU (Neither Interesting nor Unintresting)
                3. Uninteresting

            Calculating cluserters items have in common and remove redundant
            lists which are subset of others
        """

        interesting = {}
        NIU = {}
        uninteresting = {}
        total = {}
        interesting_with_rating = {}
        NIU_with_rating = {}
        uninteresting_with_rating = {}
        total_with_rating = {}

        for row in msorted.T.iteritems():
            if (row[1][2]) > 3:
                # print(row)
                if interesting.get(row[1][0], 'n') == 'n':
                    interesting.update({row[1][0]: []})
                    interesting[row[1][0]].append(row[1][1])
                    # ///////////////////////////////////////////////////////////////
                    interesting_with_rating.update({row[1][0]: {}})
                    interesting_with_rating[row[1][0]].update({row[1][1]: row[1][2]})
                else:
                    interesting[row[1][0]].append(row[1][1])
                    # //////////////////////////////////////////////////////////////
                    interesting_with_rating[row[1][0]].update({row[1][1]: row[1][2]})


            elif (row[1][2]) == 3:
                # print(row)
                if NIU.get(row[1][0], 'n') == 'n':
                    NIU.update({row[1][0]: []})
                    NIU[row[1][0]].append(row[1][1])
                    # /////////////////////////////////////////////////////////////
                    NIU_with_rating.update({row[1][0]: {}})
                    NIU_with_rating[row[1][0]].update({row[1][1]: row[1][2]})
                else:
                    NIU[row[1][0]].append(row[1][1])
                    # /////////////////////////////////////////////////////////////
                    NIU_with_rating[row[1][0]].update({row[1][1]: row[1][2]})

            elif (row[1][2]) < 3:
                # print(row)
                if uninteresting.get(row[1][0], 'n') == 'n':
                    uninteresting.update({row[1][0]: []})
                    uninteresting[row[1][0]].append(row[1][1])
                    # ///////////////////////////////////////////////////////////////
                    uninteresting_with_rating.update({row[1][0]: {}})
                    uninteresting_with_rating[row[1][0]].update({row[1][1]: row[1][2]})
                else:
                    uninteresting[row[1][0]].append(row[1][1])
                    # ////////////////////////////////////////////////////////////////
                    uninteresting_with_rating[row[1][0]].update({row[1][1]: row[1][2]})

                    ######################################################################################################33
            if total.get(row[1][0], 'n') == 'n':
                total.update({row[1][0]: []})
                total[row[1][0]].append(row[1][1])
                # ///////////////////////////////////////////////////////////////
                total_with_rating.update({row[1][0]: {}})
                total_with_rating[row[1][0]].update({row[1][1]: row[1][2]})
            else:
                total[row[1][0]].append(row[1][1])
                # //////////////////////////////////////////////////////////////
                total_with_rating[row[1][0]].update({row[1][1]: row[1][2]})

        print(interesting)
        print(NIU)
        print(uninteresting)

        return interesting, interesting_with_rating, NIU, NIU_with_rating, uninteresting, uninteresting_with_rating, total, total_with_rating

    def construct_test_list(msorted):
        """
        Returns:
            Dictionary of all (user-item)s related to test data
        """
        total = {}
        total_with_rating = {}
        for row in msorted.T.iteritems():
            if total.get(row[1][0], 'n') == 'n':
                total.update({row[1][0]: []})
                total[row[1][0]].append(row[1][1])
                # ///////////////////////////////////////////////////////////////
                total_with_rating.update({row[1][0]: {}})
                total_with_rating[row[1][0]].update({row[1][1]: row[1][2]})
            else:
                total[row[1][0]].append(row[1][1])
                # //////////////////////////////////////////////////////////////
                total_with_rating[row[1][0]].update({row[1][1]: row[1][2]})

        return total, total_with_rating


class MyMath:
    def mean_calc(targetUser, rating_list):
        """
        Args:
            rating_list: List of rated items of target user

        Returns:
            Arithmetic mean of the rating_list
        """
        msum = 0
        for item in rating_list[targetUser]:
            # print('interesting',item, rating_list[targetUser][item])
            msum += rating_list[targetUser][item]
        # print('mean:',float(msum/(rating_list[targetUser].__len__())))
        return float(msum / (rating_list[targetUser].__len__()))

from model.similarity import similarity_metrics as sm
from model.helpers import helper as mhl
from model.prediction import prediction as prd


class Predict:
    def predict_new_items(targetU, neighbour, indirNeighbour, item, mlist, list_with_R):
        """
        Args:
            neighbour: Direct neighbors of target user
            indirNeighbour: Indirect neighbors of target user
            item: Target item to calculate its probability to recommend to the
                target user
            mlist:
            list_with_R: Total dictionary of user-item matrix including rating
                values

        Returns:
            Items which have 4 or more score to be recommended
        """
        sig1 = 0
        sig2 = 0
        for i in neighbour:
            try:
                # print('prediction: rate and mean:', list_with_R[i][item], mhl.MyMath.mean_calc(i, list_with_R))
                # print('similarity:', pearson_sim(targetU, i, list, list_with_R))
                sig1 += (sm.Metrics.pearson_sim(targetU, i, mlist, list_with_R)) * (
                list_with_R[i][item] - mhl.MyMath.mean_calc(i, list_with_R))
            except:
                pass

            sig2 += sm.Metrics.pearson_sim(targetU, i, mlist, list_with_R)

        for j in indirNeighbour:
            try:
                sig1 += (sm.Metrics.new_sim(targetU, j, mlist, list_with_R)) * (
                list_with_R[j][item] - mhl.MyMath.mean_calc(i, list_with_R))
            except:
                pass
            sig2 += sm.Metrics.new_sim(targetU, j, mlist, list_with_R)

        if not sig2 == 0:
            result = (mhl.MyMath.mean_calc(targetU, list_with_R)) + (sig1 / sig2)
            if result > 5:
                result = 5
            return result
        else:
            return 0

    def prediction(trainSet, sublist_reduced_list, sublist, total, total_with_rating):
        """This method aims to predict a list of items for each user encompassed
        in the train set data considering theirsubspaces.

        than 4 have been calculated for

        Args:
            sublist_reduced_list: Reduced list of subspaces (Interesting, NUI,
                Unintersting)
            sublist: Subspace lists (Interesting, NUI, Uninteresting)
            total: Total list of train set User-Item matrix
            total_with_rating: Total list of train set User-Item matrix
                including rates between 1 and 5

        Returns:
            The predicted dictionary for userers. Each user has a list of
            predicted items which more
        """
        predicted_dictionary = {}
        listOfTestUsers = []
        for user in trainSet.T.iteritems():
            if not user[1][0] in listOfTestUsers:
                print('user number:', user[1][0])
                listOfTestUsers.append(user[1][0])
                y_pred = []
                try:
                    intlevel1and2N = mhl.neighbors.level_1and2_neighbours(user[1][0], sublist_reduced_list, sublist)
                    # NIUlevel1and2N = level_1and2_neighbours(user + 1, NIU_reduced_list, NIU)
                    # unintlevel1and2N = level_1and2_neighbours(user + 1, uninteresting_reduced_list, uninteresting)
                    # print(level1and2N)
                    dirN, indirN = mhl.neighbors.extract_neighbours(intlevel1and2N)
                    print("\n\n\npredictings ...")
                    listIndex = mhl.neighbors.find_subspace(user[1][0], sublist_reduced_list, sublist)
                    subspacelist = sublist_reduced_list[listIndex]
                    print('subspace list', subspacelist)
                    for it1 in subspacelist:
                        pred = prd.Predict.predict_new_items(user[1][0], dirN, indirN, it1, total, total_with_rating)
                        if pred >= 4:
                            y_pred.append(it1)
                            print('item number', it1, pred)
                    y_true = total[user[1][0]]
                    print(y_true)
                    print("predictions finished.\n\n\n")
                    print('|' * 80)
                except:
                    print('passed')

            predicted_dictionary.update({user[1][0]: y_pred})

        return predicted_dictionary

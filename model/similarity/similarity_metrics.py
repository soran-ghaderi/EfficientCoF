from math import sqrt
from model.helpers import helper as mhl


class Metrics:
    def pearson_sim(TUser, NUser, mlist, list_with_rating):
        '''

        :param TUser: Target user
        :param NUser: Direct neighbors of target user
        :param list: Total list of user-item edges
        :param list_with_rating: Total dictionary of user-item matrix including rating values
        :return: Pearson similarity of target user and its neighbor user
        '''
        currentusererlist = mlist[TUser]
        neighbourusererlist = mlist[NUser]
        common_list = []
        commons_count = 0
        s1 = 0
        s2 = 0
        s3 = 0
        if currentusererlist.__len__() < neighbourusererlist.__len__():
            for j in currentusererlist:
                if j in neighbourusererlist:
                    common_list.append(j)
                    commons_count += 1
        else:
            for j in neighbourusererlist:
                if j in currentusererlist:
                    common_list.append(j)
                    commons_count += 1
        ##############
        if not common_list.__len__() == 0:
            mean_target = mhl.MyMath.mean_calc(TUser, list_with_rating)
            mean1i = mhl.MyMath.mean_calc(NUser, list_with_rating)
            for k in common_list:
                s1 += (list_with_rating[TUser][k] - mean_target) * (list_with_rating[NUser][k] - mean1i)
                s2 += (list_with_rating[TUser][k] - mean_target) ** 2
                s3 += (list_with_rating[NUser][k] - mean1i) ** 2
            s2 = sqrt(s2)
            s3 = sqrt(s3)
            # print('direct')
            # print('similarity of:', TUser, NUser)
            # print("is\t\t|", s1 / (s2 * s3), '|')
            return s1 / (s2 * s3)
        else:
            return 0
            # try:
            #     pass
            # except:
            #     print('divided by zero', s2, s3)
            #     return 0

    def new_sim(TUser, NUser, mlist, list_with_rating):
        '''

        :param TUser: Target user
        :param NUser: Direct neighbors of target user
        :param list: Total list of user-item edges
        :param list_with_rating: Total dictionary of user-item matrix including rating values
        :return: Proposed similarity of this paper between target user and its neighbor user
        '''
        try:
            currentusererlist = mlist[TUser]
            neighbourusererlist = mlist[NUser]
            common_list = []
            commons_count = 0
            if currentusererlist.__len__() < neighbourusererlist.__len__():
                for j in currentusererlist:
                    if j in neighbourusererlist:
                        common_list.append(j)
                        commons_count += 1
            else:
                for j in neighbourusererlist:
                    if j in currentusererlist:
                        common_list.append(j)
                        commons_count += 1
            ##################
            # mean_target = mhl.MyMath.mean_calc(TUser, list_with_rating)
            # mean1i = mhl.MyMath.mean_calc(NUser, list_with_rating)
            ##################
            alpha = 1
            beta = 2
            n1 = 0
            n2 = 0
            l_ij = alpha * common_list.__len__() / (set(currentusererlist).union(set(neighbourusererlist))).__len__()
            ss = 0
            for k2 in common_list:
                ss += (list_with_rating[TUser][k2] - list_with_rating[NUser][k2]) ** 2
            # print('lengths',common_list.__len__(),ss)
            w_ij = 1 - (ss / beta * common_list.__len__())
            # print('w ij', w_ij)
            for ix in common_list:
                n1 += (w_ij * l_ij)
                n2 += w_ij
            # print('indirect')
            # print('similarity of:', TUser, NUser)
            # print("is\t\t|", n1 / n2, '|')
            result = n1 / n2
            if result > 5 or result < 0:
                Metrics.pearson_sim(TUser, NUser, mlist, list_with_rating)
            else:
                return result
        except:
            try:
                return Metrics.pearson_sim(TUser, NUser, mlist, list_with_rating)
            except:
                print('divided by zero', n2)
                return 0

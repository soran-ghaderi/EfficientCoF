
class Evaluate:
    def evaluate_prediction(predicted_dictionary, total_test):
        '''

        :param predicted_dictionary: Dictionary of predicted items for all users
        :param total_test: Total list of test data of users
        :return: Recall, preceision, f1_measure of the presented model
        Precision and recall are then defined as:
            Precision:  TP / TP + FP
            Recall:     TP / TP + FN
            F1_measure: (precision * recall) / (precision + recall)
                    or  (2*TP) / 2*TP + FP + FN
        '''
        tp = 0
        fp = 0
        fn = 0
        for user in predicted_dictionary:
            print(predicted_dictionary[user])
            if user in total_test:
                print(total_test[user])
                for item in predicted_dictionary[user]:

                    if item in total_test[user]:
                        tp += 1
                    else:
                        fp += 1
                fn += float(
                    set(total_test[user]).__len__() - (set(total_test[user]) & set(predicted_dictionary[user])).__len__())
        try:
            recall = tp / tp + fn
            precision = tp / tp + fp
            f1_measure = (precision * recall) / (precision + recall)
            return recall, precision, f1_measure
        except:
            return 0, 0, 0

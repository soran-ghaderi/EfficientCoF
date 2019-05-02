from datetime import datetime
from testModel import evaluate as ev
from loadData import readf as rf
from model.generators import reduced_subspace_generator as gn
from model.helpers import helper as mhl
from model.prediction import prediction as prd
from math import sqrt
from sklearn.metrics import accuracy_score, recall_score, 

def main():
    path = './dataset/u.data'
    trainSet, testSet = rf.LoadData.readf(path)
    print(trainSet.head())
    print(testSet.head())

    interesting, interesting_with_rating, NIU, NIU_with_rating \
        , uninteresting, uninteresting_with_rating, total, total_with_rating = mhl.Constructor.construct_train_lists(
        trainSet)
    total_test, total_test_with_rating = mhl.Constructor.construct_test_list(testSet)
    print('generating interesting reduced list...')
    interesting_reduced_list = gn.ReducedListGenerator.generate_reduced(interesting)
    print('interesting reduced list generated.')
    print('generating NIU reduced list...')
    NIU_reduced_list = generate_reduced(NIU)
    print('NIU reduced list generated.')
    print('generating uninteresting reduced list...')
    uninteresting_reduced_list = generate_reduced(uninteresting)
    print('uninteresting reduced list generated.')
    print('interesting reduced list')
    print(interesting_reduced_list)
    int_predicted_dictionary = prd.Predict.prediction(trainSet, interesting_reduced_list, interesting, total,
                                                      total_with_rating)
    intrecall, intprecision, intf1_measure = ev.Evaluate.evaluate_prediction(int_predicted_dictionary, total_test)
    NIU_predicted_dictionary = prd.Predict.prediction(trainSet, interesting_reduced_list, interesting, total, total_with_rating)
    NIUrecall, NIUprecision, NIUf1_measure = ev.Evaluate.evaluate_prediction(NIU_predicted_dictionary, total_test)
    unint_predicted_dictionary = prd.Predict.prediction(trainSet, interesting_reduced_list, interesting, total, total_with_rating)
    unintrecall, unintprecision, unintf1_measure = ev.Evaluate.evaluate_prediction(unint_predicted_dictionary, total_test)

    print('recall', intrecall)
    print('precision', intprecision)
    print('f1_measure', intf1_measure)

if __name__ == '__main__':
    start_time = datetime.now()
    main()
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))

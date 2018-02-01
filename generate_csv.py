import os, sys
import csv
import random # for testing purposes.
import itertools

# submission.csv must be deleted after each run.
# if submission.csv is not deleted, subsequent runs will append new entries to
# last run's results.

def gen_into_CSV(patch_name, pred):

    if not os.path.isfile('submission.csv'):
        csv_file = open('submission.csv', 'w')

    else:
        csv_file = open('submission.csv', 'a')

    rounded = round(pred)

    with csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([str(patch_name), rounded])

def batch_gen_into_CSV(patch_names, preds):

    if not os.path.isfile('submission.csv'):
        csv_file = open('submission.csv', 'w')

    else:
        csv_file = open('submission.csv', 'a')

    rounded = [round(x) for x in preds]

    batched = []
    
    for i, name in enumerate(patch_names):
        batched.append([str(name), rounded[i]])

    with csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(batched)



if __name__ == '__main__':

    try:
        os.remove('submission.csv')
    except OSError:
        pass


    names = [str(i) + '.jpg' for i in range(15)]
    outcomes = [random.random() for i in range(15)]

    # For non-batch appending
    ''' 
    for n, name in enumerate(names):
        gen_into_CSV(name, outcomes[n])
    '''

    # For batch writing
    batch_gen_into_CSV(names, outcomes)

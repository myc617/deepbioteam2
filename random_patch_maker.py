import pickle
import random

random_tumor_patch={}
random_normal_patch={}

random_train_set = {}
random_valid_set = {}
random_test_set = {}

tumor_patch={}
normal_patch={}

NORMAL = 160000
TUMOR = 40000
TUMOR_RATIO = 0.2
NORMAL_RATIO = 0.8

TRAINT = int(100000*TUMOR_RATIO)
VALIDT = int(50000*TUMOR_RATIO)
TESTT = int(50000*TUMOR_RATIO)

TRAINN = int(100000*NORMAL_RATIO)
VALIDN = int(50000*NORMAL_RATIO)
TESTN = int(50000*NORMAL_RATIO)
#mini test : train 25k / val 25k / test 10k => total 60k
#final : train 100k / val 50k / test 50k    => total 200k

file = open('normal_cancer_dict.txt','rb')
data = pickle.load(file)    #dict of normal+cancer

keys = list(data.keys())

for key in keys:
    if data.get(key) == 0:      #normal
        #normal_patch.append(key)
        normal_patch[key] = 0
    
    elif data.get(key) == 1:    #tumor
        #tumor_patch.append(key)
        tumor_patch[key] = 1

normal_keys = list(normal_patch.keys())
tumor_keys = list(tumor_patch.keys())

random_normal_keys = random.sample(normal_keys,NORMAL)
random_tumor_keys = random.sample(tumor_keys,TUMOR)

#splicing random normal/tumor set
train_nkey = random_normal_keys[0:TRAINN]
valid_nkey = random_normal_keys[TRAINN:TRAINN+VALIDN]
test_nkey = random_normal_keys[TRAINN+VALIDN:]

train_tkey = random_tumor_keys[0:TRAINT]
valid_tkey = random_tumor_keys[TRAINT:TRAINT+VALIDT]
test_tkey = random_tumor_keys[TRAINT+VALIDT:]

#randomly pick normal
for nkey in train_nkey:
    random_train_set[nkey] = 0

for nkey in valid_nkey:
    random_valid_set[nkey] = 0

for nkey in test_nkey:
    random_test_set[nkey] = 0

#randomly pick tumor
for tkey in train_tkey:
    random_train_set[tkey] = 1

for tkey in valid_tkey:
    random_valid_set[tkey] = 1

for tkey in test_tkey:
    random_test_set[tkey] = 1

#print
print('len of train:'+str(len(random_train_set)))
print('len of val:'+str(len(random_valid_set)))
print('len of test:'+str(len(random_test_set)))

#save data sets
with open('random_train_set_ver2.txt','wb') as f:
    pickle.dump(random_train_set,f)
f.close()

with open('random_valid_set_ver2.txt','wb') as a:
    pickle.dump(random_valid_set,a)
a.close()

with open('random_test_set_ver2.txt','wb') as b:
    pickle.dump(random_test_set,b)
b.close()

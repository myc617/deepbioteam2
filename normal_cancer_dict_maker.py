import pickle
import re

TUMOR_DICT_PATH = '/home/interns/tumor_patch_dict/'
TISSUE_DICT_PATH = '/home/interns/guldam/tissue_patch_dictionary'

normal_cancer_dict = {}
tumordict = {}

for i in range(1,16):
    with open(TUMOR_DICT_PATH+'dict'+str(i)+'.txt','rb') as a:   #library of tumor+tissue
        tumordata = pickle.load(a)
       # if i==1:
        tumordict.update(tumordata)
       # else:
       #     tumordict.update = tumordata
with open(TISSUE_DICT_PATH,'rb') as b:  #library of tissue only
    tissuedict = pickle.load(b)

pre_tumor_keys = list(tumordict.keys())
tissue_keys = list(tissuedict.keys())



#for key in pre_tumor_keys:
#    
#    pattern = 's(\d+)px(\d+)py(\d+)'
#    r = re.compile(pattern)
#    match = r.search(key)
#    key = 's'+match.group(1)+'px'+match.group(2)+'py'+match.group(3)
#    
#    if tumordict.get(key+'.png') == 1:      #if value= 1 in tumor+tissue library(cancer)
#        normal_cancer_dict[key] = 2
#
#    elif tissuedict.get(key) == 'Tissue':    #normal
#        normal_cancer_dict[key] = 1
#



for key in tissue_keys:

    if tumordict.get(key+'.png') == 1:      #if value= 1 in tumor+tissue library(cancer)
        normal_cancer_dict[key] = 1
        del tissuedict[key]

    else:    #normal
        normal_cancer_dict[key] = 0




f = open('normal_cancer_dict.txt','wb')
pickle.dump(normal_cancer_dict,f)
f.close()

import os
import pickle
#import subprocess
import shutil
import re 


SLIDE_PATCH_PATH = '/mnt/tmpfs/interns/slides/slides'
PATCHLIST_PATH = '/mnt/tmpfs/interns/tissuepatch'

patch_list=[]

with open('/home/interns/guldam/tissue_patch_dictionary','rb') as a:
        dict1 = pickle.load(a)

keys = list(dict1.keys())

for key in keys:
    pattern = 's(\d+)px(\d+)py(\d+)'
    r = re.compile(pattern)
    match = r.search(key)
    slide_number = match.group(1)
    shutil.move(SLIDE_PATCH_PATH+slide_number+'/'+match.group(0)+'.jpg',PATCHLIST_PATH)


    print(match.group(0),"success")
CD

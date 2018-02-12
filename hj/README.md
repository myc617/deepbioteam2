[hj]

 -normal_cancer_dict_maker.py
    'normal_cancer_dict.txt' 생성

 -random_patch_maker.py
    'random_train_set.txt', 'random_valid_set.txt', 'random_test_set.txt' 생성

 -tissue_patch_sampler.py
    '/mnt/ ... /interns/tissuepatch'폴더에 grid patch에서 tissue patch만 추출하여 저장

 -shape.py
    '/jwwoo/heatmap.py'에서 사용할 data(net(input)의 결과를 2D numpy array로 변형)
 
 -input_formatting.py
    make grid patches from input slide as np.array 
    
 -txts 폴더
    생성된 txt파일들 저장



image_name = 'data\\001.jpg'
base_name = image_name.split('\\')[-1]
print(base_name)
with open('./data/results/' + 'res_{}.txt'.format(base_name.split('.')[0]), 'w') as f:
    print(f)
import json
import os


"""
cd datasets
mkdir -p mix_baseline/annotations
cp MOT_LT/annotations/val.json mix_baseline/annotations/val.json
# cp MOT_LT/annotations/test.json mix_baseline/annotations/test.json
cd mix_baseline
ln -s ../MOT_LT/train MOT_LT_train
ln -s ../MOT17/train MOT17_train
ln -s ../crowdhuman/CrowdHuman_train crowdhuman_train
ln -s ../crowdhuman/CrowdHuman_val crowdhuman_val
ln -s ../Cityscapes cp_train
ln -s ../ETHZ ethz_train
ln -s ../CUHK-SYSU cuhk_train
ln -s ../PRW prw_train
cd ..
"""

MOT_LT_json = json.load(open('datasets/MOT_LT/annotations/train.json','r'))

img_list = list()
for img in MOT_LT_json['images']:
    img['file_name'] = 'MOT_LT_train/' + img['file_name']
    img_list.append(img)

ann_list = list()
for ann in MOT_LT_json['annotations']:
    ann_list.append(ann)

video_list = MOT_LT_json['videos']
category_list = MOT_LT_json['categories']


print('MOT_LT')

max_img = 10000
max_ann = 2000000
max_video = 18

crowdhuman_json = json.load(open('datasets/crowdhuman/annotations/train.json','r'))
img_id_count = 0
for img in crowdhuman_json['images']:
    img_id_count += 1
    img['file_name'] = 'crowdhuman_train/' + img['file_name']
    img['frame_id'] = img_id_count
    img['prev_image_id'] = img['id'] + max_img
    img['next_image_id'] = img['id'] + max_img
    img['id'] = img['id'] + max_img
    img['video_id'] = max_video
    img_list.append(img)

for ann in crowdhuman_json['annotations']:
    ann['id'] = ann['id'] + max_ann
    ann['image_id'] = ann['image_id'] + max_img
    ann_list.append(ann)

print('crowdhuman_train')

video_list.append({
    'id': max_video,
    'file_name': 'crowdhuman_train'
})


max_img = 30000
max_ann = 10000000

crowdhuman_val_json = json.load(open('datasets/crowdhuman/annotations/val.json','r'))
img_id_count = 0
for img in crowdhuman_val_json['images']:
    img_id_count += 1
    img['file_name'] = 'crowdhuman_val/' + img['file_name']
    img['frame_id'] = img_id_count
    img['prev_image_id'] = img['id'] + max_img
    img['next_image_id'] = img['id'] + max_img
    img['id'] = img['id'] + max_img
    img['video_id'] = max_video
    img_list.append(img)

for ann in crowdhuman_val_json['annotations']:
    ann['id'] = ann['id'] + max_ann
    ann['image_id'] = ann['image_id'] + max_img
    ann_list.append(ann)

print('crowdhuman_val')

video_list.append({
    'id': max_video,
    'file_name': 'crowdhuman_val'
})

max_img = 40000
max_ann = 20000000

ethz_json = json.load(open('datasets/ETHZ/annotations/train.json','r'))
img_id_count = 0
for img in ethz_json['images']:
    img_id_count += 1
    img['file_name'] = 'ethz_train/' + img['file_name'][5:]
    img['frame_id'] = img_id_count
    img['prev_image_id'] = img['id'] + max_img
    img['next_image_id'] = img['id'] + max_img
    img['id'] = img['id'] + max_img
    img['video_id'] = max_video
    img_list.append(img)

for ann in ethz_json['annotations']:
    ann['id'] = ann['id'] + max_ann
    ann['image_id'] = ann['image_id'] + max_img
    ann_list.append(ann)

print('ETHZ')

video_list.append({
    'id': max_video,
    'file_name': 'ethz'
})

max_img = 50000
max_ann = 25000000

cp_json = json.load(open('datasets/Cityscapes/annotations/train.json','r'))
img_id_count = 0
for img in cp_json['images']:
    img_id_count += 1
    img['file_name'] = 'cp_train/' + img['file_name'][11:]
    img['frame_id'] = img_id_count
    img['prev_image_id'] = img['id'] + max_img
    img['next_image_id'] = img['id'] + max_img
    img['id'] = img['id'] + max_img
    img['video_id'] = max_video
    img_list.append(img)

for ann in cp_json['annotations']:
    ann['id'] = ann['id'] + max_ann
    ann['image_id'] = ann['image_id'] + max_img
    ann_list.append(ann)

print('Cityscapes')

video_list.append({
    'id': max_video,
    'file_name': 'cityperson'
})

max_img = 60000
max_ann = 30000000

MOT17_json = json.load(open('datasets/MOT17/annotations/train.json','r'))
img_id_count = 0
for img in MOT17_json['images']:
    img_id_count += 1
    img['file_name'] = 'MOT17_train/' + img['file_name']
    img['frame_id'] = img_id_count
    img['prev_image_id'] = img['id'] + max_img
    img['next_image_id'] = img['id'] + max_img
    img['id'] = img['id'] + max_img
    img['video_id'] = max_video
    img_list.append(img)

for ann in MOT17_json['annotations']:
    ann['id'] = ann['id'] + max_ann
    ann['image_id'] = ann['image_id'] + max_img
    ann_list.append(ann)

print('MOT17')

video_list.append({
    'id': max_video,
    'file_name': 'MOT17'
})


max_img = 70000
max_ann = 40000000

cuhk_json = json.load(open('datasets/CUHK-SYSU/annotations/train.json','r'))
img_id_count = 0
for img in cuhk_json['images']:
    img_id_count += 1
    img['file_name'] = 'cuhk_train/' + img['file_name'][10:]
    img['frame_id'] = img_id_count
    img['prev_image_id'] = img['id'] + max_img
    img['next_image_id'] = img['id'] + max_img
    img['id'] = img['id'] + max_img
    img['video_id'] = max_video
    img_list.append(img)

for ann in cuhk_json['annotations']:
    ann['id'] = ann['id'] + max_ann
    ann['image_id'] = ann['image_id'] + max_img
    ann_list.append(ann)

print('CUHK-SYSU')

video_list.append({
    'id': max_video,
    'file_name': 'CUHK-SYSU'
})

max_img = 82000
max_ann = 50000000

prw_json = json.load(open('datasets/PRW/annotations/train.json','r'))
img_id_count = 0
for img in prw_json['images']:
    img_id_count += 1
    img['file_name'] = 'prw_train/' + img['file_name'][4:]
    img['frame_id'] = img_id_count
    img['prev_image_id'] = img['id'] + max_img
    img['next_image_id'] = img['id'] + max_img
    img['id'] = img['id'] + max_img
    img['video_id'] = max_video
    img_list.append(img)

for ann in prw_json['annotations']:
    ann['id'] = ann['id'] + max_ann
    ann['image_id'] = ann['image_id'] + max_img
    ann_list.append(ann)

print('PRW')

video_list.append({
    'id': max_video,
    'file_name': 'PRW'
})

mix_json = dict()
mix_json['images'] = img_list
mix_json['annotations'] = ann_list
mix_json['videos'] = video_list
mix_json['categories'] = category_list

json.dump(mix_json, open('datasets/mix_baseline/annotations/train.json','w'))
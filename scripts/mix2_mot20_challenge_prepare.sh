# Convert dataset
# python tools/convert_dataset/convert_crowdhuman_to_coco.py &&
# python tools/convert_dataset/convert_ethz_to_coco.py &&
# python tools/convert_dataset/convert_mot20_to_coco.py &&
# python tools/convert_dataset/convert_cityperson_to_coco.py &&

# Prepare for mix dataset
cd datasets  &&
mkdir -p mix2_mot20_challenge/annotations &&
cp MOT20/annotations/train.json mix2_mot20_challenge/annotations/val.json &&
cd mix2_mot20_challenge &&
ln -s ../crowdhuman/CrowdHuman_train crowdhuman_train &&
ln -s ../crowdhuman/CrowdHuman_val crowdhuman_val &&
ln -s ../Cityscapes cp_train &&
ln -s ../ETHZ ethz_train &&
ln -s ../MOT20/train MOT20_train &&
cd ../../ &&
# Really mix dataset
python tools/mix_dataset/mot20/mix2_mot20_challenge.py



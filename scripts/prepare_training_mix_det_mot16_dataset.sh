# Convert dataset
python tools/convert_dataset/convert_crowdhuman_to_coco.py &&
python tools/convert_dataset/convert_cuhk_sysu_to_coco.py &&
python tools/convert_dataset/convert_ethz_to_coco.py &&
python tools/convert_dataset/convert_prw_to_coco.py &&
python tools/convert_dataset/convert_mot16_to_coco.py &&
python tools/convert_dataset/convert_det_mot16_to_coco.py &&
python tools/convert_dataset/convert_mot17_to_coco.py &&
python tools/convert_dataset/convert_cityperson_to_coco.py &&

# Prepare for mix dataset
cd datasets  &&
mkdir -p mix_det_mot16/annotations &&
cp MOT16/annotations/train.json mix_det_mot16/annotations/val.json &&
cd mix_det_mot16 &&
ln -s ../crowdhuman/CrowdHuman_train crowdhuman_train &&
ln -s ../crowdhuman/CrowdHuman_val crowdhuman_val &&
ln -s ../Cityscapes cp_train &&
ln -s ../ETHZ ethz_train &&
ln -s ../CUHK-SYSU cuhk_train &&
ln -s ../PRW prw_train &&
ln -s ../MOT17/train MOT17_train &&
ln -s ../MOT16/train MOT16_train &&
ln -s ../MOT16/test MOT16_test_det &&
cd ../../ &&
# Really mix dataset
python tools/mix_dataset/mix_data_det_mot16_challenge.py



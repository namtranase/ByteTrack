cd datasets  &&
mkdir -p mix_mot16/annotations &&
cp MOT16/annotations/train.json mix_mot16/annotations/val.json &&
cd mix_mot16 &&
ln -s ../crowdhuman/CrowdHuman_train crowdhuman_train &&
ln -s ../crowdhuman/CrowdHuman_val crowdhuman_val &&
ln -s ../Cityscapes cp_train &&
ln -s ../ETHZ ethz_train &&
ln -s ../CUHK-SYSU cuhk_train &&
ln -s ../PRW prw_train &&
ln -s ../MOT17/train MOT17_train &&
ln -s ../MOT16/train MOT16_train &&
cd ../../

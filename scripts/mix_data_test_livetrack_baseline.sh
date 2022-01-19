cd datasets &&
mkdir -p mix_baseline/annotations &&
cp MOT_LT/annotations/val.json mix_baseline/annotations/val.json &&
cd mix_baseline &&
ln -s ../MOT_LT/train MOT_LT_train &&
ln -s ../MOT17/train MOT17_train &&
ln -s ../crowdhuman/CrowdHuman_train crowdhuman_train &&
ln -s ../crowdhuman/CrowdHuman_val crowdhuman_val &&
ln -s ../Cityscapes cp_train &&
ln -s ../ETHZ ethz_train &&
ln -s ../CUHK-SYSU cuhk_train &&
ln -s ../PRW prw_train &&
cd ../../
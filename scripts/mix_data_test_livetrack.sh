cd datasets  &&
mkdir -p mix_det/annotations &&
cp MOT_LT/annotations/val.json mix_det/annotations/val.json &&
cd mix_det &&
ln -s ../MOT_LT/train MOT_LT_train &&
ln -s ../crowdhuman/CrowdHuman_train crowdhuman_train &&
ln -s ../crowdhuman/CrowdHuman_val crowdhuman_val &&
ln -s ../Cityscapes cp_train &&
ln -s ../ETHZ ethz_train &&
cd ../../
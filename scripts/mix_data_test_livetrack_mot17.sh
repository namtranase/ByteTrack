cd datasets  &&
mkdir -p mix_det_17/annotations &&
cp MOT_LT/annotations/val.json mix_det_17/annotations/val.json &&
# cp MOT_LT/annotations/test.json mix_det_17/annotations/test.json &&
cd mix_det_17 &&
ln -s ../MOT_LT/train MOT_LT_train &&
ln -s ../MOT17/train MOT17_train &&
ln -s ../crowdhuman/CrowdHuman_train crowdhuman_train &&
ln -s ../crowdhuman/CrowdHuman_val crowdhuman_val &&
ln -s ../Cityscapes cp_train &&
ln -s ../ETHZ ethz_train &&
cd ../../
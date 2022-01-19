#!/bin/bash

set -e

mkdir -p $1/vis
search_dir=/the/path/to/base/dir/
for entry in "$search_dir"/*
do
  echo "$entry"
done

for f in "$1"/10fps/*; do
    echo $f
    video_name=$(basename ${f})
    echo $1/vis/$video_name
    python tools/demo_track_cam.py video --path $f -f exps/example/mix_dataset_livetrack/yolox_s_mix_dataset_det_livetrack.py -c /home/namtd/workspace/research/MOT-playground/ByteTrack/weights/trained/mix_dataset_livetrack/yolox_s_mix_dataset_det_livetrack/best_ckpt.pth.tar --save_path $1/vis/$video_name
    echo "================================================================================================================================================"
done

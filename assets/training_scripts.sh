# Superpod
## mix_livetrack
python tools/train.py -f exps/example/mix_livetrack/yolox_s_mix_livetrack.py -d 1 -b 64 --fp16 -o -c weights/mot_pretrained/bytetrack_s_mot17.pth.tar -expn yolox_s_mix_livetrack
python tools/train.py -f exps/example/mix_livetrack/yolox_m_mix_livetrack.py -d 1 -b 16 --fp16 -o -c weights/mot_pretrained/bytetrack_m_mot17.pth.tar -expn yolox_m_mix_livetrack
python tools/train.py -f exps/example/mix_livetrack/yolox_x_mix_livetrack.py -d 1 -b 8 --fp16 -o -c weights/mot_pretrained/bytetrack_x_mot17.pth.tar -expn yolox_x_mix_livetrack

## mot_livetrack
python tools/train.py -f exps/example/mot_livetrack/yolox_s_mot_livetrack.py -d 1 -b 32 --fp16 -o -c weights/mot_pretrained/bytetrack_s_mot17.pth.tar -expn yolox_s_mot_livetrack
python tools/train.py -f exps/example/mot_livetrack/yolox_m_mot_livetrack.py -d 1 -b 16 --fp16 -o -c weights/mot_pretrained/bytetrack_m_mot17.pth.tar -expn yolox_m_mot_livetrack
python tools/train.py -f exps/example/mot_livetrack/yolox_x_mot_livetrack.py -d 1 -b 8 --fp16 -o -c weights/mot_pretrained/bytetrack_x_mot17.pth.tar -expn yolox_x_mot_livetrack


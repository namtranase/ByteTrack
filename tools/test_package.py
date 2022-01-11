from yolox.bytrack_api import ByteTrackGP

args = ['webcam',
        # '--path=videos/palace.mp4',
        '-f=exps/example/mix_dataset_livetrack/yolox_s_mix_dataset_det_livetrack.py',
        '-c=/home/namtd/workspace/research/MOT-playground/ByteTrack/weights/trained/mix_dataset_livetrack/yolox_s_mix_dataset_det_livetrack/best_ckpt.pth.tar',
        '--save_result',
        '-expn=test_demo']

exp_file_path = 'exps/example/mix_dataset_livetrack/yolox_s_mix_dataset_det_livetrack.py'

bt_gp = ByteTrackGP(args=args, exp_file=exp_file_path)
bt_gp.inference_video()
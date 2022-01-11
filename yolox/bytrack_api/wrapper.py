from .bytrack_engine import *
from .utils import make_parser

class ByteTrackGP():
    def __init__(
        self,
        args,
        exp_file,
    ):
        self.args = args
        self.exp_file = exp_file

    def inference_video(self):
        self.args = make_parser().parse_args(self.args)
        print(self.args)
        exp = get_exp(self.exp_file, self.args.name)
        inference(exp, self.args)

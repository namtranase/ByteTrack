#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Copyright (c) Megvii, Inc. and its affiliates.
import os

from yolox.exp import Exp as MyExp


class Exp(MyExp):
    def __init__(self):
        super(Exp, self).__init__()
        self.depth = 0.67
        self.width = 0.75
        self.exp_name = os.path.split(os.path.realpath(__file__))[1].split(".")[0]

        # Define yourself dataset path
        self.data_dir = "datasets/LiveTrack_COCO"
        self.train_ann = "gt_train.json"
        self.val_ann = "gt_val.json"

        self.num_classes = 1
        self.max_epoch = 300
        self.data_num_workers = 4
        self.eval_interval = 1

        # # Conf 2
        # --------------  training config --------------------- # => For conf2
        # self.warmup_epochs = 5
        # self.warmup_lr = 0
        # self.basic_lr_per_img = 0.01 / 64.0
        # self.scheduler = "yoloxwarmcos"
        # self.no_aug_epochs = 15
        # self.min_lr_ratio = 0.05
        # self.ema = True

        # self.weight_decay = 5e-4
        # self.momentum = 0.9

        # # Conf 3
        self.mosaic_prob = 1.0
        self.mixup_prob = 1.0
        self.hsv_prob = 1.0
        self.flip_prob = 0.5
        self.degrees = 10.0
        self.translate = 0.1
        self.mosaic_scale = (0.1, 2)
        self.mixup_scale = (0.5, 1.5)
        self.shear = 2.0
        self.enable_mixup = True

        # --------------  training config --------------------- #
        self.warmup_epochs = 5
        self.warmup_lr = 0
        self.basic_lr_per_img = 0.01 / 64.0
        self.scheduler = "yoloxwarmcos"
        self.no_aug_epochs = 15
        self.min_lr_ratio = 0.05
        self.ema = True

        self.weight_decay = 5e-4
        self.momentum = 0.9
        # self.print_interval = 1
        self.eval_interval = 1
        self.exp_name = os.path.split(os.path.realpath(__file__))[1].split(".")[0]

        # -----------------  testing config ------------------ #
        self.test_size = (640, 640)
        self.test_conf = 0.01
        self.nmsthre = 0.65

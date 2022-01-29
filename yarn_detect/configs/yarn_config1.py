# -*- coding: utf-8 -*-
# @Time    : 2022/1/29 18:23
# @Author  : Marshall
# @FileName: yarn_config1.py
# The new config inherits a base config to highlight the necessary modification
_base_ = './mask_rcnn/mask_rcnn_r50_fpn_1x_coco.py'

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=2),
        mask_head=dict(num_classes=2)))

# Modify dataset related settings
dataset_type = 'COCODataset'
classes = ('warp', 'weft')
data = dict(
    train=dict(
        img_prefix='E:/1_dataset/fabric/dataset/',
        classes=classes,
        ann_file='E:/1_dataset/fabric/annotations/train_annotation.json'),
    val=dict(
        img_prefix='E:/1_dataset/fabric/val/',
        classes=classes,
        ann_file='E:/1_dataset/fabric/annotations/val_annotation.json'),
    test=dict(
        img_prefix='E:/1_dataset/fabric/test/',
        classes=classes,
        ann_file='E:/1_dataset/fabric/annotations/test_annotation.json'))

# We can use the pre-trained Mask RCNN model to obtain higher performance
load_from = 'checkpoints/mask_rcnn_r50_fpn_1x_coco_20200205-d4b0c5d6.pth'
import argparse
import json
import logging
import os

import cv2
import numpy as np
import rasterio as rio

from image_similarity_measures.quality_metrics import metric_functions

logger = logging.getLogger(__name__)


def read_image(path):
    logger.info("Reading image %s", os.path.basename(path))
    if path.endswith(".tif") or path.endswith(".tiff"):
        return np.rollaxis(rio.open(path).read(), 0, 3)
    return cv2.imread(path)


def evaluation(org_img_path, pred_img_path, metrics):
    output_dict = {}
    org_img = read_image(org_img_path)
    pred_img = read_image(pred_img_path)
    if type(metrics) == list:
        for metric in metrics:
            metric_func = metric_functions[metric]
            out_value = float(metric_func(org_img, pred_img))
            logger.info(f"{metric.upper()} value is: {out_value}")
            output_dict[metric] = out_value
    else:
        metric_func = metric_functions[metrics]
        out_value = float(metric_func(org_img, pred_img))
        logger.info(f"{metrics.upper()} value is: {out_value}")
        output_dict[metrics] = out_value

    return output_dict


def main(org_img_path, pred_img_path, metrics):

    metric_values = evaluation(
        org_img_path=org_img_path,
        pred_img_path=pred_img_path,
        metrics=metrics,
    )
    result_dict = {"image1": org_img_path, "image2": pred_img_path, "metric": metric_values}
    return result_dict

import warnings

from image_similarity_measures_library import image_similarity_measures as similarity
import twitterSearch
import urllib.request as get
from PIL import Image
import os
import main

warnings.filterwarnings("ignore")

metrics = {"fsim": (">", 0.5), "psnr": (">", 50), "rmse": ("<", 0.001), "sre": (">", 100)}


def isSame(metricList, metricJson):
    for metric in metricList:
        if metrics[metric][0] == ">":
            if metricJson[metric] > metrics[metric][1]:
                pass
            else:
                return False, metric
        elif metrics[metric][0] == "<":
            if metricJson[metric] < metrics[metric][1]:
                pass
            else:
                return False, metric
    return True, "Pass"


def singleCompare(comparisonImage, user_id, metricList = ["sre", "fsim", "psnr", "rmse"]):
    # comparisonImage = "images/comparisons/oni1"
    imageURL, imageName = twitterSearch.fetch_image(user_id=user_id)  # backup ID 1517894403758641152
    twitterImage = f"images/twitter/twitterImage{imageName}"
    get.urlretrieve(imageURL, f"{twitterImage}.jpg")

    comp = Image.open(f"{comparisonImage}.jpg").convert("RGB")
    twitter = Image.open(f"{twitterImage}.jpg").convert("RGB")

    if comp.size > twitter.size:
        comp = comp.resize(twitter.size, Image.ANTIALIAS)
        print("Resizing Comparison Image")
        print(comp.size)
    elif comp.size < twitter.size:
        twitter = twitter.resize(comp.size, Image.ANTIALIAS)
        print("Resizing Twitter Image")
    else:
        pass
    comp.save(f"{comparisonImage}.tif", 'TIFF')
    twitter.save(f"{twitterImage}.tif", 'TIFF')
    finalJson = similarity.evaluate.main(f"{twitterImage}.tif", f"{comparisonImage}.tif", metricList)
    print(finalJson["metric"])
    print(isSame(metricList, finalJson["metric"]))


def batchCompare(user_ids, comparisonImage="images/comparisons/image1"):
    compResults = {}

    comp = Image.open(f"{comparisonImage}.jpg").convert("RGB")
    comp.save(f"{comparisonImage}.tif", 'TIFF')

    for user_id in user_ids:
        imageURL, imageName = twitterSearch.fetch_image(user_id=user_id)  # backup ID 1517894403758641152
        twitterImage = f"images/twitter/twitterImage{imageName}"
        get.urlretrieve(imageURL, f"{twitterImage}.jpg")
        twitter = Image.open(f"{twitterImage}.jpg").convert("RGB")
        twitter = twitter.resize(comp.size, Image.ANTIALIAS)
        twitter.save(f"{twitterImage}.tif", 'TIFF')
        metricList = ["sre", "fsim", "psnr", "rmse"]
        finalJson = similarity.evaluate.main(f"{twitterImage}.tif", f"{comparisonImage}.tif", metricList)
        # print(finalJson["metric"])
        output = isSame(metricList, finalJson["metric"])
        print(output)
        compResults[user_id] = output
    print(compResults)


# singleCompare("images/comparisons/oni1", 1517894403758641152)
batchCompare([1436756733775552516, 1517894403758641152, 1375234369636331522], "images/comparisons/image1")

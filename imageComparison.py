import warnings

from image_similarity_measures_library import image_similarity_measures as similarity
import twitterSearch
import urllib.request as get
from PIL import Image
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
    return True


def singleCompare(comparisonImage, user_id):
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
    metricList = ["sre", "fsim", "psnr", "rmse"]
    finalJson = similarity.evaluate.main(f"{twitterImage}.tif", f"{comparisonImage}.tif", metricList)
    print(finalJson["metric"])
    print(isSame(metricList, finalJson["metric"]))

singleCompare("images/comparisons/oni1", 1517894403758641152)
import warnings

from image_similarity_measures_library import image_similarity_measures as similarity
import twitterSearch
import urllib.request as get
from PIL import Image
import main
warnings.filterwarnings("ignore")

metrics = {"fsim": 1, "issm": 1, "psnr": 1, "rmse": 0.001, "sam": 1, "sre": 1, "ssim": 1, "uiq": 1}


comparisonImage = "images/comparisons/wp4676622-4k-pc-wallpapers"
imageURL, imageName = twitterSearch.fetch_image(user_id=1517894403758641152)
twitterImage = f"images/twitter/twitterImage{imageName}"
get.urlretrieve(imageURL, f"{twitterImage}.jpg")

comp = Image.open(f"{comparisonImage}.jpg")
twitter = Image.open(f"{twitterImage}.jpg")

if comp.size > twitter.size:
    comp = comp.resize(twitter.size, Image.ANTIALIAS)
    print("Resizing Comparison Image")
elif comp.size < twitter.size:
    twitter = twitter.resize(comp.size, Image.ANTIALIAS)
    print("Resizing Twitter Image")
else:
    pass
comp.save(f"{comparisonImage}.tif", 'TIFF')
twitter.save(f"{twitterImage}.tif", 'TIFF')

finalJson = similarity.evaluate.main(f"{twitterImage}.tif", f"{comparisonImage}.tif", ["rmse", "ssim", "sre"])
print(finalJson["metric"])
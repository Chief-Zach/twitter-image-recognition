import warnings

from image_similarity_measures_library import image_similarity_measures as similarity
import twitterSearch
import urllib.request as get
from PIL import Image
import main
warnings.filterwarnings("ignore")

metrics = {"fsim": (">", 0.5), "psnr": (">", 50), "rmse": ("<", 0.001), "sre": (">", 100)}


comparisonImage = "images/comparisons/oni1"
imageURL, imageName = twitterSearch.fetch_image(user_id=1517894403758641152)
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

finalJson = similarity.evaluate.main(f"{twitterImage}.tif", f"{comparisonImage}.tif", "uiq")
print(finalJson["metric"])
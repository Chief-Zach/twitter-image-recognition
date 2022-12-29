import imageComparison
import sys, getopt


def main(argv):
    twitterID = 0
    image = ''
    batch = []
    opts, args = getopt.getopt(argv, "hm:t:i:b:", ["mode=", "twitter=", "image=", "batch="])
    for opt, arg in opts:
        if opt == "-h":
            print('twitterComparison.py -m single -t <twitterID> -i <image name>')
            print('twitterComparison.py -m batch -t <twitterID> -b <id batch>')
            sys.exit()
        elif opt in ("-t", "--twitter"):
            twitterID = int(arg)
        elif opt in ("-i", "--image"):
            image = arg
        elif opt in ("-d", "--directory"):
            batch = arg.split(",")
        elif opt in ("-m", "--mode"):
            if arg == "single":
                imageComparison.singleCompare(image, twitterID)
            elif arg == "batch":
                imageComparison.batchCompare(batch, image)
            else:
                print(f"{arg} is not a valid mode")
                sys.exit()
        else:
            print('twitterComparison.py -m single -t <twitterID> -i <image name>')
            print('twitterComparison.py -m batch -t <twitterID> -b <id batch>')
            sys.exit()


if __name__ == '__main__':
    main(sys.argv[1:])

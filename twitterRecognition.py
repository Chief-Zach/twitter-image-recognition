import imageComparison
import sys, getopt


def main(argv):
    print(argv)
    opts, args = getopt.getopt(argv, "hm:t:i:b:", ["mode=", "twitter=", "image=", "batch="])
    for opt, arg in opts:
        print(opts, arg)
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
            if arg == "single" or arg == "batch":
                mode = arg
            else:
                print(f"{arg} is not a valid mode")
                sys.exit()
        else:
            print('twitterComparison.py -m single -t <twitterID> -i <image name>')
            print('twitterComparison.py -m batch -t <twitterID> -b <id batch>')
            sys.exit()
    try:
        if mode == "single":
            imageComparison.singleCompare(image, twitterID)
        elif mode == "batch":
            imageComparison.batchCompare(batch, image)
    except UnboundLocalError:
        print('twitterComparison.py -m single -t <twitterID> -i <image name>')
        print('twitterComparison.py -m batch -t <twitterID> -b <id batch>')
        sys.exit()


if __name__ == '__main__':
    main(sys.argv[1:])

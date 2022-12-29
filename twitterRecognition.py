import imageComparison
import sys, getopt


def main(argv):
    # print(argv)
    opts, args = getopt.getopt(argv, "hu:m:t:i:b:", ["metrics=", "mode=", "twitter=", "image=", "batch="])
    metric = False
    for opt, arg in opts:
        # print(opts, arg)
        if opt == "-h":
            print('twitterComparison.py -m single -t <twitterID> -i <image name>')
            print('twitterComparison.py -m batch -t <twitterID> -b <id batch>')
            sys.exit()
        elif opt in ("-u", "--metrics"):
            metrics = arg
            if "," in metrics:
                metrics = metrics.split(",")
            metric = True
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
            print('twitterComparison.py -m single -t <51946511351655> -i <image1>')
            print('twitterComparison.py -m batch -t <5191654919516519,23453457345623452,134524573452334> -i <image1>')
            sys.exit()
    try:
        if mode == "single":
            if metric:
                imageComparison.singleCompare(image, twitterID, [metrics])
            else:
                imageComparison.singleCompare(image, twitterID)
        elif mode == "batch":
            if metric:
                imageComparison.batchCompare(batch, image, [metrics])
            else:
                imageComparison.batchCompare(image, twitterID)
    except UnboundLocalError as e:
        print('twitterComparison.py -m single -t <51946511351655> -i <image1>')
        print('twitterComparison.py -m batch -t <5191654919516519,23453457345623452,134524573452334> -i <image1>')
        sys.exit()


if __name__ == '__main__':
    main(sys.argv[1:])

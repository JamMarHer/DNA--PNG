import sys

if __name__ == '__main__':
    if (len(sys.argv)<=1):
        print("Please provide a input file.")
        exit()

    if (sys.argv[1:][0].split(".")[-1] != "txt"):
        # TODO eh it could technically in other format, good for now.
        print("Please make sure that the file is in txt format")
        exit()
 

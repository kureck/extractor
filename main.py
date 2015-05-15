import sys
from extractor.extractor import Extractor


def run(in_root_dir, out_root_dir):
    extractor = Extractor(in_root_dir, out_root_dir)
    extractor.folder_travel()

if __name__ == '__main__':
    if len(sys.argv) <= 2:
        print "Wrong parameters"
    else:
        in_root_dir = sys.argv[1]
        out_root_dir = sys.argv[2]

        run(in_root_dir, out_root_dir)

import sys


def run(in_root_dir, out_root_dir):
    pass

if __name__ == '__main__':
    if len(sys.argv) <= 2:
        print "Wrong parameters"
    else:
        in_root_dir = sys.argv[1]
        out_root_dir = sys.argv[2]

    run(in_root_dir, out_root_dir)

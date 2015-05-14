import os
import errno


class Extractor:
    def __init__(self, in_root_folder, out_root_folder):
        self.in_root_folder = in_root_folder
        self.out_root_folder = out_root_folder

    def create_out_folder(self):
        try:
            os.makedirs(self.out_root_folder)
        except OSError as exception:
            if exception.errno is not errno.EEXIST:
                raise

    def folder_travel(self):
        # Set the directory you want to start from
        for dirName, subdirList, fileList in os.walk(self.in_root_folder):
            print('Found directory: %s' % dirName)
            for fname in fileList:
                print('\t%s' % fname)

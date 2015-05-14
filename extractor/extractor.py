import os
import errno


class Extractor:
    def __init__(self, in_root_folder, out_root_folder):
        self.in_root_folder = in_root_folder
        self.out_root_folder = out_root_folder

    def create_out_folder(self, out_root_folder):
        try:
            os.makedirs(out_root_folder)
        except OSError as exception:
            if exception.errno is not errno.EEXIST:
                raise

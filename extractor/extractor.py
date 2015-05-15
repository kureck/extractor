import os
import errno
import zipfile
import uuid


class Extractor:
    def __init__(self, in_root_folder, out_root_folder):
        self.in_root_folder = in_root_folder
        self.out_root_folder = out_root_folder
        self._create_out_folder()

    def _create_out_folder(self):
        try:
            os.makedirs(self.out_root_folder)
        except OSError as exception:
            print "Folder already exists!"
            if exception.errno is not errno.EEXIST:
                raise

    def _check_file_extension(self, file_name, extension):
        return file_name.endswith(extension)

    def _extract_csv(self, zip_file):
        try:
            with zipfile.ZipFile(zip_file, 'r') as z:
                print "Extracting from zip file: %s" % zip_file
                files = self._get_csv_from_zip(z)
                for file_name in files:
                    print "Extracting csv: %s" % file_name
                    z.extract(file_name, self.out_root_folder)
        except zipfile.BadZipfile:
            print "Not valid zip, maybe corrupted!"

    def _change_file_name(self, file_name):
        return "%s_%s" % (str(uuid.uuid4()), file_name.replace('/', ''))

    # def get_csv_from_zip(self, z):
    #     def f(x): return x if x.endswith('.csv') else None
    #     return filter(f, z.namelist())

    def _get_csv_from_zip(self, z):
        zinfo = z.infolist()
        zlist = []
        for i, _ in enumerate(zinfo):
            if self._check_file_extension(zinfo[i].filename, '.csv'):
                zinfo[i].filename = self._change_file_name(zinfo[i].filename)
                zlist.append(zinfo[i])
        return zlist

    def folder_travel(self):
        # Set the directory you want to start from
        for dirName, subdirList, fileList in os.walk(self.in_root_folder):
            print('Found directory: %s' % dirName)
            for fname in fileList:
                print('\t%s' % fname)
                is_zip = self._check_file_extension(fname, '.zip')
                if is_zip:
                    self._extract_csv("%s/%s" % (dirName,fname))

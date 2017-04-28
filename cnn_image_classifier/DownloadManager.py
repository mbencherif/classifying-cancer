import os
import logging
from urllib.request import urlretrieve
from progressbar import ProgressBar, Percentage, Bar


class DownloadManager:

    def __init__(self, source_data, download_url):
        self.source_data = source_data
        self.download_url = download_url

    def download(self):
        """Download data if not present on local FileSystem"""

        def progress(count, blockSize, totalSize):
            pbar.update(int(count * blockSize * 100 / totalSize))

        full_url = self.download_url + '/' + self.source_data

        if not os.path.exists(self.source_data):
            logging.info(
                "%s not found on local filesystem. File will be downloaded from %s.", self.source_data,
                full_url)

            pbar = ProgressBar(widgets=[Percentage(), Bar()])
            urlretrieve(full_url, self.source_data, reporthook=progress)

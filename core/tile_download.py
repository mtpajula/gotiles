from pathlib import Path
import requests
import os


class TileDownload:

    def __init__(self, path, filetype):
        self.folder = '/output'
        self.path = path
        self.filetype = filetype

    def get_folder(self):
        current_dir = Path(__file__).parent.parent
        return Path(str(current_dir) + self.folder)

    def create_folder(self):
        print(self.get_folder())
        self.get_folder().mkdir(parents=True, exist_ok=True)

    def download_tiles(self, tilepoints):
        for tp in tilepoints:
            if not self.download_tile(tp):
                return False
        return True

    def download_tile(self, tp):
        file_path = tp.get_addr(str(self.get_folder()) + '/', self.filetype)
        url = tp.get_addr(self.path, self.filetype)
        print(url, end='')
        try:
            r = requests.get(url)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'wb') as f:
                f.write(r.content)

            print(' => ok')
            return True
        except Exception as e:
            print(' => Error downloading', e)
            return False

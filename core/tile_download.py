from pathlib import Path
import requests
import os


class TileDownload:

    def __init__(self, path, filetype):
        self.folder = '/output'
        self.path = path
        self.filetype = filetype
        self.override = False

    def get_folder(self):
        current_dir = Path(__file__).parent.parent
        return Path(str(current_dir) + self.folder)

    def create_folder(self):
        print(self.get_folder())
        self.get_folder().mkdir(parents=True, exist_ok=True)

    def download_tiles(self, tilepoints):
        for i, tp in enumerate(tilepoints):
            if self.download_tile(tp):
                print(f' {round(i / len(tilepoints) * 100, 1)}%')
            else:
                return False
        return True

    def tile_exists(self, file_path):
        if self.override:
            return False
        return os.path.exists(file_path)

    def download_tile(self, tp):
        file_path = tp.get_addr(str(self.get_folder()) + '/', self.filetype)
        url = tp.get_addr(self.path, self.filetype)
        print(url, end='')
        try:
            if self.tile_exists(file_path):
                print(' => tile exists', end='')
            else:
                r = requests.get(url)
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                with open(file_path, 'wb') as f:
                    f.write(r.content)
                print(' => ok', end='')
            return True
        except Exception as e:
            print(' => Error downloading', e)
            return False

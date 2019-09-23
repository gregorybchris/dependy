"""Reader for parsing project files and directories."""
import os


class ProjectReader:
    """Reader for parsing project files and directories."""
    def __init__(self):
        pass

    def read(self, *packages):
        """
        Read in projects to be searched recursively.
        
        :param packages: Package objects to parse.
        """
        print(f"Reading {len(packages)} package(s)...")
        for package in packages:
            print(f'\tLoading {package.get_name()}...')
            for root, dirs, files in os.walk(package.get_path()):
                print('root', root)
                print('dirs', dirs)
                print('files', files)
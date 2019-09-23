import os


class Package:
    def __init__(self, package_name, package_path):
        """
        Construct a Package object.

        :param package_name: Name of the package.
        :param package_path: Path to the package.
        """
        if not os.path.isdir(package_path):
            raise IOError(f"{package_path} not found.")

        self._package_name = package_name
        self._package_path = package_path
    
    def get_name(self):
        """
        Get the name of the package.

        :return: The name of the package.
        """
        return self._package_name
    
    def get_path(self):
        """
        Get the absolute path to the package.

        :return: The absolute path to the package.
        """
        return self._package_path

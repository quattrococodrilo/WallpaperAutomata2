from os import system


class Paper:

    def __init__(self, image_path) -> None:
        self._image_path = image_path
        self._set_wallpaper()

    @staticmethod
    def create(image_path):
        return Paper(image_path)

    def _set_wallpaper(self):
        command = f"gsettings set org.gnome.desktop.background picture-uri 'file://{self._image_path}'"
        system(command)

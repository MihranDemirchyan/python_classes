import requests
import json


class Url:
    def __init__(self, json_path):
        # self.image_list = []
        with open(json_path) as file:
            self.images = json.load(file)

    def download_image(self, url, name):
        print("started", name)
        try:
            response_ = requests.get(url)
        except requests.exceptions.ConnectionError as err:
            print(f"smth happened {err}")
            return

        if response_.status_code == 200:
            with open(f"{name}", "wb") as photo:
                photo.write(response_.content)
                print(f"image {name} is downloaded")

    def download_all(self):
        for image in self.images:
            self.download_image(url=image["img_url"], name=image["img_name"])


if __name__ == "__main__":

    img_download = Url(json_path="new.json")
    img_download.download_all()

import threading
import json
import requests


class ImgDownloader:
    def __init__(self, json_path):
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

    def download_with_threads(self):
        thread_list = []
        for image in self.images:
            x = threading.Thread(target=self.download_image, args=(image["img_url"], image["img_name"]))
            thread_list.append(x)
            x.start()
        for td in thread_list:
            td.join()
        print("downloaded with threads")


if __name__ == "__main__":
    img_download = ImgDownloader(json_path="photos_10.json")
    img_download.download_with_threads()

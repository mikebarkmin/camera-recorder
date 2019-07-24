from PIL import Image, ImageChops
import requests
import math


class Recorder():

    def __init__(self, url):
        self.url = url
        self.image = None
        self.last_image = None

    def capture(self):
        """
        Captures an image
        """
        response = requests.get(self.url, stream=True)
        self.last_image = self.image
        self.image = Image.open(response.raw)

    def compare(self):
        """
        Compares the last two captured images.
        """
        if self.image is None or self.last_image is None:
            return 0

        image = ImageChops.difference(self.image, self.last_image)
        return Recorder.image_entropy(image)

    @staticmethod
    def image_entropy(image):
        """
        Calculates how much is going on in the image.
        """
        histogram = image.histogram()
        histogram_length = sum(histogram)
        samples_probability = [float(h) / histogram_length for h in histogram]
        return -sum([p * math.log(p, 2) for p in samples_probability if p != 0])

    def save(self, bw=False):
        if bw:
            self.image = self.image.convert('1')
        self.image.save("bw.jpg")

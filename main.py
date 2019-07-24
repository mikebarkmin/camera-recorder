from time import sleep
from recorder import Recorder


if __name__ == '__main__':
    url = input("IP Wecam URL: ")
    recorder = Recorder(url)

    while True:
        recorder.capture()
        print(recorder.compare())

        sleep(0.5)

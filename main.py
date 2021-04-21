import pyautogui as pa
from python_imagesearch.imagesearch import *
from time import sleep


def run():
    images = [
        "mining_hub",
        "mine",
        "claim",
        "cap",
        "error",
        "error_x"
    ]

    while True:
        for img in images:
            if imagesearch("img/" + img + ".png")[0] != -1:
                if img == "error":
                    click("./img/error_x.png")
                    pa.click()
                else:
                    click("./img/" + img + ".png")
                    pa.click()

        sleep(1)


def click(image, offset=5):
    pos = imagesearch(image)
    img = cv2.imread(image)
    height, width, channels = img.shape
    pa.moveTo(pos[0] + r(width / 2, offset), pos[1] + r(height / 2, offset),
              0.5)
    pa.click(button="left")


if __name__ == '__main__':
    run()

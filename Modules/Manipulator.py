import cv2
from rembg import remove

class Manipulator:
    def __init__(self):
        return
    
    def remove_bg(image, save = "", serChroma = False):
        img = remove(image)
        if save != "":
            cv2.imwrite(save, img)
        return img
    
    
if __name__ == "__main__":
    # img = cv2.imread("Images/ChromaKey.jpg", cv2.IMREAD_COLOR) 
    img = cv2.imread("Images/Lenna.png", cv2.IMREAD_COLOR) 
    img = Manipulator.remove_bg(img, "Images/Lenna_rmbg.png")
    cv2.imshow("base", img)

    cv2.waitKey(0)

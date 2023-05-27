import cv2
from rembg import remove
import numpy as np

class Manipulator:
    def __init__(self):
        return
    
    def remove_bg(image, save = "", serChroma = False):
        img = remove(image)
        if save != "":
            cv2.imwrite(save, img)
        return img
    
    
if __name__ == "__main__":
    bg = cv2.imread("Images/ChromaKey.png", cv2.IMREAD_COLOR) 
    lenna = cv2.imread("Images/Lenna.png", cv2.IMREAD_COLOR) 
    print(lenna[0][0])
    print(bg.shape)
    lenna = Manipulator.remove_bg(lenna, "Images/Lenna_rmbg.png")
    # cv2.cvtColor(lenna, cv2.COLOR_BGR2RGB)
    h, w = lenna.shape[:2]
    
    # cv2.cvtColor(lenna, lenna, cv2.COLOR_BGR2RGB)
    # print(lenna.shape)
    # mask = np.full_like(lenna,)
    # img = cv2.seamlessClone(lenna, bg,)
    # hsv = cv2.cvtColor(lenna, cv2.COLOR_BGR2HSV)
    # mask = cv2.inRange(hsv, (0, 0, 0), (0, 0, 0))
    x_offset = 50
    y_offset = 50
    print(bg.shape)
    b_channel, g_channel, r_channel = cv2.split(bg)
    alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype)
    bg = cv2.merge((b_channel, g_channel, r_channel, alpha_channel))
    print(bg.shape)
    print(lenna.shape)
    print(lenna[0][0])
    for i in range(h):
        for j in range(w):
            if lenna[i][j][3] > 15:
                bg[y_offset+i][x_offset+j] = lenna[i][j]
        
    # bg[y_offset:y_offset+512, x_offset:x_offset+512] = lenna
    
    cv2.imshow("base", bg)

    cv2.waitKey(0)

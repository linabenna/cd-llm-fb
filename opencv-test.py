import cv2
import numpy as np
from PIL import Image
import urllib.request
import util

def detect_objects(hsv_frame):
    detected_objects = []
    area_min = 20
    area_max = 6000
    for color, (lower, upper) in colors.items():
        mask = None
        if color == "red":
            mask1 = cv2.inRange(hsv_frame, lower[0], lower[1])
            mask2 = cv2.inRange(hsv_frame, upper[0], upper[1])
            mask = cv2.bitwise_or(mask1, mask2)
        else:
            mask = cv2.inRange(hsv_frame, lower, upper)
            grey = False

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > area_min:
                if color == "grey" and area >= area_max:
                    continue
                else:
                    x, y, w, h = cv2.boundingRect(contour)
                    detected_objects.append((color, (x, y, w, h)))
    return detected_objects


colors = {
    "yellow": (
        util.y1.hsv[0][0],
        util.y2.hsv[0][0]
    ),
    "blue": (
        util.b1.hsv[0][0],
        util.b2.hsv[0][0]
    ),
    "brown": (
        util.br1.hsv[0][0],
        util.br2.hsv[0][0]
    ),
    "purple": (
        util.p1.hsv[0][0],
        util.p2.hsv[0][0]
    ),
    "grey": (
        util.g1.hsv[0][0],
        util.g2.hsv[0][0]
    ),
    "green": (
        util.gr1.hsv[0][0],
        util.gr2.hsv[0][0]
    ),
    # "gold": (
    #     util.gl1.hsv[0][0],
    #     util.gl2.hsv[0][0]
    # ),
    "red": (
        (util.r1l.hsv[0][0], util.r2l.hsv[0][0]),
        (util.r1h.hsv[0][0], util.r2h.hsv[0][0])
    )
}

def detect():
    # req = urllib.request.urlopen(pic)
    # arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    # image = cv2.imdecode(arr, -1)
    image = cv2.imread("input_image.jpg")
    imcopy = image.copy()
    imcopy2 = image.copy()
    

    y1 = 0
    edges = cv2.Canny(image,100,200)
    edge_win = 'Edge Detection'
    cv2.namedWindow(edge_win)
    cv2.moveWindow(edge_win, -100, y1)
    cv2.imshow(edge_win, edges)

    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse = True)
    for i in range(len(contours)):
        contour = contours[i]
        color = (255, 0, 0)
        cv2.drawContours(imcopy, [contour], -1, color, 2)

    #cv2.drawContours(imcopy, contours, -1, (255, 0, 0), 2)
    contour_win = 'Contour Detection'
    cv2.namedWindow(contour_win)
    x1 = 640
    cv2.moveWindow(contour_win, x1, y1)
    cv2.imshow(contour_win, imcopy)

    hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    detected_objects = detect_objects(hsvImage)
    for color, (x, y, w, h) in detected_objects:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(image, color, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    col_win = 'Color Detection'
    cv2.namedWindow(col_win)
    cv2.moveWindow(col_win, x1*2, y1)
    cv2.imshow(col_win, image)

    grey_img = cv2.cvtColor(imcopy2, cv2.COLOR_BGR2GRAY)
    grey_win = 'Greyscale Image'
    cv2.namedWindow(grey_win)
    cv2.moveWindow(grey_win, 0,600)
    cv2.imshow(grey_win, grey_img)
    adjusted = cv2.addWeighted(grey_img, 3., np.zeros(grey_img.shape, grey_img.dtype), 0, 95)

    adj_edges = cv2.Canny(adjusted,100,200)
    contours, _ = cv2.findContours(adj_edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse = True)
    for i in range(len(contours)):
        contour = contours[i]
        color = (0, 0, 0)
        #print(f'\n{i}. {contour}, Len: {len(contour)}')
        #if len(contour) > 15:
            #print(f'\n{i}. {contour}, Len: {len(contour)}')
        cv2.drawContours(adjusted, [contour], -1, color, 2)

    adj_win = 'Material Detection'
    cv2.namedWindow(adj_win)
    cv2.moveWindow(adj_win, x1,600)
    cv2.imshow(adj_win, adjusted)

    org_win = 'Original Image'
    cv2.namedWindow(org_win)
    cv2.moveWindow(org_win, x1*2, 600)
    cv2.imshow(org_win, imcopy2)

    cv2.waitKey()
    cv2.destroyAllWindows()


detect()

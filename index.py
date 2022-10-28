import cv2 

#convert an image into cartoon character
#You can customize the value of the given parameters
def cartoonify(img):
    #convert the image into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #apply median blur to smoothen the image
    gray = cv2.medianBlur(gray,5)
    #detect edges in an image and threshold it
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9,9)
    #apply bilateral filter to remove noise and keep edge sharp as possible
    color  = cv2.bilateralFilter(img, 9, 300, 300)
    #mask edged image with our "BEAUTIFY" image
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    return cartoon

if __name__ == "__main__":
    #read image
    img = cv2.imread("ADA.png")
    #call cartoonify function
    cartoon = cartoonify(img)
    #display image
    cv2.imshow("Cartoon", cartoon)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
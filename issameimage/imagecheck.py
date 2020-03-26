import sys
import cv2
import argparse

def how_about_shape(ori_img, sec_img):
    if fir_img.shape == sec_img.shape:
        print("\nThe images have same size and channels\n")
        return True
    else:
        print("\nThe images have not smae size and channels")
        return False


def how_about_rgb(ori_img, cmp_img):
    h, w, c = ori_img.shape
    difference = cv2.subtract(ori_img, cmp_img)
    b, g, r = cv2.split(difference)

    if cv2.countNonZero(b) == 0 \
            and cv2.countNonZero(g) == 0 \
            and cv2.countNonZero(r) == 0:
        print("And, the images are completely Equal!\n")

    else:
        sum_ = cv2.countNonZero(b) + cv2.countNonZero(g) + cv2.countNonZero(r)
        print("But, the images are not Equal...\n")
        '''
        print(
            "blue:", cv2.countNonZero(b), \
            "green:", cv2.countNonZero(g), \
            "red:", cv2.countNonZero(r)
        )

        print(f"diff(%): {sum_ / ((h * w)*c)*100}%\n")
        '''
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--first', help="first image")
    parser.add_argument('--second', help="second image")
    args = parser.parse_args()
    
    fir_img = cv2.imread(args.first)
    sec_img = cv2.imread(args.second)

    if how_about_shape(fir_img, sec_img):
        how_about_rgb(fir_img,sec_img)
    

   



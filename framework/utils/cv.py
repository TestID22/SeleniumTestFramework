import cv2


class VisionUtils:
    @staticmethod
    def compare_images(img1_path, img2_path, threshold=0.95):
        image1 = cv2.imread(img1_path)
        image2 = cv2.imread(img2_path)

        # Convert to grayscale
        gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

        # Compute similarity
        res = cv2.matchTemplate(gray1, gray2, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(res)

        return max_val >= threshold

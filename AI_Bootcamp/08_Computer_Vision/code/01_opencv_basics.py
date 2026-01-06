import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    print("=== OpenCV Basic Image Processing ===\n")
    
    # 1. Create a dummy image (Black image)
    # 300x300 pixels, 3 channels (RGB)
    img = np.zeros((300, 300, 3), dtype='uint8')
    
    # 2. Draw Shapes
    # Rectangle (Blue)
    cv2.rectangle(img, (50, 50), (250, 250), (255, 0, 0), 3)
    # Circle (Green)
    cv2.circle(img, (150, 150), 80, (0, 255, 0), -1) # -1 means filled
    # Line (Red)
    cv2.line(img, (0, 0), (300, 300), (0, 0, 255), 5)
    
    # 3. Text
    cv2.putText(img, "OpenCV Demo", (60, 280), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    
    # 4. Color Conversion (BGR to Grayscale)
    # Note: OpenCV uses BGR by default, matplotlib uses RGB
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 5. Save Image
    cv2.imwrite("generated_image.jpg", img)
    print("Image saved as 'generated_image.jpg'")

    # Visualize (using matplotlib for compatibility)
    # Convert BGR to RGB for correct display in matplotlib
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(img_rgb)
    plt.title("Original (RGB)")
    
    plt.subplot(1, 2, 2)
    plt.imshow(gray_img, cmap='gray')
    plt.title("Grayscale")
    
    # plt.show()
    print("Visualization code executed.")

if __name__ == "__main__":
    main()

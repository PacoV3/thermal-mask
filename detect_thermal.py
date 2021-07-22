# import the necessary packages
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import plot_model
import numpy as np
import cv2

model = load_model("thermal_mask_detector.model")
plot_model(
    model,
    to_file="model.png",
    show_shapes=True,
    show_layer_names=True,
    rankdir="TB",
    expand_nested=True,
    dpi=96
)

image = cv2.imread("examples/mask1.jpg")
h, w = image.shape[:2]
startX, startY = 10, 0
endX, endY = w - 11, h - 1

final_image = image[startY:endY, startX:endX]
final_image = cv2.resize(final_image, (224, 224))
final_image = img_to_array(final_image)
final_image = preprocess_input(final_image)

mask, no_mask = model.predict(np.expand_dims(final_image, axis=0))[0]
print(f'Mask: {mask:0.2f}, No Mask: {no_mask:0.2f}')
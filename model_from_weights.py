from vgg import VGG
import os

model = VGG()
print(model.summary())
weights = './Xml_File/emotion_best_weights.h5'
if os.path.exists(weights):
    print("Loading weight")
    model.load_weights(weights)
    print("Saving model")
    model.save("./Xml_File/emotion_recognition.h5")

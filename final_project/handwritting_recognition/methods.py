import random

from cv2 import cv2
import numpy
import tensorflow
from tensorflow_core.python.keras.models import Sequential

from final_project.handwritting_recognition import constants, file_operation
from final_project.handwritting_recognition.neural_network import NeuralNetwork
from final_project.handwritting_recognition.pygame import globals
import matplotlib.pyplot as plt
import numpy as py
from tensorflow.keras.layers import Dense, Dropout, Conv2D, MaxPooling2D, Flatten


#------------------------------------------------------------------------------------------------------------
#Utility Functions
def convert_int_to_digit_str(num:int, digits:int) -> str:
    """Converts a given integer to a str representation with X digits"""
    num_str:str = str(num)
    excess_zero:int = digits - len(num_str)
    if excess_zero > 0:
        return ("0" * excess_zero) + num_str
    else:
        return num_str

def display_sample(sample:{}, key:str = "random", num:int = -1):
    """Display a sample (for testing and debugging purposes only"""
    if key == 'random':
        key = random.choice(constants.char_list)
    if num == -1:
        num = py.random.randint(0, len(sample[key]))
    
    image = sample[key][num]    #Get Image
    
    #Plot
    plt.imshow(image)
    plt.show()
    
def convert_data_map_to_lists(data_map:{}):
    """Converts the data dictionary to a numpy array of the labels (keys as integers) and a numpy array of the images (used to insert into neural net model)"""
    raw_images:[] = []
    image_labels:[] = []
    for character in data_map:
        for image in data_map[character]:
            raw_images.append(image)
            image_labels.append(character)
    
    return raw_images, numpy.array(image_labels)

def convert_labels_to_one_hot(labels, categories:int):
    """Convert the labels to one-hot format (so that we know what character it is)"""
    new_labels:[] = convert_labels_to_index_correspondence(labels)
    return tensorflow.keras.utils.to_categorical(new_labels, categories)

def convert_labels_to_index_correspondence(labels):
    """Method to convert the characters of the sorted labels to correspond to the index of the char_list in constants"""
    new_labels:[] = []
    i = -1
    current_char = ""
    prev_char = ""
    for a in range(len(labels)):
        current_char = labels[a]
        if current_char != prev_char:
            i+=1
        prev_char = labels[a]
        new_labels.append(str(i))
    return new_labels

def shape_image_for_2d_mlp_input(images, width:int = constants.image_width, height:int = constants.image_height, color_channels:int=3):
    """A method to reshape the images to be ready for neural net input"""
    #Color channels is the amount of possible colors -> grayscale = 1, colored = 3
    
    #Sometimes Keras puts color channels first before width and height, so we need to check for that
    if tensorflow.keras.backend.image_data_format() == 'channels_first':
        reshaped_images = images.reshape(images.shape[0], color_channels, width, height)
    else:
        reshaped_images = images.reshape(images.shape[0], width, height, color_channels)
    
    reshaped_images = reshaped_images.astype('float32')
    reshaped_images /= 255      #Divide by 255 because 255 color scheme, so that the input will be decimals between 0-1
    
    return reshaped_images

def get_input_shape(color_channels:int, width:int = constants.image_width, height:int = constants.image_height):
    """A method to get the input shape of the data to be fed to the neural network"""
    return (color_channels, width, height) if tensorflow.keras.backend.image_data_format() == 'channels_first' else (width, height, color_channels)

def resize_image(image, width:int = constants.image_width, height:int = constants.image_height):
    """Method to resize image, aspect ratio not preserved"""
    image_resized = cv2.resize(image, (width, height), interpolation = cv2.INTER_AREA)
    return image_resized

def resize_images(images, width:int = constants.image_width, height:int = constants.image_height):
    """Method to convert a list of images"""
    for i in range(len(images)):
        image = resize_image(images[i], width, height)
        images[i] = image
    return images

def convert_to_numpy_arr(images, width, height, color_channels):
    """Method for converting the list of images as a numpy array fit for neural network input"""
    array = numpy.zeros((len(images), width, height, color_channels))
    for i in range(len(images)):
        array[i,:,:,:] = images[i]
    
    return array

def get_image_and_label_for_mlp_input(image_map:{}, width:int = constants.image_width, height:int = constants.image_height, color_channels = constants.color_channels):
    """Method to automatically format input image dictionary to be usable for neural network input. Method returns the formatted image as 4D numpy list and the associated labels"""
    images = image_map
    
    image_list, image_labels = convert_data_map_to_lists(images)    #Convert the dictionary to a list, and convert the keys to a list as well that matches the size of the image list
    
    image_list = prepare_images_for_mlp_input(image_list, width, height, color_channels)
    
    image_labels = convert_labels_to_one_hot(image_labels, len(constants.char_list))    #Convert the labels to one-hot format for neural network classification
    
    return image_list, image_labels

def show_prediction_graph(image, prediction:str):
    """Method to display the prediction and the image in the same matplotlib graph"""
    plt.title("Prediction: " + prediction)
    plt.imshow(image, cmap="gray")
    plt.show()

def show_prediction_graph_with_label(image, prediction:str, label:str):
    """Method to display the prediction and the image in the same matplotlib graph. The actual label is also displayed"""
    plt.title("Prediction: " + prediction + " Label: " + label)
    plt.imshow(image, cmap="gray")
    plt.show()
    
def prepare_images_for_mlp_input(images,
                                 width:int = constants.image_width,
                                 height:int = constants.image_height,
                                 color_channels:() = constants.color_channels):
    """Prepares the image for neural network input compatible"""
    images = resize_images(images, width, height)   #Resize the images to a uniform size
    images = convert_to_numpy_arr(images, width, height, color_channels)    #Convert the list to a numpy array
    images = shape_image_for_2d_mlp_input(images, width, height, color_channels)    #Convert image_array according to keras specification (color channels first or last), and normalize the images to be between 0 and 1
    return images

def update_loading_progress(txt:str):
    globals.loading_progress = txt

#------------------------------------------------------------------------------------------------------------
#Neural Network functions
def create_model(input_shape:int, label_count:int):
    """Creates the neural network model"""
    model = Sequential()
    model.add(Conv2D(16, kernel_size=(4, 4), activation='relu', input_shape=input_shape))
    model.add(Conv2D(32, kernel_size=(3, 3),
                     activation='relu'))
    # 64 3x3 kernels
    model.add(Conv2D(64, (3, 3), activation='relu'))
    # Reduce by taking the max of each 2x2 block
    model.add(MaxPooling2D(pool_size=(2, 2)))
    # Dropout to avoid overfitting
    model.add(Dropout(0.25))
    # Flatten the results to one dimension for passing into our final layer
    model.add(Flatten())
    # A hidden layer to learn with
    model.add(Dense(1024, activation='relu'))
    model.add(Dense(512, activation='relu'))
    model.add(Dense(128, activation='relu'))
    model.add(Dense(64, activation='relu'))
    # Another dropout
    model.add(Dropout(0.5))
    # Final categorization 0-9, A-z with softmax
    model.add(Dense(label_count, activation='softmax'))
    
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    
    return model

def save(model, filename):
    """Method to save current neural network model"""
    model.save("models/" + filename + ".h5")
    
def train_neural_network(neural_network:NeuralNetwork, 
                         loaded_model:int,  
                         iterations:int, 
                         width:int = constants.image_width, 
                         height:int = constants.image_height, 
                         color_channels:() = constants.color_channels):
    """
    Trains the selected neural network with default settings
    
    neural_network: the NeuralNetwork class object
    loaded_model: the currently loaded model number
    iterations: amount of neural network model files to create
    width: width of the input image
    height: height of the input image
    color_channels: amount of color channels in the input image
    """
    #Load training and test images
    train_images, train_labels = get_image_and_label_for_mlp_input(file_operation.load_nist_database(1), width, height, color_channels)
    test_images, test_labels = get_image_and_label_for_mlp_input(file_operation.load_nist_database(2, 0.3), width, height, color_channels)
    
    #Train neural network
    for i in range(loaded_model+1, loaded_model + 1 + iterations):
        neural_network.train(train_images, 
                             train_labels, 
                             batch_size=64, 
                             epochs=3, 
                             verbose=1, 
                             validation_data=(test_images, test_labels))
        neural_network.save("model_" + str(i))  #Save the neural network
        neural_network = NeuralNetwork(file_operation.load_training_model("model_" + str(i))) #Load it for next training iteration
        
def make_prediction_from_test_images(neural_network,
                                     width:int = constants.image_width,
                                     height:int = constants.image_height,
                                     color_channels:() = constants.color_channels,
                                     begin:int = 0,
                                     iterations:int = 11):
    """Method to make prediction of the test images"""
    test_images = file_operation.load_test_images("images/test", ".png")
    test_images = prepare_images_for_mlp_input(test_images, width, height, color_channels)
    
    for x in range(begin, begin+iterations):
#         image = test_images[x,:].reshape(1, 128, 128, 3)
#         prediction = neural_network.getModel().predict(image).argmax()
#         predLabel:str = constants.char_list[int(prediction.__str__())]
#     
#         show_prediction_graph(image.reshape(128, 128, 3), predLabel)
        image = test_images[x,:].reshape(1, 128, 128, 3)
        neural_network.predict(image, show_pred_graph=True)
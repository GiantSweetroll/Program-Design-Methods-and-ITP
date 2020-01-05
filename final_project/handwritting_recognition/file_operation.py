import glob

from final_project.handwritting_recognition import methods, constants
import cv2
import tensorflow
import pygame
import io

def load_image(filename):
    image = cv2.imread(filename)      #Read image file
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  #Convert from BGR to RGB Format
    return image

def get_training_images() -> {}:
    """Get dictionary that maps the images for training"""
    #image dataset courtesy of http://www.ee.surrey.ac.uk/CVSSP/demos/chars74k/
    #T. E. de Campos, B. R. Babu and M. Varma. Character recognition in natural images. In Proceedings of the International Conference on Computer Vision Theory and Applications (VISAPP), Lisbon, Portugal, February 2009.
    
    images_to_train:{} = {}
    
    #Start from "good" images
    for i in range(1, 63):  #There are 62 characters, 0-9, a-z, A-Z
        for filename in glob.glob('images/Goodimg/Sample' + methods.convertIntToDigitStr(i, 3) + '/*.png'):
            image = load_image(filename)
            key = constants.char_list[i-1]
            if images_to_train.get(key) != None:    #If key exists in dictionary
                images_to_train[key].append(image)
            else:
                images_to_train[key] = [image]
    
    #Now go to "bad" images
    for i in range(1, 63):  #There are 62 characters, 0-9, a-z, A-Z
        for filename in glob.glob('images/Goodimg/Sample' + methods.convertIntToDigitStr(i, 3) + '/*.png'):
            image = load_image(filename)
            key = constants.char_list[i-1]
            #No need to check for key existence because it will definitely be there after "good" image run
            images_to_train[key].append(image)
    
    return images_to_train
def load_nist_database(dataset_num = 1, data_size:float = 1.):
    """Get dictionary that maps the images for training"""
    #dataset_num = hsf folder number
    #data_size is the amount of data to be loaded, between 0 and 1. 1 means all of the data.
    images:{} = {}
    
    if data_size > 1:
        data_size = 1
    elif data_size < 0:
        data_size = 0
    
    groups:() = ("digit", "upper", "lower")
    for group in groups:        #("const", "digit", "lower", "upper")
        for hexa in constants.ascii_hex:
            files = glob.glob(constants.nist_database_location + 'hsf_' + str(dataset_num) + "/" + group + "/" + hexa + "/*.png")
            for i in range(int(len(files) * data_size)):
                filename = files[i]
                image = image = load_image(filename)
                key = bytearray.fromhex(hexa).decode()
                if images.get(key) != None:    #If key exists in dictionary
                    images[key].append(image)
                else:
                    images[key] = [image]
#                 print('images/nist_database/hsf_' + str(dataset_num) + "/" + group + "/" + hexa + "/" + filename, "loaded.")
    
    return images

def load__training_model(filename:str):
    """A method to load the training CNN model"""
    return tensorflow.keras.models.load_model("models/" + filename + ".h5")

def load_model(path:str):
    """
    Method to laod the desired neural network model
    path: the path of the model file, complete with .h5 extension
    """
    return tensorflow.keras.models.load_model(path)

def load_test_images(directory:str, file_extension:str = ".png"):
    """A method to load the images used to test the neural network or for it to be predicted"""
    images:[] = []
    for file in glob.glob(directory + "/*" + file_extension):
        image = image = load_image(file)
        images.append(image)
    
    return images

def load_hourglass_images() -> []:
    """Method to load the hourglass animation images"""
    hourglass:[] = []
    
    for i in range(10):
        hourglass.append(pygame.image.load("images/hourglass/" + str(i) + ".png"))
    
    return hourglass

def load_loading_hints() -> [str]:
    """Method to load the loading hints and store them in a list"""
    with io.open("pygame/files/loading_hints.txt", encoding="utf8") as file:
        return file.read().splitlines()
    
    return []
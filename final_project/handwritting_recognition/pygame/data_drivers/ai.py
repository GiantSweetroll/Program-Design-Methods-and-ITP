import pygame
from pygame.rect import Rect
import pandas
from final_project.handwritting_recognition import constants, file_operation
from cv2 import line
from final_project.handwritting_recognition.neural_network import NeuralNetwork


class AI():
    """Class to represent the AI characters as an object"""
    
    #Constructor
    def __init__(self, name:str, data_folder:str):
        """
        
        name: name of the AI
        data_folder: Path for the AI files folder
        """
        self.__name:str = name
        self.__image_idle_path:str = data_folder + "/idle.png"
        self.__image_processing_path:str = data_folder + "/processing.png"
        self.__image_idle = pygame.image.load(self.__image_idle_path)
        self.__image_processing = pygame.image.load(self.__image_processing_path)
        self.__image_info_screen_path = data_folder + "/info.png"
        self.__model_struct:str = self.__get_model_structure_as_string(data_folder)
        self.__model_info:[] = self.__get_model_info(data_folder)
        self.__ai_folder:str = data_folder
    
    #Setters and getters
    def get_name(self):
        return self.__name
    
    def get_image_idle(self):
        return self.__image_idle
    
    def get_image_info_screen_path(self):
        return self.__image_info_screen_path
    
    def get_image_processing(self):
        return self.__image_processing
    
    def get_image_idle_rect(self) -> Rect:
        return self.get_image_idle().get_rect()
    
    def get_image_processing_rect(self) -> Rect:
        return self.get_image_processing().get_rect()
    
    def get_model_structure(self):
        return self.__model_struct
    
    def get_folder_path(self):
        return self.__ai_folder
    
    def get_image_idle_path(self):
        return self.__image_idle_path
    
    def get_image_processing_path(self):
        return self.__image_processing_path
    
    #Other methods
    def draw_image_idle(self, screen):
        """
        Method to draw the AI idle image to the screen
        screen: the pygame screen
        """
        screen.blit(self.get_image_idle(), self.get_image_idle_rect())
    def draw_image_processing(self, screen):
        """
        Method to draw the AI processing image to the screen
        screen: the pygame screen
        """
        screen.blit(self.get_image_processing(), self.get_image_processing_rect())
    def __get_model_structure_as_string(self, path):
        """Method to get the model structure as one string from the csv file"""
        data:[] = pandas.read_csv(path + "model_sum.csv")
        #replace '%nbsp%' with ', '
        data["Output Shape"] = data["Output Shape"].str.replace(constants.comma_space_replacer, ", ")
        
        #Convert from pandas dataframe to a 2d list
        ls:[] = []
        for i in range(data.shape[0]):  #Iterate over each row
            ls.append(list(data.iloc[i, :]))
            #Convert to string
            for a in range(len(ls[i])):
                ls[i][a] = ls[i][a].__str__()
        ls.insert(0, ["Layer (type)", "Output Shape", "Param #"])   #insert headers back because it's gone
        
        #generate spacing and add as one string
        final_str:str = ""
        col_counts:[] = [0, 0, 0]
        for row in ls:
            for i in range(len(row)):
                col_counts[i] = len(row[i]) if len(row[i]) > col_counts[i] else col_counts[i]   #Update max length
        col_counts = [x+1 for x in col_counts]  #add 1 to the max length to accomodate space
        for row_num, row in enumerate(ls, start=0):
            sub_str:str = ""
            for i, col in enumerate(row, start=0):
                col += " " * (col_counts[i]-len(col))   #Add spacing by the amount missing
                sub_str += col
            sub_str += "\n" #Add line breaker
            if row_num == 1:    #if second row
                final_str += "=" * (col_counts[0] + col_counts[1] + col_counts[2]) + "\n"       #Add border
            final_str += sub_str
        
        return final_str
    def __get_model_info(self, path:str):
        with open(path + "model_info.txt") as file:
            temp:[] = []
            lines = file.readlines()
            for line in lines:
                temp.append(line)
        return temp
    
    def load_neural_network(self) -> NeuralNetwork:
        """Loads and returns the neural network model associated with the AI"""
        return NeuralNetwork(file_operation.load_model(self.__ai_folder + "/model.h5"))
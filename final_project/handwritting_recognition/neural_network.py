from final_project.handwritting_recognition import constants, methods

class NeuralNetwork():
    
    #Constructor
    def __init__(self, model = None):
        """A class to represent the neural network object"""
        if model == None:
            model = methods.create_model(methods.get_input_shape(constants.color_channels, 
                                                                            constants.image_width, 
                                                                            constants.image_height), 
                                                                            len(constants.char_list))
        self.__model = model
    
    #Setters and Getters
    getModel = lambda self: self.__model
    def setModel(self, model):
        self.__model = model
    #Other Methods
    def train(self, train_images, train_labels, batch_size:int = 100, epochs:int = 10, verbose:int = 2, validation_data = None):
        """train model"""
        return self.getModel().fit(train_images, train_labels, 
                 batch_size = batch_size, 
                 epochs = epochs, 
                 verbose = verbose, 
                 validation_data = validation_data)
    def save(self, filename):
        """save the current state of the model as a file so that it can be loaded in the future"""
        self.getModel().save("models/" + filename + ".h5")
    def evaluate(self, data, labels, verbose = 2):
        """Function to evaluate the accuracy of the model"""
        self.getModel().evaluate(data, labels, verbose = verbose)
    def predict(self, image, show_pred_graph:bool = False) -> str:
        """Method to predict what character is the image, returns the image."""
        #If show_pred_graph = True, it will draw the image and the prediction in a matplotlib graph
        prediction = self.getModel().predict(image)
        for pred in prediction:
            print(pred)
        prediction_argmax = prediction.argmax()
        print("Argmax:", prediction_argmax)
        predLabel:str = constants.char_list[int(prediction_argmax.__str__())]
        
        if show_pred_graph:
            methods.show_prediction_graph(image.reshape(128, 128, 3), predLabel)
            
        return predLabel
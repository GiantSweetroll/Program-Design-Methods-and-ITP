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
    def get_model(self):
        return self.__model
    
    def get_model_summary(self):
        return self.get_model().summary()
#     def get_model_summary_for_export(self):
#         model_sum_raw:[] = []
#         self.get_model().summary(print_fn=lambda x: model_sum_raw.append(x))    #adds each row of the summary to the list
#         
#         #Copy to a new list devoid of the ====== and ___________ borders
#         model_sum_raw_len:int = len(model_sum_raw)
#         model_sum:[] = []
#         for i in range(0, model_sum_raw_len-4, 2):    #-4 because ignore the last 4 elements for now, 2 because the borders exist every 2 rows
#             model_sum.append(model_sum_raw[i])
#         #Copy the last 4 elements, except for the last one (index -1)
#         for i in range(model_sum_raw_len-4, model_sum_raw_len-1):   #Ignore last element because it's a border
#             model_sum.append(model_sum_raw[i])
#         
#         #Remove headers
#         del(model_sum[1])
#         model_sum_len:int = len(model_sum)
#         #Convert all ', ' to a set of characters so that it can be exported to csv
#         for i in range(model_sum_len):
#             model_sum[i] = model_sum[i].replace(", ", constants.comma_space_replacer)
#         #split the layer, output shape, and param fields into its own list
#         core_list:[] = []
#         for i in range(1, model_sum_len-3):
#             temp:[] = model_sum[i].split(")")
#             temp = temp[1:len(temp)]    #Remove first column
#             #remove brackets on first column
#             temp[0] = temp[0].replace("(", "")
#             temp[0] = temp[0].replace(")", "")
#             core_list.append(temp)  #add to list
#         
#         return core_list
            
    def set_model(self, model):
        self.__model = model
        
    #Other Methods
    def train(self, 
              train_images, 
              train_labels, 
              batch_size:int = 100, 
              epochs:int = 10, 
              verbose:int = 2, 
              validation_data = None):
        """
        Train the neural network model
        train_images: the images to train with
        train_labels: the image labels to train with
        batch_size: amount of images to train with at one given time
        epochs: training iterations to do
        verbose: verbose mode. (0=silent, 1=minimal, 2=every batch)
        validation_data: the data used to validate the neural network model
        """
        return self.get_model().fit(train_images, train_labels, 
                                     batch_size = batch_size, 
                                     epochs = epochs, 
                                     verbose = verbose, 
                                     validation_data = validation_data)
        
    def save(self, filename):
        """save the current state of the model as a file so that it can be loaded in the future"""
        self.get_model().save("models/" + filename + ".h5")
        
    def evaluate(self, data, labels, verbose = 2):
        """Function to evaluate the accuracy of the model"""
        self.get_model().evaluate(data, labels, verbose = verbose)
        
    def predict(self, image, show_pred_graph:bool = False) -> str:
        """Method to predict what character is the image, returns the image."""
        #If show_pred_graph = True, it will draw the image and the prediction in a matplotlib graph
        prediction = self.get_model().predict(image)
#         for pred in prediction:
#             print(pred)
        prediction_argmax = prediction.argmax()
#         print("Argmax:", prediction_argmax)
        predLabel:str = constants.char_list[int(prediction_argmax.__str__())]
        
        if show_pred_graph:
            methods.show_prediction_graph(image.reshape(128, 128, 3), predLabel)
            
        return predLabel
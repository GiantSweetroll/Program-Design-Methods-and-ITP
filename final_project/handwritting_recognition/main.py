from final_project.handwritting_recognition import file_operation, methods, \
    constants
from final_project.handwritting_recognition.neural_network import NeuralNetwork
from final_project.handwritting_recognition.pygame.main_game import MainGame
import numpy


# nn = NeuralNetwork(file_operation.load_training_model("model_1"))
# print(nn.get_model_summary())
# nn = NeuralNetwork()
# methods.train_neural_network(nn, 0, 10)
game = MainGame()
# methods.make_prediction_from_test_images(nn, iterations = 12)

# eval_images, eval_labels = methods.get_image_and_label_for_mlp_input(file_operation.load_nist_database(4, 0.5))
# nn.evaluate(eval_images, eval_labels, verbose = 1)
# for _ in range(1000):
#     x = numpy.random.randint(0, len(eval_images)) 
#     image = eval_images[x]
#     prediction = nn.predict(image.reshape(1, constants.image_width, 
#                                                 constants.image_height, 
#                                                 constants.color_channels), False)
#     label = constants.char_list[eval_labels[x].argmax()]
#     if (prediction != label):
#         methods.show_prediction_graph_with_label(image, prediction, label)

# Model evaluation
# for i in range(1, 5):
#     nn = NeuralNetwork(file_operation.load_training_model("model_" + str(i)))
#     print("Model", i)
#     nn.evaluate(eval_images, eval_labels, verbose = 2)
#     print()
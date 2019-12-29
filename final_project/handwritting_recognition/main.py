from final_project.handwritting_recognition import file_operation, methods
from final_project.handwritting_recognition.neural_network import NeuralNetwork
from final_project.handwritting_recognition.pygame.main_game import MainGame


nn = NeuralNetwork(file_operation.load_model("model_11"))
# nn = NeuralNetwork()
# methods.train_neural_network(nn, 10, 4)
# game = MainGame(nn)
# methods.make_prediction_from_test_images(nn, iterations = 12)

eval_images, eval_labels = methods.get_image_and_label_for_mlp_input(file_operation.load_nist_database(3, 0.1))
nn.evaluate(eval_images, eval_labels, verbose = 2)
print("Process done")
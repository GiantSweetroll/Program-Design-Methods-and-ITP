import pygame

from final_project.handwritting_recognition.pygame.data_drivers.ai import AI


char_list:[] = [str(x) for x in range(10)] + [chr(x) for x in range(65, 91)] + [chr(x) for x in range(97, 123)]       #A tuple consisting of the characters 0-9, A-Z, and a-z
ascii_hex:[] = [hex(x)[2:] for x in range(48, 58)] + [hex(x)[2:] for x in range(65, 91)] + [hex(x)[2:] for x in range(97, 123)] #List of ascii characters in hexadecimal

image_width = 128
image_height = 128
color_channels = 3

comma_space_replacer:str = "%nbsp%"

pygame_image_path:str = "pygame/images/"
pygame_test_image_name:str = "pygame_test_xyz.png"
nist_database_location:str = "J:/For Machine Learning/NIST Database/by_field/"

#image locations
path_img_gamemode_welc_console:str = "images/art/gamemode_welcome_console.png"
path_img_gamemode_funhouse_console:str = "images/art/gamemode_funhouse_console.png"
path_img_gamemode_random_chaos_console:str = "images/art/gamemode_random_chaos_console.png"
path_img_ai_info_empty:str = "images/art/empty_ai_info.png"

#AI's
ai_cintra = AI("Cintra-01000010", "ai_files/cintra/")

#Colors
color_red:() = (239, 43, 44)
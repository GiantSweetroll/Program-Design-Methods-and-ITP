from final_project.handwritting_recognition.pygame.data_drivers.ai import AI

mouse_left_pressed:bool = False
panel_index:int = 0
active_ai:AI = None
loading_active:bool = False
show_results:bool = False
loading_progress:str = ""
prediction:str = ""
reset_defaults:bool = False
import pygame
from pygame.event import Event
from pygame.rect import Rect

from final_project.handwritting_recognition import constants
from final_project.handwritting_recognition.pygame import game_functions as gf, \
    globals, game_functions
from final_project.handwritting_recognition.pygame.buttons.ai_button import AIButton
from final_project.handwritting_recognition.pygame.buttons.button import Button
from final_project.handwritting_recognition.pygame.data_drivers.ai import AI
from final_project.handwritting_recognition.pygame.game_panels.panel import Panel
from final_project.handwritting_recognition.pygame.labels.label import Label
from final_project.handwritting_recognition.pygame.misc.ai_info_display import AIInfoDisplay
from final_project.handwritting_recognition.pygame.settings import Settings


class ChooseAIPanel(Panel):
    
    #Constructor
    def __init__(self, screen, settings:Settings):
        super().__init__(screen, settings, background_img_path="choose_ai.png")
        
        #Initialize components
        self.__sub_title_label = Label("Choose your AI")
        self.__choose_button = Button(screen, settings, "Choose")
        self.__ai_buttons:[] = []
        self.__back_button:Button = Button(self.get_screen(), self.get_settings(), "Back", button_color = settings.button_color_red)
        self.__selected_button:AIButton = None
        self.__ai_details_screen:AIInfoDisplay = AIInfoDisplay()
        self.__active_ai_image = None
        
        #Properties
        self.__choose_button.set_enabled(False)
        
        #Configure component placement
        screen_rect:Rect = screen.get_rect()
        #Sub title
        self.__sub_title_label.get_rect().top = screen_rect.top + 20
        self.__sub_title_label.get_rect().centerx = screen_rect.centerx
        #AI Details Display Screen
        details_screen_rect:Rect = self.__ai_details_screen.get_rect()
        details_screen_rect.left = screen_rect.centerx + screen_rect.centerx//3
        details_screen_rect.centery = screen_rect.centery
        #Choose Button
        self.__choose_button.get_rect().centery = self.get_screen().get_rect().bottom - self.__choose_button.get_height()
        self.__choose_button.prep_msg(self.__choose_button.get_text())
        #Back Button
        self.__back_button.get_rect().left = self.get_screen().get_rect().left + 20
        self.__back_button.get_rect().centery = self.get_screen().get_rect().bottom - self.__back_button.get_height()
        self.__back_button.prep_msg(self.__back_button.get_text())
        
        self.__init_ai_buttons()
    
    #Other init methods
    def __init_ai_buttons(self):
        """Method to initialize the AIButton objects and configure their placements"""
        #Append AIs
        padding = 10
        self.__ai_buttons.append(AIButton(self.get_screen(), 
                                          self.get_settings(), 
                                          AI("Cintra - 01000010", "ai_files/cintra/"),
                                          padding = padding))
        self.__ai_buttons.append(AIButton(self.get_screen(), 
                                          self.get_settings(), 
                                          AI("Echo - 01100001", "ai_files/echo/"),
                                          padding = padding))
        self.__ai_buttons.append(AIButton(self.get_screen(), 
                                          self.get_settings(), 
                                          AI("Glados - 01100111", "ai_files/glados/"),
                                          padding = padding))
        self.__ai_buttons.append(AIButton(self.get_screen(), 
                                          self.get_settings(), 
                                          AI("House - 01110101", "ai_files/house/"),
                                          padding = padding))
        self.__ai_buttons.append(AIButton(self.get_screen(), 
                                          self.get_settings(), 
                                          AI("Talos - 01110011", "ai_files/talos/"),
                                          padding = padding))
        
        #Calculate total height and max width
        tot_height:int = 0
        width_max:int = 0
        for button in self.__ai_buttons:
            tot_height += button.get_rect().height       #Add total height of the buttons
            width = button.get_rect().width
            if width > width_max:
                width_max = width
        
        #Update width of all buttons to be the same
        for button in self.__ai_buttons:
            button.get_rect().width = width_max
        
        #Placement configuration
        rect:Rect = Rect(0, 0, self.__ai_buttons[0].get_rect().width, tot_height)
        rect.centery = self.get_screen().get_rect().centery
        rect.centerx = self.get_screen().get_rect().centerx//3
        #Configure first button
        padding:int = 5
        self.__ai_buttons[0].get_rect().top = rect.top - padding
        self.__ai_buttons[0].get_rect().left = rect.left
        self.__ai_buttons[0].prep_msg(self.__ai_buttons[0].get_text())
        #Configure remaining buttons
        for i in range(1, len(self.__ai_buttons)):
            self.__ai_buttons[i].get_rect().top = self.__ai_buttons[i-1].get_rect().bottom + padding
            self.__ai_buttons[i].get_rect().left = rect.left
            self.__ai_buttons[i].prep_msg(self.__ai_buttons[i].get_text())
            self.__ai_buttons[i].prep_surface()
        
    #Setters and Getters
    def get_ai_buttons(self) -> [AIButton]:
        return self.__ai_buttons
    
    def get_ai_details_display_screen(self) -> AIInfoDisplay:
        return self.__ai_details_screen
    
    def get_active_ai_image(self):
        return self.__active_ai_image
    
    def get_back_button(self):
        return self.__back_button
    
    def get_choose_button(self):
        return self.__choose_button
    
    def get_selected_button(self) -> AIButton:
        return self.__selected_button
    
    #Other Methods
    def check_ai_button_selection(self, button:AIButton, mouse_pos:()):
        """Method to check for AI selection, when one of the AI buttons are pressed"""
        if button != None and game_functions.mouse_on_button(button, mouse_pos):                
            self.__selected_button = button
            
            updated_selection:bool = not self.__selected_button.is_selected()
            self.__selected_button.set_selected(updated_selection)
            
            if updated_selection:       #If button is selected, disable every other button
                for button in self.__ai_buttons:
                    if button != self.__selected_button:
                        button.set_selected(False)
            
            self.get_ai_details_display_screen().set_image(self.__selected_button.get_ai().get_image_info_screen_path())
            self.prep_ai_idle_image(self.__selected_button.get_ai().get_image())
            
            self.__choose_button.set_enabled(updated_selection)
            if updated_selection == False:
                self.__selected_button = None
            else:
                self.__selected_button.get_ai().get_image_idle_rect().center = self.get_screen().get_rect().center
    
    def check_back_button(self, mouse_pos:()):
        """Method to check when the back button is pressed"""
        if gf.mouse_on_button(self.__back_button, mouse_pos):
            globals.panel_index -= 1
    
    def check_choose_button(self, mouse_pos:()):
        """Method to check when the choose button is pressed"""
        if gf.mouse_on_button(self.__choose_button, mouse_pos) and self.__choose_button.is_enabled():
            globals.active_ai = self.__selected_button.get_ai()
            globals.panel_index += 1
    
    def prep_ai_idle_image(self, image):
        """Method to prepare the ai idle image for display"""
        self.__active_ai_image = image
        self.__active_ai_image.get_rect().center = self.get_screen().get_rect().center
    
    #Overridden Methods
    def check_events(self, event:Event):
        super().check_events(event)
        x, y = gf.get_mouse_position()
        
        #Check for mouse over actions
        hover:bool = False
        selected_button:AIButton = None
        for ai_button in self.__ai_buttons:
            hover = gf.mouse_in_area(ai_button.get_rect(), (x, y))
            if hover:
                selected_button = ai_button
                break
        if self.__selected_button == None:
            if (hover):
#             self.get_ai_details_display_screen().set_model_sum_text(selected_button.get_ai().get_model_structure())
                self.get_ai_details_display_screen().set_image(selected_button.get_ai().get_image_info_screen_path())
                self.prep_ai_idle_image(selected_button.get_ai().get_image())
                
            else:
                self.get_ai_details_display_screen().set_image(constants.path_img_ai_info_empty)
                self.__active_ai_image = None
#             self.get_ai_details_display_screen().set_model_sum_text("")
        
        #Check for mouse button presses
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:   #1 is left mouse button
                self.check_ai_button_selection(selected_button, (x, y))
                self.check_back_button((x, y))
                self.check_choose_button((x, y))
    
    def draw_components(self):
        super().draw_components()
        
        self.__sub_title_label.draw(self.get_screen())
        
        self.__back_button.draw()
        self.__choose_button.draw()
        
        self.get_ai_details_display_screen().draw(self.get_screen())
        
        if self.__active_ai_image != None:
            rect:Rect = Rect(0, 0, self.__active_ai_image.get_rect().width, self.__active_ai_image.get_rect().height)
            rect.center = self.get_screen().get_rect().center
            self.get_screen().blit(self.__active_ai_image, rect)
        
        for ai_button in self.get_ai_buttons():
            ai_button.draw()
            
        pygame.display.flip()
        
    def reset_defaults(self):
        super().reset_defaults()
        
        #If there's an existing selection, turn it off and set the selection to None
        if (self.__selected_button != None):
            self.__selected_button.set_selected(False)
            self.__selected_button = None
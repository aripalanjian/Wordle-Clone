import pygame


class InputBox:
    """Text and Input Box Creation"""
    #properties
    # text_color = (0,0,0)
    # text_input = ''
    # text_box_coords = (0,0)
    # text_box_w = 125
    # text_size = 20

    def __init__(self, text_color=(0,0,0), text_input='', text_size=20, coords=(0,0), width = 0):
        #Initializes text box properties
        self.text_color = text_color
        self.text_input = text_input
        self.text_size = text_size
        self.coords = coords
        self.text_box_w = width

    def _create_input_box(self):
        #creates input box and returns text and rect to be drawn
        input_text = self.render_text(self.text_input, self.text_size, self.text_color)
        input_text_rect = input_text.get_rect(self.coords ,width = self.text_box_w)
        return input_text, input_text_rect

    @staticmethod
    def render_text(text,size,color):
        '''Reusable render text function.'''
        font = pygame.font.SysFont("comicsans",size)
        text = font.render(text, True, color)
        return text
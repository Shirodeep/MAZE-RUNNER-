import pygame
import cairosvg
import io
from  screeninfo import get_monitors

pygame.init()
WIDTH = 700
HEIGHT = 400
monitorInfo= get_monitors()
for i in monitorInfo:
    WIDTH  = i.width
    HEIGHT  = i.height
WIN = pygame.display.set_mode((WIDTH-100, HEIGHT-100))
pygame.display.set_caption("Practice project using path finding algorithm")
fontSize = 20
fontName = 'freesansbold.ttf'
font = pygame.font.Font(fontName, fontSize)  
clock = pygame.time.Clock()
FPS = 60
AQUA = (0,255,255)           
BANANA = (227,207,87)        
BLACK = (0,0,0)              
AZURE = (240,255,255)        
DARKORCHID = (153,50,204)    
BLUE = (16,78,139)           
GRAY = (161,161,161)         
GREEN = (124,252,0)          
RED = (255, 0, 0)            
WHITE = (255, 255, 255)
WHITESMOKE = (245, 245, 245)
     


class Button:
    def __init__(self, text, text_info, textcolor, color, fontSize, x, y, eventFunc):
        self.textcolor = textcolor
        self.color = color
        self.fontsize = fontSize
        self.y = y
        self.text = text
        self.text_surface, self.text_width, self.text_height = text_info(self.fontsize, self.text, self.textcolor)
        self.x = x
        self.event_func = eventFunc
        self.rect = pygame.Rect(self.x, self.y, self.text_width + 80, self.text_height + 80 )
    
    def makeButton(self, win, event):
        action = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                action = True
        if self.text == "OPTIONS" | self.text == "PLAY" | self.text == "HIGH SCORE":
            self.x = WIDTH / 2 - self.text_width / 2 
            self.rect = pygame.Rect(self.x, self.y, self.text_width + 80, self.text_height + 80 )
        pygame.draw.rect(win, self.color, self.rect)
        win.blit(self.text_surface, (self.x + 40, self.y + 40)) 
        return action

# To define text for implementation
def render_text(additionalFontSize, text, color):
    font = pygame.font.Font(fontName, fontSize + additionalFontSize)
    text_surface = font.render(text, True, color)
    text_width, text_height = font.size(text)
    return text_surface, text_width, text_height

# to implement image in game 
def render_image(image):
    height = image.get_height()
    width = image.get_width()
    return width, height

# to render svg image in game  making png 
def render_svg(svg_path):
    with open(svg_path, 'rb') as svg_file: 
        svg_data = svg_file.read()
    png_data = cairosvg.svg2png(bytestring=svg_data)
    png_block = pygame.image.load(io.BytesIO(png_data))
    png_height = png_block.get_height()
    png_width = png_block.get_width()
    return png_block, png_height, png_width

# to display when game is opened 
def make_first_impression(win):
    count = 0
    text_surface, text_width, text_height = render_text(60, "MAZE RUNNER", BLUE)
    win.blit(text_surface, ((WIDTH - text_width-80) // 2, (HEIGHT - text_height-200 / 2) // 2))
    rect_width = 10
    rect_height = 10
    for i in range(0, 23 * 5 , 1):
        pygame.draw.line(win, BLUE, (50 - 10, HEIGHT - 2 * 100 - 10), (24 * 50 + 10, HEIGHT - 2 * 100 - 10),  4)
        pygame.draw.line(win, BLUE, (50 - 10, HEIGHT - 2 * 100 - 10), (50 -10, HEIGHT - 2 * 100 + rect_height + 10),  4)
        pygame.draw.line(win, BLUE, (50 -10, HEIGHT - 2 * 100 + rect_height + 10), (24 * 50 + 10, HEIGHT - 2 * 100 + rect_height + 10),  4)
        pygame.draw.line(win, BLUE, (24 * 50 + 10, HEIGHT - 2 * 100 - 10), (24 * 50 + 10, HEIGHT - 2 * 100 + rect_height + 10),  4)
        pygame.draw.rect(win, BLUE, (50 + i * 10 , HEIGHT - 2 * 100 , rect_width, rect_height))
        pygame.time.delay(10)
        pygame.display.flip()
    text_surface, text_width, text_height = render_text(0, "PRESS ANY KEY TO CONTINUE...", WHITE)
    win.blit(text_surface, ((WIDTH - text_width-80) // 2 , (HEIGHT - text_height-220)))

def display_levels():
    pass

def play(win):
    win.fill(BLACK)
    pygame.display.flip()

def settings(win):
    win.fill(RED)
    pygame.display.flip()

def highscore(win):
    win.fill(BLUE)
    pygame.display.flip()

# To render after continue at first phage

# Creating buttons for MAINMENU UI
options_button = Button("OPTIONS", render_text, RED, BLUE, 40, 0 , 400 - 100 , settings)
high_score_button = Button("HIGH SCORE", render_text, RED, BLUE, 40, 0 , 600 - 100 , highscore)
play_button = Button("PLAY", render_text, BLUE, RED, 40, 0 , 200 - 100 , play)

# making the platform  
def __play__(win):
    screen = ""
    run = True
    while(run):
        clock.tick(FPS)
        if screen == "show_menu":
            win.fill(BLACK)
            if play_button.makeButton(win, event):
                screen = "play"
            if options_button.makeButton(win, event):
                screen = "options"
            if high_score_button.makeButton(win, event):
                high_score_button.event_func(win)
                screen = "high_score"
        elif screen == "play":
            play_button.event_func(win)    
        elif screen == "options":
            options_button.event_func(win)
        elif high_score_button == "high_score":
            high_score_button.event_func(win)
        elif screen == "options":
            play_button.event_func(win)
        elif screen == "high_score":
            play_button.event_func(win)
        elif screen == "":
            make_first_impression(win)
        for event in  pygame.event.get():
            if event.type == pygame.KEYDOWN:
                screen = "show_menu"

            if event.type == pygame.QUIT:
                run = False
            
                       
        pygame.display.update()
    
#defined main function 
def main(win):
    win.fill((0,0,0))
    __play__(win)

main(WIN)

from pygame import *
import json
import os
window_size = 600, 400
window = display.set_mode(window_size)
display.set_caption("Not finished game")
font.init()
main_font = font.Font(None, 36)
filename = "settings.json"
diffs = ["Easy", "Medium", "Hard"]
current_index = 0
if os.path.exists(filename):
    with open(filename, "r") as f:
        data = json.load(f)
        if data.get("difficulty") in diffs:
            current_index = diffs.index(data["difficulty"])
else:
    with open(filename, "w") as f:
        json.dump({"difficulty": diffs[0]}, f)
class Button:
    def __init__(self, x,y,width,height,color,text,text_color=(0,100,0)):
        self.rect = Rect(x,y,width,height)
        self.color = color
        self.text = text
        self.text_color = text_color
        self.font = font.Font(None, 28)
    def draw(self):
        draw.rect(window, self.color, self.rect)
        text_surf = self.font.render(self.text,True,self.text_color)
        text_rect = text_surf.get_rect(center = self.rect.center)
        window.blit(text_surf, text_rect)
    def is_clicked(self, event):
        return event.type == MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)
play_button = Button(200,80,200,50,(200,20,200),"Play")
settings_button = Button(200,160,200,50,(20,200,200),"Difficulty")
exit_button = Button(200,240,200,50,(200,200,20), "Leave")
running = True
while running:
    window.fill((255,255,25))
    diff_text = main_font.render("Difficulty: "+ diffs[current_index], True, (0,234,0))
    window.blit(diff_text, (180, 20))
    play_button.draw()
    settings_button.draw()
    exit_button.draw()
    display.update()

    for e in event.get():
        if e.type == QUIT:
            running = False
        if play_button.is_clicked(e):
            print("Game starts with difficulty: ", diffs[current_index])
        if settings_button.is_clicked(e):
            current_index = (current_index +1)% len(diffs)
            with open(filename, "w") as f:
                json.dump({"difficulty": diffs[current_index]}, f)
        if exit_button.is_clicked(e):
            print("Leaving...")
            running = False
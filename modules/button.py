import customtkinter as ctk
import modules.screen_app as m_app
import modules.find_path as m_path
from PIL import Image
import modules.button_functions as bt

def create_button(master, image, width = 50, height = 50, command = None):
    button = ctk.CTkButton(
                        master = master,
                        width = width,
                        height = height,
                        image = image,
                        text = "",
                        fg_color= "transparent",
                        bg_color= "transparent",
                        hover = False,
                        command = command
                        
    )
    return button

button_width = 50
button_height = 50

button_add = create_button(master = m_app.main_app, 
                            image = ctk.CTkImage(light_image=Image.open(m_path.find_path("images\\ButtonADD.png")),
                            size = (button_width, button_height)),
                            command = bt.add_song)
button_add.place(x=40, y=440)

button_stop = create_button(master = m_app.main_app, 
                            image = ctk.CTkImage(light_image=Image.open(m_path.find_path("images\\Button STOP.png")), 
                            size = (button_width + 100, button_height)), 
                            width = 150,
                            command = bt.stop)
button_stop.place(x=280, y=340)

button_sound_plus = create_button(master = m_app.main_app, 
                            image = ctk.CTkImage(light_image=Image.open(m_path.find_path("images\\Button SOUND +.png")), 
                            size = (button_width, button_height)),
                            command = bt.volume_add)
button_sound_plus.place(x=280, y=440)

button_sound_minus = create_button(master = m_app.main_app, 
                            image = ctk.CTkImage(light_image=Image.open(m_path.find_path("images\\Button SOUND -.png")), 
                            size = (button_width, button_height)),
                            command = bt.volume_minus)
button_sound_minus.place(x=380, y=440)

button_play = create_button(master = m_app.main_app, 
                            image = ctk.CTkImage(light_image=Image.open(m_path.find_path("images\\Button PLAY.png")), 
                            size = (button_width + 100, button_height)), 
                            width = 150, 
                            command=bt.playsong)
button_play.place(x=280, y=40)

button_pause = create_button(master = m_app.main_app, 
                            image = ctk.CTkImage(light_image=Image.open(m_path.find_path("images\\Button PAUSE.png")), 
                            size = (button_width + 100, button_height)), 
                            width = 150,
                            command = bt.pause)
button_pause.place(x=280, y=240)

button_mix = create_button(master = m_app.main_app,
                            image = ctk.CTkImage(light_image=Image.open(m_path.find_path("images\\Button MIX.png")), 
                            size = (button_width, button_height)),
                            command = bt.mix)
button_mix.place(x=200, y=440)

button_delete = create_button(master = m_app.main_app,
                            image = ctk.CTkImage(light_image=Image.open(m_path.find_path("images\\Button Delete.png")), 
                            size = (button_width, button_height)),
                            command = bt.delete)
button_delete.place(x=120, y=440)

button_back = create_button(master = m_app.main_app, 
                            image = ctk.CTkImage(light_image=Image.open(m_path.find_path("images\\ButtonBACK.png")), 
                            size = (button_width, button_height)),
                            command = bt.previous_track)
button_back.place(x=380, y=140)

button_forward = create_button(master = m_app.main_app, 
                            image = ctk.CTkImage(light_image=Image.open(m_path.find_path("images\\Button FORWARD.png")), 
                            size = (button_width, button_height)),
                            command = bt.next_track)
button_forward.place(x=280, y=140)

button_close = create_button(master = m_app.main_app, 
                            image = ctk.CTkImage(light_image=Image.open("images\\Button CLOSE.png"), 
                            size = (button_width, button_height)),
                            command = bt.close)
button_close.place(x = 440, y = 0)
import customtkinter
from PIL import Image, ImageTk
import os

import keras_cv
from tensorflow import keras
import matplotlib.pyplot as plt

customtkinter.set_appearance_mode("dark") 
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("532x622")
app.title("CustomTkinter simple_example.py")

model = keras_cv.models.StableDiffusion(img_width=500, img_height=500)



def generate():
	img = model.text_to_image(prompt.get(), batch_size=1,  # How many images to generate at once
    num_steps=50,  # Number of iterations (controls image quality)
    seed=123)
	Image.fromarray(img[0]).save("generated.png")
	ph = ImageTk.PhotoImage(Image.fromarray(img[0]))
	home_image_main.configure(image=ph)
	#Loading previous image
	#img = Image.open("./generated.png")
	#ph= ImageTk.PhotoImage(img)
	#home_image_main.configure(image=ph)



app = customtkinter.CTkFrame(master=app)
app.pack(pady=20, padx=60, fill="both", expand=True)

prompt = customtkinter.CTkEntry(master=app, placeholder_text="e.g. astronaut riding a horse", font=("Arial",20), fg_color="grey", width=512)
prompt.pack(pady=10, padx=10)

trigger = customtkinter.CTkButton(master=app, font=("Arial",20), text_color="white", 
	fg_color="blue", command=generate)
trigger.pack(pady=10, padx=10)
trigger.configure(text="Generate")


home_image_main = customtkinter.CTkLabel(master=app,text="")
home_image_main.pack(pady=20, padx=30)




app.mainloop()

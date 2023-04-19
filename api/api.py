from PIL import Image, ImageTk
import os

import keras_cv
from tensorflow import keras
import matplotlib.pyplot as plt


from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from io import BytesIO
import base64

app = FastAPI()
app.add_middleware(
	CORSMiddleware,
	allow_credentials=True,
	allow_origins=["*"],
	allow_methods=["*"],
	allow_headers=["*"]
)



model = keras_cv.models.StableDiffusion(img_width=500, img_height=500)
@app.get("/")
def generate(prompt: str):
	img = model.text_to_image(prompt, batch_size=1,  # How many images to generate at once
    num_steps=20,  # Number of iterations (controls image quality)
    seed=123)
	Image.fromarray(img[0]).save("generated.png")
	#return {"out": "hello World"}
	buffer = BytesIO()
	Image.fromarray(img[0]).save(buffer, format="PNG")
	imgstr=base64.b64encode(buffer.getvalue())
	return Response(content=imgstr, media_type="image/png")
	#ph = ImageTk.PhotoImage(Image.fromarray(img[0]))
	#home_image_main.configure(image=ph)


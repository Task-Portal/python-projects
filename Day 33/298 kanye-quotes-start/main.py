from datetime import datetime
from tkinter import *
import requests

#
# def get_quote():
#     response= requests.get("https://api.kanye.rest")
#     response.raise_for_status()
#     canvas.itemconfig(quote_text, text=f"{response.json()['quote']}")
#
#
# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)
#
# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="background.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
# canvas.grid(row=0, column=0)
#
# kanye_img = PhotoImage(file="kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
# kanye_button.grid(row=1, column=0)
#
#
#
# window.mainloop()

MY_LAT = "50.450100"
MY_LONG = "30.523399"
paramenters = {
    "lat":MY_LAT,
    "lng": MY_LONG,
    "formatted":0

}

response = requests.get("https://api.sunrise-sunset.org/json", params=paramenters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise)
time_now = datetime.now()
print(time_now)


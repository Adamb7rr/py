import customtkinter as ctk

def button_callback():
    print("Button clicked!")
    label.configure(text="You clicked the button!")

app = ctk.CTk()
app.geometry("400x240")
app.title("My Python App")

label = ctk.CTkLabel(app, text="This is 100% Python", fg_color="transparent")
label.pack(pady=20)

button = ctk.CTkButton(app, text="Click Me", command=button_callback)
button.pack(pady=20)

app.mainloop()
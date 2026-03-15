import customtkinter as ctk
from PIL import Image
from src.controllers.Controller import Controller

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        # Window Configurations
        self.geometry("600x500")

        # Controller creation
        self.controller = Controller("hello.csv")

        self.label = ctk.CTkLabel(self, text="Hello!")
        self.label.pack()

        # Camera frame creation
        self.image = ctk.CTkLabel(self, text="", width=300, height=200)
        self.image.pack()
        self.update_image()


        # Label value entry
        self.label_entry = ctk.CTkEntry(self, placeholder_text="Enter image label")
        self.label_entry.pack()

        # Save value into csv button
        def save_into_csv():
            self.controller.addRow(label=self.label_entry.get())

        self.save_into_csv_button = ctk.CTkButton(self, text="Save into CSV", command=save_into_csv)
        self.save_into_csv_button.pack()

    def update_image(self):
            self.pil_image = Image.fromarray(self.controller.showCam())

            self.ctk_image = ctk.CTkImage(self.pil_image, size=(300,200))
            self.image.configure(image=self.ctk_image)
            
            self.after(33, self.update_image)
    
app = App()
app.mainloop()


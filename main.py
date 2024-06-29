from AppOpener import open
import customtkinter

application_list = ["spotify", "advantagescope wpilib"]
#open("advantagescope wpilib")

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue") 
app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("800x580")
lst=[]
for i in range(5):
    lst.append(customtkinter.CTkButton(master=app, text="CTkButton", command=None,corner_radius=20).grid(row=0, column=i))


app.mainloop()
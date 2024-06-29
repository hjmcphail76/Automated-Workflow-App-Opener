from AppOpener import open
import customtkinter


def open_programming_Workflow():
    open("wpilib advantagescope",match_closest=True)
    open("prusaslicer")
    open("google chrome")
    open("spotify")
    app.destroy()

def open_3d_printing_Workflow():
    open("prusaslicer")
    open("google chrome")
    open("spotify")
    app.destroy()

function_lst = [open_programming_Workflow, open_3d_printing_Workflow]
button_names_lst=["Programming Workflow", "3D Printing Workflow"]
button_lst = []



customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")
app = customtkinter.CTk()
app.geometry("800x580")


for i in range(len(button_names_lst)):
    button_lst.append(
        customtkinter.CTkButton(
                                master=app, 
                                text=button_names_lst[i],
                                command=function_lst[i],corner_radius=20,
                                border_color="black",
                                border_width=3
                                )
                                    .pack(side="left", 
                                        fill="both", 
                                        expand=True))


app.mainloop()
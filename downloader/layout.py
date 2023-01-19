import customtkinter as ctk
from video import Video

finish_label = ""
def click_event(var, url_name):
    global finish_label
    vid = Video(url_name)
    finish_label.configure(text=vid.info())
    if (var.get()==0):
        vid.download(0)
        finish_label.configure(text= "Dowlnloaded audio only to current folder")
    elif(var.get()==1):
        vid.download(1)
        finish_label.configure(text="Dowlnloaded low res video to current folder")
    elif (var.get()==2):
        vid.download(2)
        finish_label.configure(text="Dowlnloaded high res video to current folder")

def layout():
    global finish_label
    ctk.set_appearance_mode("system")

    root = ctk.CTk()
    var = ctk.IntVar()
    url_name = ""
    root.title("YT downloader")
    root.geometry("500x500")

    frame = ctk.CTkFrame(master=root)
    frame.pack(pady="5", padx="5", fill="both", expand=True)

    url_label = ctk.CTkLabel(master=frame, text="URL:")
    url_text = ctk.CTkEntry(master=frame)

    radio_audio = ctk.CTkRadioButton(master=frame, text="Only audio",variable=var, value=0)
    radio_low_res = ctk.CTkRadioButton(master=frame, text="Low resolution", variable=var, value=1)
    radio_high_res = ctk.CTkRadioButton(master=frame, text="High resolution", variable=var, value=2)

    action_button = ctk.CTkButton(master=frame, text="Download", command=lambda: click_event(var, url_text.get()))

    finish_label = ctk.CTkLabel(master=frame, text=":)")

    url_label.pack(padx="5", pady="5")
    url_text.pack(padx="5", pady="5")
    radio_audio.pack(padx="5", pady="5")
    radio_low_res.pack(padx="5", pady="5")
    radio_high_res.pack(padx="5", pady="5")
    action_button.pack(padx="5", pady="5")
    finish_label.pack()
    root.mainloop()
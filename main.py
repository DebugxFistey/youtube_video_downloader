from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from tkinter.filedialog import askdirectory
from tkinter import messagebox
import time
from pytube import YouTube


class YoutubeDownloader():

        # ========== Video Path ===================
        def select_v_path(self):
                self.location = askdirectory()

                if self.video_path.get() != "":
                        self.video_path.delete(0,END)
                        self.video_path.insert(END,self.location)
                else:
                        self.video_path.insert(END,self.location)
                
        
        
        # =======================  Downloading Video ====================
        def download_video(self):
                if self.video_url.get() == "":
                        messagebox.showerror("Error","Please Paste Video URL")
                elif 'https://' not in self.video_url.get():
                         messagebox.showerror("Error","Wrong Video Url")
                elif self.video_path.get() == "":
                        messagebox.showerror("Error","Please provide Path")
                else:
                        try:
                            self.url = self.video_url.get()
                            self.path = self.video_path.get()
                            self.video = YouTube(self.url).streams
                            self.stream = self.video.filter(
                            file_extension="mp4", res="720p", 
                            only_audio=False  
                            ).first()
                            messagebox.showinfo("Notification","You will be notify if video downloaded")

                            self.root = tk.Tk()
                            self.root.geometry('300x150')
                            self.root.maxsize(300,150)
                            self.root.minsize(300,150)
                            self.root.title('Video Dowload Successfully')
                            self.root['bg'] = "white"

                            
                            self.start_downloading = Label(self.root,text="Video downloaded successfully .....",fg="red",font=('verdana',10,'bold'),bg="white")
                            self.start_downloading.place(x=40,y=10)

                            self.stream.download(output_path = self.path,filename=None)
                            

                            self.root.mainloop()

                                
                        except:
                            time.sleep(10)
                            messagebox.showerror("Error","Unable to Download Video | Something went wrong !!")

                # ========================= End ==============================




        # ==============================  Main Window ========================
        def __init__(self):
                self.root = tk.Tk()
                self.root.geometry('500x270')
                self.root.maxsize(500,350)
                self.root.minsize(500,350)
                self.root['bg']="white"
                self.root.title('Youtube Video Downloader')
                
                self.l1 = Label(self.root,text="DebugxFistey Youtube Video Downloader",font=('verdana',15,'bold'),bg="white",fg="red")
                self.l1.place(x=50,y=5)

                self.yt_icon = ImageTk.PhotoImage(Image.open('1.png'))
                self.logo = Label(self.root,image=self.yt_icon,bg="white")
                self.logo.place(x=220,y=50)

                
                # ==================== Video ============================

                self.frame1 = LabelFrame(self.root,text="Download Video",width=480,height=180,font=('verdana',10,'bold'),bg="white",fg="red",borderwidth=5,relief=SUNKEN,highlightcolor="red",highlightbackground="red")
                self.frame1.place(x=10,y=140) 

                self.v_url = Label(self.frame1,text="Paste url Here ...",font=('verdana',10,'bold'),bg="white")
                self.v_url.place(x=20,y=2)

                self.video_url = Entry(self.frame1,width=60,relief=SUNKEN,borderwidth=2,bg="green",fg="white")
                self.video_url.place(x=10,y=30)

                self.v_path = Label(self.frame1,text="Select Path",font=('verdana',10,'bold'),bg="white")
                self.v_path.place(x=10,y=60)

                self.video_path = Entry(self.frame1,width=50,relief=SUNKEN,borderwidth=2,bg="green",fg="white")
                self.video_path.place(x=10,y=90)

                self.file = Button(self.frame1,text="Browser",font=('verdana',8,'bold'),relief=RAISED,bg="white",command=self.select_v_path)
                self.file.place(x=300,y=88)

                self.download_video = Button(self.frame1,text="Download",font=('verdana',9,'bold'),relief=RAISED,bg="white",borderwidth=4,command=self.download_video)
                self.download_video.place(x=40,y=125)


                self.root.mainloop()


if __name__ == '__main__':
        YoutubeDownloader()
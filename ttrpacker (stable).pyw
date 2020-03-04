 
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox
import time
import os
import shutil
import subprocess

"""
class newPackPrompt(object):
    def __init__(self,master):
        top=self.top=Toplevel(master)
        self.l=Label(top,text="Please Enter the name of your pack!")
        self.l.pack(padx=50)
        self.e=Entry(top)
        self.e.pack()
        self.b=Button(top,text='Create',command=self.cleanup)
        self.b.pack(pady=10,padx=5)
        self.b=Button(top,text='Cancel',command=self.purge)
        self.b.pack(pady=10,padx=5)
        self.x = StringVar()
    def purge(self):
        self.top.destroy()
    def cleanup(self):
        #while 1:
        self.value=self.e.get()
        self.newp = self.value
        if os.path.isdir(os.getcwd()+"/"+self.newp):
            messagebox.showinfo(title="Matching directory", message="That pack already exists!")
        else:
            os.makedirs(os.getcwd()+"/"+self.newp)
            self.x.set(self.newp)
            self.top.destroy()
"""


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.lbitems = []
        self.newf = StringVar()
        self.counter = 0
        self.track = StringVar()
        self.media = ""
        self.factory = StringVar()
        self.sub = StringVar()
        self.userpath = StringVar()
        self.osub = StringVar()
        self.multifypath = StringVar()
        self.toontown = StringVar()
        self.filep = StringVar()
        self.infop = StringVar()
        self.filep.set("////")
        self.userpath.set("none")
        self.infop.set("Waiting...")
        #self.multifypath.set("none")
        self.toontown.set("none")
        #program setup Donald's Dream Land", "Sellbot Hq", "Cashbot Hq", "Lawbot Hq", "Bossbot Hq", "Toonfest", "Building", "Battle"
        
        self.library = {
                "Toontown Central":{
                        "unit":"Playground",
                        "base":"",
                        "Playground":"phase_4/audio/bgm/TC_nbrhood",
                        "Street":"phase_3.5/audio/bgm/TC_SZ",
                        "Shop":"phase_3.5/audio/bgm/TC_SZ_activity"
                    },
                "Speedway":{
                        "unit":"Playground",
                        "base":"phase_6",
                        "Playground":"/audio/bgm/GS_SZ",
                        "Street":"/audio/bgm/GS_SZ",
                        "Shop":"/audio/bgm/GS_KartShop"
                        
                    },
                "Donald's Dock":{
                        "unit":"Playground",
                        "base":"phase_6",
                        "Playground":"/audio/bgm/DD_nbrhood",
                        "Street":"/audio/bgm/DD_SZ",
                        "Shop":"/audio/bgm/DD_SZ_activity"
                    },
                "Daisy's Gardens":{
                        "unit":"Playground",
                        "base":"phase_8",
                        "Playground":"/audio/bgm/DG_nbrhood",
                        "Street":"/audio/bgm/DG_SZ",
                        "Shop":"/audio/bgm/DG_SZ_activity"
                    },
                "Minnies Melody Land":{
                        "unit":"Playground",
                        "base":"phase_6",
                        "Playground":"/audio/bgm/MM_nbrhood",
                        "Street":"/audio/bgm/MM_SZ",
                        "Shop":"/audio/bgm/MM_SZ_activity"
                    },
                "The Brrrgh":{
                        "unit":"Playground",
                        "base":"phase_8",
                        "Playground":"/audio/bgm/TB_nbrhood",
                        "Street":"/audio/bgm/TB_SZ",
                        "Shop":"/audio/bgm/TB_SZ_activity"
                    },
                "Donald's Dream Land":{
                        "unit":"Playground",
                        "base":"phase_8",
                        "Playground":"/audio/bgm/DL_nbrhood",
                        "Street":"/audio/bgm/DL_SZ",
                        "Shop":"/audio/bgm/DL_SZ_activity"
                    },
                "Sellbot Hq":{
                        "unit":"coghq",
                        "base":"phase_9",
                        "HQ Theme":"audio/bgm/encntr_suit_HQ_nbrhood",
                        "Cog Facility":"audio/bgm/CHQ_FACT_bg"
                    },
                "Cashbot Hq":{
                        "unit":"coghq",
                        "base":"phase_10",
                        "HQ Theme":"audio/bgm/CBHQ_LOBBY_bg",
                        "Cog Facility":"audio/bgm/CHQ_MINT_bg"
                    },
                "Lawbot Hq":{
                        "unit":"coghq",
                        "base":"phase_11",
                        "HQ Theme":"audio/bgm/LB_courtyard",
                        "Cog Facility":"audio/bgm/LB_office"
                    },
                "Bossbot Hq":{
                        "unit":"coghq",
                        "base":"phase_12",
                        "HQ Theme":"audio/bgm/Bossbot_Entry_v1",
                        "Cog Facility":"audio/bgm/Bossbot_Factory_v1"
                    },
                "Toonfest":{
                        "unit":"Playground",
                        "base":"phase_XXXXXXXX",
                        "Playground":"XXXXXXXX",
                        "Street":"XXXXXXXXX",
                        "Shop":"XXXXXXXXX"
                    },
                "- Other -":{
                        "unit":"other",
                        "Elevator":"phase_7/audio/bgm/tt_elevator",
                        "Building Battle":"phase_7/audio/bgm/encntr_general_bg_indoor",
                        "Building Idle":"phase_7/audio/bgm/encntr_toon_winning_indoor",
                        "Building Top":"phase_7/audio/bgm/encntr_suit_winning_indoor",
                        "Street Battle":"phase_3.5/audio/bgm/encntr_general_bg",
                        "Cog Hq Battle":"phase_9/audio/bgm/encntr_suit_winning",
                        "Vp Running":"phase_9/audio/bgm/encntr_toon_winning",
                        "Toon Victory":"phase_9/audio/bgm/encntr_hall_of_fame",
                        "Speedway Race":"phase_6/audio/bgm/GS_Race_CC",
                        "Rural Race":"phase_6/audio/bgm/GS_Race_RR",
                        "Urban Race":"phase_6/audio/bgm/GS_Race_SS",
                        "Bossbot Theme 2":"phase_12/audio/bgm/Bossbot_Entry_v2",
                        "Bossbot Theme 3":"phase_12/audio/bgm/Bossbot_Entry_v3",
                        "Bossbot Factory Last Floor":"phase_12/audio/bgm/Bossbot_Factory_Finale",
                        "Golf Zone":"phase_6/audio/bgm/GZ_SZ",
                        "Golf Course":"phase_6/audio/bgm/GZ_PlayGolf",
                    },
            }
        """
        "Elevator", "Building Battle", "Building Idle", "Building Top",
        "Street Battle", "Cog Hq Battle", "Vp Running", "Toon Victory",
        "Speedway Race", "Rural Race", "Urban Race", "Bossbot Theme 2",
        "Bossbot Theme 3", "Bossbot Factory Last Floor"
        
        """
        self.master = master
        self.master.title("TTR Sountrack Editor")
        
        self.nb = ttk.Notebook(master)
        self.nb.pack(expand=1, fill="both")
        
        #setup page
        
        page1 = ttk.Frame(self.nb)
        self.nb.add(page1, text='File Manager')
        
        #racing page
        
        page2 = ttk.Frame(self.nb)
        self.nb.add(page2, text='Edit Music')
        
        page3 = ttk.Frame(self.nb)
        self.nb.add(page3, text='Options')
        
        #Options Tab
        self.inphasef = StringVar()
        self.inphasef.set("phase_3")
        
        self.phases = OptionMenu(page3, self.inphasef, "phase_3","phase_3.5","phase_4","phase_5","phase_5.5","phase_6","phase_7","phase_8","phase_9","phase_10","phase_11","phase_12","phase_13")
        self.phases.place(x=5, y=50)
        
        self.spack = Button(page3, text= "Pack", command=self.singlePack)
        self.spack.place(x=5, y=85)
        self.sunpack = Button(page3, text= "Unpack", command=self.singleUnpack)
        self.sunpack.place(x=45, y=85)
        
        self.findm = Button(page3, text= "Edit Multify.exe Path", command=self.find_multify)
        self.findm.place(x=5, y=115)
        
        self.sunpack["state"] = "disabled"
        self.spack["state"] = "disabled"
        
        self.no_alerts = IntVar()
        self.optionone = Checkbutton(page3, text="Disable Song Overwrite Alert", variable=self.no_alerts)
        self.optionone.place(x=5,y=5)
        
        self.resourceunpack = IntVar()
        self.optionthree = Checkbutton(page3, text="Unpack From Resources", variable=self.resourceunpack)
        self.optionthree.place(x=185,y=5)
        
        self.no_bound = IntVar()
        self.optiontwo = Checkbutton(page3, text="Extra Output", variable=self.no_bound)
        self.optiontwo.place(x=5,y=25)
        
        
        #Edit Tab
        self.info = Label(page2, text = "Toontown Music File ")
        self.info.place(x=5, y=5)
        
        self.info = Label(page2, text = "Your Music File ")
        self.info.place(x=5, y=160)
        
        self.track.set("Toontown Central")
        self.zone = OptionMenu(page2, self.track, "Toontown Central", "Donald's Dock", "Speedway", "Daisy's Gardens", "Minnies Melody Land", "The Brrrgh", "Donald's Dream Land", "Sellbot Hq", "Cashbot Hq", "Lawbot Hq", "Bossbot Hq", "Toonfest","- Other -")
        self.zone.place(x=5, y=30)
        
        self.sub.set("Playground")
        self.szone = OptionMenu(page2, self.sub, "Playground", "Street", "Shop")
        self.szone.place(x=5, y=60)
        
        self.factory.set("HQ Theme")
        self.fzone = OptionMenu(page2, self.factory, "HQ Theme", "Cog Facility")
        self.fzone.place(x=5, y=90)
        
        self.osub.set("Elevator")
        self.other = OptionMenu(page2, self.osub, "Elevator", "Building Battle", "Building Idle", "Building Top", "Street Battle", "Cog Hq Battle", "Vp Running", "Toon Victory", "Speedway Race", "Rural Race", "Urban Race", "Bossbot Theme 2", "Bossbot Theme 3", "Bossbot Factory Last Floor", "Golf Zone", "Golf Course" )
        self.other.place(x=5, y=120)
        
        self.fpath = Label(page2, textvariable = self.filep)
        self.fpath.place(x=10, y=250)
        
        self.openf = Label(page2, textvariable=self.userpath)
        self.openf.place(x=10, y=230)
        
        self.openf = Button(page2, text= "Select Music", command=self.openfile)
        self.openf.place(x=10, y=180)
        self.openf["state"] = "disabled"
        
        self.replacet = Button(page2, text= "Replace Track", command=self.REPLACE)
        self.replacet.place(x=190, y=210)
        
        self.clearm = Button(page2, text= "Clear Your Music", command=self.clearpath)
        self.clearm.place(x=280, y=210)
        
        self.musicout = Text(page2, height=12, width=26)
        self.musicout.place(x=180, y=4)
        self.musicout.configure(state="disabled")
        
        
        #Setup Tab
        
        
        
        self.request = Label(page1, text = "Make sure this file is in an EMPTY folder!")
        self.request.place(x=6, y=0)
        
        self.vers = Label(page1, text = "Requires panda3d 1.10.4.1, or current version of toontowns panda3d")
        self.vers.place(x=6, y=15)
        
        
        self.efile = Button(page1, text= "Edit Selected Pack", command=self.packOptionWindow)
        self.efile.place(x=110, y=33)
        self.efile["state"] = "disabled"
        
        self.newp = Button(page1, text= "New Music Pack", command=self.new_pack)
        self.newp.place(x=10, y=33)
        
        self.packf = Button(page1, text= "Apply", command=self.pack_mf)
        #self.packf.place(x=115, y=33)
        #self.packf["state"] = "disabled" 
        
        self.packrestore = Button(page1, text= "Restore", command=self.unpack_resources)
        #self.packrestore.place(x=161, y=33)
        #self.packrestore["state"] = "disabled"
        
        self.exportf= Button(page1, text= "Export to toontown", command=self.export)
        #self.exportf.place(x=215, y=33)
        #self.exportf["state"] = "disabled"
        
        #self.TESTB= Button(page1, text= "TEST B", command=self.TEST)
        #self.TESTB.place(x=215, y=10)
        
        self.upackf = Button(page1, text= "Unpack", command=self.unpack_mf)
        #self.upackf.place(x=60, y=33)
        #self.upackf["state"] = "disabled"
        
        self.output = Text(page1, height=10, width=23)
        self.output.place(x=198, y=65)
        self.output.configure(state="disabled")
        
        #self.progress = IntVar()
        self.progressone = ttk.Progressbar(page1, orient="horizontal", length=373, mode="determinate")
        self.progressone.place(x=10,y=240)
        self.progressone["maximum"]=13
        
        self.working = Label(page1, textvariable = self.infop)
        self.working.place(x=15, y=263)
        self.working.config(font=("Courier",6))
        
        self.packs = Listbox(page1, width=30)
        self.packs.place(x = 10, y = 65)
        self.quick_list()
        
        root.update()
        self.add_one()
        self.fts()
        
    def packOptionWindow(self):
        top=self.top=Toplevel(self.master)
        
        self.l=Label(top,text=" ")
        self.l.pack(padx=170,pady=3)
        
        self.b=Button(top,text='Edit This Packs Music',command=self.set_current_path)
        #self.b.place(x=3,y=10)
        
        self.b=Button(top,text='Convert To Mf',command=self.pack_mf)
        self.b.place(x=3,y=0)
        
        self.b=Button(top,text='Export To Toontown',command=self.export)
        self.b.place(x=89,y=0)
        
        self.b=Button(top,text='Delete This Pack',command=self.REMOVE)
        self.b.place(x=206,y=0)
        
        self.b=Button(top,text='Cancel',command=self.purge)
        self.b.place(x=301,y=0)
       
        
        
    def entryWindow(self):
        top=self.top=Toplevel(self.master)
        
        self.l=Label(top,text=" ")
        self.l.pack(padx=110,pady=40)
        
        self.l=Label(top,text="Please Enter the name of your pack.")
        self.l.place(x=8,y=5)
        self.e=Entry(top)
        self.e.place(x=10,y=30)
        self.b=Button(top,text='Create New',command=self.cleanup)
        self.b.place(x=10,y=60)
        
        self.b=Button(top,text='Import',command=self.im)
        self.b.place(x=85,y=60)
        
        self.b=Button(top,text='Cancel',command=self.purge)
        self.b.place(x=135,y=60)
        self.x = StringVar()
    def purge(self):
        self.top.destroy()
        
    def im(self):
        #while 1:
        self.value=self.e.get()
        self.p = self.value
        if os.path.isdir(os.getcwd()+"/"+self.p):
            messagebox.showinfo(title="Matching directory", message="That pack already exists!")
        else:
            chars = set(' /\:-][}{|!@#$%^&*=`~<>?.,')
            if any((c in chars) for c in self.p):
                messagebox.showinfo(title="Error", message="Characters entered may not work, please rename!")
                return 0
            os.makedirs(os.getcwd()+"/"+self.p)
            messagebox.showinfo(title="File", message="Select the folder containing the mf files")
            f =  fd.askdirectory()
            self.quick_list()
            self.top.destroy()
            self.fillimport(self.p, f)
     
        
    def cleanup(self):
        #while 1:
        self.value=self.e.get()
        self.p = self.value
        if os.path.isdir(os.getcwd()+"/"+self.p):
            messagebox.showinfo(title="Matching directory", message="That pack already exists!")
        else:
            chars = set(' /\:-][}{|!@#$%^&*=`~<>?.,')
            if any((c in chars) for c in self.p):
                messagebox.showinfo(title="Error", message="Characters entered may not work, please rename!")
                return 0
            os.makedirs(os.getcwd()+"/"+self.p)
            self.quick_list()
            self.top.destroy()
            self.fill(self.p)
    
    
    def fillimport(self, value, filepath):
        #self.newf.set(value)
        print(value)
        os.makedirs(os.getcwd()+"/"+value+"/resources")
        os.makedirs(os.getcwd()+"/"+value+"/rbuild")
        self.find_resource()
        #-> move to resouce folder goes here
        self.load_mf(value, filepath)
        self.unpack_resources(value)
    
    def fill(self, value):
        #self.newf.set(value)
        print(value)
        os.makedirs(os.getcwd()+"/"+value+"/resources")
        os.makedirs(os.getcwd()+"/"+value+"/rbuild")
        self.find_resource()
        self.unpack_mf(value)
        
    def quick_list(self):
        self.packs.delete(0, END)
        self.lbitems = []
        for item in os.listdir(os.getcwd()):
            if os.path.isdir(os.getcwd()+"/"+item):
                self.lbitems.append(item)
                self.packs.insert(END, item)
    
    def REPLACE(self):
        if not self.no_alerts.get():
            prompt = messagebox.askyesno(title="Replacing file", message="You are about to replace a music file, this cannot be undone. Continue?")
            if not prompt:
                return 0
        
        self.musicout.configure(state="normal")
        filename = self.userpath.get()
        dest = self.filep.get()
        shutil.copy(filename, os.getcwd()+"/"+dest)
        file_unextended = filename.split("/")
        file = file_unextended[len(file_unextended)-1]
        
        self.musicout.insert(INSERT, "\n"+filename+" moved to and replaced " +dest +" successfully")
        self.musicout.configure(state="disabled")
        
    def clearpath(self):
        self.userpath.set("none")
        if self.no_bound.get():
            self.musicout.configure(state="normal")
            self.musicout.insert(INSERT, "User path cleared")
            self.musicout.configure(state="disabled")
    
    def openfile(self):
        filename =  fd.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("OGG files","*.ogg"),("all files","*.*")))
        print (filename)
        self.userpath.set(filename)
        if self.no_bound.get():
            self.musicout.configure(state="normal")
            self.musicout.insert(INSERT, "\nUser path set to "+filename)
            self.musicout.configure(state="disabled")
        
        
        #os.system(command)
        
    def singleUnpack(self):
        if os.path.isfile(self.inphasef.get()+".mf"):
            path=self.inphasef.get()
            if  not self.resourceunpack.get():
                command = self.multifypath.get()+" -x -f "+path+".mf"
                os.system(command)
                os.system("move "+path+" rbuild")
            else:
                command = self.multifypath.get()+" -x -f resources/"+path+".mf"
                os.system(command)
                os.system("move resources/"+path+" rbuild")
            
            messagebox.showinfo(title="Process Finished", message="Unpacked.")
        else:
            messagebox.showinfo(title="Missing file", message="No such file exists.")
            
    
    def singlePack(self):
        if os.path.isdir("rbuild/"+self.inphasef.get()):
            path=self.inphasef.get()
            command = self.multifypath.get()+" -c -f resources/"+path+".mf rbuild/"+path
            samefile = self.multifypath.get()+" -c -f "+path+".mf rbuild/"+path
            messagebox.showinfo(title="Process Finished", message="Packed.")
            os.system(command)
            #os.system(samefile)
        else:
            messagebox.showinfo(title="Missing file", message="No such file exists.")
            
    def add_one(self):
        self.counter += 1
        self.output.see(END)
        self.set_current_path()
        self.fts()
        if self.progressone["value"]==0:
            self.infop.set("Awaiting Process.")
        
        self.after(400, self.add_one)
        
        if self.no_bound.get():
            self.musicout.configure(state="normal")
            self.musicout.insert(INSERT, "\nEvents Checked:")
        
        if self.userpath.get()=="none":
           self.replacet["state"] = "disabled"
           if self.no_bound.get():
            self.musicout.insert(INSERT, "\nReplace: disabled")
        else:
           self.replacet["state"] = "normal"
           if self.no_bound.get():
            self.musicout.insert(INSERT, "\nReplace: enabled")
           
        if self.library[self.track.get()]["unit"] == "Playground":
            self.fzone["state"] = "disabled"
            self.szone["state"] = "normal"
            self.other["state"] = "disabled"
            self.filep.set(self.newf.get()+"/rbuild/"+self.library[self.track.get()]["base"]+""+self.library[self.track.get()][self.sub.get()]+".ogg")
        if self.library[self.track.get()]["unit"] == "coghq":
            self.szone["state"] = "disabled"
            self.fzone["state"] = "normal"
            self.other["state"] = "disabled"
            self.filep.set(self.newf.get()+"/rbuild/"+self.library[self.track.get()]["base"]+"/"+self.library[self.track.get()][self.factory.get()]+".ogg")
        if self.library[self.track.get()]["unit"] == "other":
            self.fzone["state"] = "disabled"
            self.szone["state"] = "disabled"
            self.other["state"] = "normal"
            self.filep.set(self.newf.get()+"/rbuild/"+self.library[self.track.get()][self.osub.get()]+".ogg")
        
        self.musicout.configure(state="disabled")
    
    def fts(self):
        #print("opened")
        try:
            with open("multify.path", "r") as z:
                #self.output.insert(INSERT, "path loaded: "+file.read())
                #print(z.read())
                self.multifypath.set(z.read())
        except:
            pass
        try:
            with open("ttrpath.path", "r") as x:
                #self.output.insert(INSERT, "path loaded: "+file.read())
                #print(x.read())
                self.toontown.set(x.read())
        except:
            pass
                
    def TEST(self):
        path = "phase_3"
        command = self.multifypath.get()+" -c -f resources/"+path+".mf rbuild/"+path
        subprocess.run(command)
        
    def pack_mf(self):
        self.top.destroy()
        self.output.configure(state="normal")
        phase = ["3","3.5","4","5","5.5","6","7","8","9","10","11","12","13"]
        
        for x in range(0, len(phase)):
            path=self.newf.get()+"/rbuild/phase_"+phase[x]
            if os.path.isdir(path):  
                print("\nResource file found")
                self.output.insert(INSERT, path+" found.\n")
            else:  
                self.output.insert(INSERT, path+" is missing.\n")
                prompt = messagebox.askyesno(title="Missing files", message=path+" is missing. Do you wish to continue?")
                if not prompt:
                    return 0
        prompt = messagebox.askyesno(title="Warning", message="Packing to .mf will overwrite all current .mf files. Do you want to continue?")
        if not prompt:
            return 0
        
        for x in range(0, len(phase)):
            path="phase_"+phase[x]
            self.progressone["value"]=x
            self.infop.set("Removing "+path)
            root.update()
            command = self.newf.get()+"/resources/"+path+".mf"
            if os.path.isfile(command):
                os.remove(command)
                self.output.insert(INSERT, path+" purged.\n")
            else:
                self.output.insert(INSERT, path+" wasn't located. Skipping.\n")
            #os.system(samefile)
            #shutil.copy("resources/"+path+".mf", self.toontown.get()+"/resources/"+path+".mf")
        prepath = os.getcwd()
        os.chdir(prepath+"/"+self.newf.get()+"/rbuild")
        print(os.getcwd())
        
        for x in range(0, len(phase)):
            path="phase_"+phase[x]
            self.progressone["value"]=x
            self.infop.set("Repacking "+path)
            root.update()
            command = self.multifypath.get()+" -c -f "+path+".mf "+path
            self.output.insert(INSERT, path+" packing...\n")
            os.chdir(prepath+"/"+self.newf.get()+"/rbuild")
            os.system(command)
            #os.system(samefile)
            self.output.insert(INSERT, path+" finished.\n")
            #shutil.copy("resources/"+path+".mf", self.toontown.get()+"/resources/"+path+".mf")
        os.chdir(prepath)    
        for x in range(0, len(phase)):
            path="phase_"+phase[x]
            self.progressone["value"]=x
            self.infop.set("Relocating "+path)
            root.update()
            #os.system("move rbuild/"+path+".mf resources/"+path+".mf")
            shutil.copy(prepath+"/"+self.newf.get()+"/rbuild/"+path+".mf", prepath+"/"+self.newf.get()+"/resources/"+path+".mf")
            self.output.insert(INSERT, path+" relocating.n")
            #subprocess.run(command)
            #os.system(samefile)
            #self.output.insert(INSERT, path+" moved.\n")
            #shutil.copy("resources/"+path+".mf", self.toontown.get()+"/resources/"+path+".mf")
        self.progressone["value"]=0
        root.update()
        #clean up
        """
        if os.path.isdir(self.toontown.get()+"/resources"):
            shutil.copy("resources/"+path+".mf", self.toontown.get()+"/resources/"+path+".mf")
        else:
            messagebox.showinfo(title="Missing Folder", message="Toontown was missing a resource folder, one was created.")
            os.makedirs(self.toontown.get()+"/resources")
            shutil.copy("resources", self.toontown.get()+"/resources")
        """
        self.output.configure(state="disabled")
    
    def export(self):
        self.top.destroy()
        phase = ["3","3.5","4","5","5.5","6","7","8","9","10","11","12","13"]
        for x in range(0, len(phase)):
            path="phase_"+phase[x]
            self.progressone["value"]=x
            self.infop.set(path)
            root.update()
            shutil.copy(self.newf.get()+"/resources/"+path+".mf", self.toontown.get()+"/resources/"+path+".mf")
            self.output.insert(INSERT, path+" was moved to toontown.\n")
        self.progressone["value"]=0
        self.output.insert(INSERT, self.newf.get()+" was applied to toontown!\n")
        root.update()
    def REMOVE(self):
        prompt = messagebox.askyesno(title="Remove", message="Delete "+self.newf.get()+"?")
        if prompt:
            self.output.insert(INSERT, self.newf.get()+" removed.\n")
            shutil.rmtree(os.getcwd()+"/"+self.newf.get(), ignore_errors=True)
            self.top.destroy()
            self.quick_list()
    def unpack_mf(self, p):
        self.output.configure(state="normal")
        phase = ["3","3.5","4","5","5.5","6","7","8","9","10","11","12","13"]
        
        for x in range(0, len(phase)):
            path="phase_"+phase[x]+".mf"
            if os.path.isdir(path):  
                print("\nResource file found")
                #self.output.insert(INSERT, "Resource file found.\n")
            elif os.path.isfile(path):  
                print(path+" found!")
                self.output.insert(INSERT, "Similar files found.\n")
                prompt = 1
                if prompt:
                    break
                else:
                    return 0
            else:  
                print(path+" not found, continue..." )
                
        for x in range(0, len(phase)):
            path="phase_"+phase[x]
            self.progressone["value"]=x
            self.infop.set("Removing "+path)
            root.update()
            command = p+"/rbuild/"+path
            self.output.insert(INSERT, path+" removing...\n")
            if os.path.isdir(command):
                shutil.rmtree(command, ignore_errors=True)
            else:
                self.output.insert(INSERT, path+" wasn't found. Skipped.\n")
            self.output.insert(INSERT, path+" finished.\n")
        self.output.insert(INSERT, "Process finished\n")
        for x in range(0, len(phase)):
            path="phase_"+phase[x]
            self.progressone["value"]=x
            self.infop.set("Unpacking "+path)
            root.update()
            command = self.multifypath.get()+" -x -f "+path+".mf"
            self.output.insert(INSERT, "relocating "+path+"\n")
            os.system(command)
            #self.output.insert(INSERT, path+" finished.\n")
            os.system("move "+path+" "+p+"/rbuild")
            shutil.copy(os.getcwd()+"/"+path+".mf", p+"/resources/"+path+".mf")
            #self.output.insert(INSERT, path+" moved.\n")
        #clean up
        self.progressone["value"]=0
        self.output.insert(INSERT, "Process finished\n")
        root.update()
        self.output.configure(state="disabled")
        
    def unpack_resources(self, p):
        self.find_resource()
        self.output.configure(state="normal")
        phase = ["3","3.5","4","5","5.5","6","7","8","9","10","11","12","13"]
        
        for x in range(0, len(phase)):
            path=p+"/resources/phase_"+phase[x]+".mf"
            if os.path.isdir(path):  
                print("\nResource file found")
                #self.output.insert(INSERT, "Resource file found.\n")
            elif os.path.isfile(path):  
                print(path+" found!")
                self.output.insert(INSERT, "Similar files found.\n")
                break
                
        
        for x in range(0, len(phase)):
            path="phase_"+phase[x]
            self.progressone["value"]=x
            self.infop.set(path)
            root.update()
            command = self.multifypath.get()+" -x -f "+p+"/resources/"+path+".mf"
            self.output.insert(INSERT, "relocating "+path+"\n")
            os.system(command)
            #self.output.insert(INSERT, path+" finished.\n")
            os.system("move "+path+" "+p+"/rbuild/"+path)
            #self.output.insert(INSERT, path+" moved.\n")
        #clean up
        self.output.insert(INSERT, "Process finished\n")
        self.progressone["value"]=0
        root.update()
        self.output.configure(state="disabled")
    
    def load_mf(self, d, p):
        phase = ["3","3.5","4","5","5.5","6","7","8","9","10","11","12","13"]
        
        for x in range(0, len(phase)):
            path="phase_"+phase[x]+".mf"
            if not os.path.isfile(p+"/"+path):  
                print(path+" not found")
                self.output.insert(INSERT, path+" not found.\n")
                return 0
               
        for i in range(0, len(phase)):
            shutil.copy(p+"/phase_"+phase[i]+".mf", d+"/resources")
            self.progressone["value"]=i
            self.output.insert(INSERT, "grabbing phase_"+phase[i]+"\n")
            self.infop.set("Copying phase_"+phase[i])
            root.update()
        #messagebox.showinfo(title="Finish", message="Setup completed!")
        self.output.insert(INSERT, "Process finished\n")
        self.progressone["value"]=0
        root.update()
                
    
    def find_multify(self):
        prompt = messagebox.askyesno(title="Relocate", message="This option is to locate a multify.exe file that is NOT located in the panda3d directory\n(/panda3dfolder/bin/multify.exe)\nSelecting a multify file that is NOT from panda3d ver 1.10.4.1 folder may cause the program to fail. This will replace the CURRENT path, which is "+self.multifypath.get()+". Do you wish to proceed?")
        if prompt:
            messagebox.showinfo(title="Find file", message="Please select the multify.exe file.")
            filename =  fd.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("EXE files","*.exe"),("all files","*.*")))
            self.multifypath.set(filename)
            messagebox.showinfo(title="Notice", message="Note:\nThis option is entirely controlled by the user, any errors that may occur will probably result from running this process.")
        else:
            messagebox.showinfo(title="Notice", message="Multify.exe was restored to its previous path: "+self.multifypath.get())
            
    def new_pack(self):
        print("newpack:")
        self.entryWindow()
        print(self.newf.get())
        
    def set_current_path(self):
        try:
            self.newf.set(self.lbitems[self.packs.curselection()[0]])
            if self.newf.get():
                #messagebox.showinfo(title="Notice", message="You are now editing "+self.newf.get())
                self.efile["state"] = "normal"
                self.openf["state"] = "normal"
        except:
            pass#print("nothing")
    def find_resource(self):
        toonfile = ""
        ignore_fts = 0
        if os.path.isfile(os.getcwd()+"/ttrpath.path"):
            ignore_fts = 1
            with open("ttrpath.path", "r") as file:
                self.toontown.set(file.read())
        
        if not os.path.isdir(self.toontown.get()):
            self.output.configure(state="normal")
            messagebox.showinfo(title="First Time Setup", message="Please select a path to the toontown install folder")
            toonfile =  fd.askdirectory()
            if not os.path.isfile(os.getcwd()+"/ttrpath.path"):
                with open("ttrpath.path", "w") as file:
                    file.write(toonfile)
        
        if not toonfile and not ignore_fts:
            messagebox.showinfo(title="Find file", message="You need to select your toontown install folder, that's the whole purpose of this program!")
            return 0
        else:
            if not ignore_fts:
                self.toontown.set(toonfile)
            
        if not os.path.isdir(self.toontown.get()+"/resources"):
            os.makedirs(self.toontown.get()+"/resources")
        
        print("clicked")
        path="resources"
        if os.path.isdir(path):  
            print("\nResource file found")
            self.output.insert(INSERT, "Resource file found.\n")
        elif os.path.isfile(path):  
            print("\nAn Error Has Occured.")
            self.output.insert(INSERT, "An Error Has Occured.\n")
        else:  
            print("Resources file doesn't exist, creating one..." )
            self.output.insert(INSERT, "Resource file doesn't exist.\n")
            #prompt = messagebox.askyesno(title="Missing file", message="Resource file not found, create one?")
            #if prompt:
                #os.makedirs(path)
                #self.output.insert(INSERT, "Resource folder created in current directory.\n")
            #else:
                #return 0
        
        path="rbuild"
        if os.path.isdir(path):  
            print("\nBuild file found")
            self.output.insert(INSERT, "Resource file found.\n")
        elif os.path.isfile(path):  
            print("\nAn Error Has Occured.")
            self.output.insert(INSERT, "An Error Has Occured.\n")
        else:  
            print("Build file doesn't exist, creating one..." )
            self.output.insert(INSERT, "Build file doesn't exist.\n")
            #prompt = messagebox.askyesno(title="Missing file", message="Build file not found, create one?")
            #if prompt:
                #os.makedirs(path)
                #self.output.insert(INSERT, "Build folder created in current directory.\n")
            #else:
                #return 0
        
        
        if os.path.isfile(os.getcwd()+"/multify.path"):
            with open("multify.path", "r") as file:
                self.multifypath.set(file.read())
        
        path=self.multifypath.get()
        
        if os.path.isdir(path):  
            print("\nResource file found")
            #self.output.insert(INSERT, "Resource file found.\n")
        elif os.path.isfile(path):  
            print("\nMultify.exe file found")
            self.output.insert(INSERT, "Multify.exe file found.\n")
        else:  
            print("\nMultify file doesn't exist!" )
            self.output.insert(INSERT, "Multify.exe file missing.\n")
            prompt = messagebox.askyesno(title="Missing File", message="Is Panda3d Installed?")
            if prompt:
                messagebox.showinfo(title="Find file", message="Please select the panda3d folder.")
                filename =  fd.askdirectory()
                print (filename+"/bin/multify.exe")
                self.multifypath.set(filename+"/bin/multify.exe")
                with open("multify.path", "w") as file:
                    file.write(self.multifypath.get())
                if os.path.isfile(self.multifypath.get()):
                    self.output.insert(INSERT, "Multify.exe file found.\n")
                    #messagebox.showinfo(title="File found", message="Multify.exe was located successfully.")
                else:
                    messagebox.showinfo(title="Missing file", message="Multify.exe was not found. Make sure you select the folder with /bin/multify.exe in it. NOT THE BIN FOLDER ITSELF! If the multify file is located elsewhere, go to the options tab and select the multify file!")
                    return 0
            else:
                prompt = messagebox.showinfo(title="Missing Program", message="Please download panda3d!")
                return 0
            #return 0
        
        phase = ["3","3.5","4","5","5.5","6","7","8","9","10","11","12","13"]
        
        for x in range(0, len(phase)):
            path="phase_"+phase[x]+".mf"
            if os.path.isdir(path):  
                print("\nResource file found")
                #self.output.insert(INSERT, "Resource file found.\n")
            elif os.path.isfile(path):  
                print(path+" found")
                self.output.insert(INSERT, path+" found.\n")
            else:  
                print(path+" doesn't exist!" )
                self.output.insert(INSERT, path+" missing.\n")
                #prompt = messagebox.askyesno(title="Missing file", message="One or more phase files are missing. Do you want to copy the current phase files from the toontown install folder?")
                prompt = 1
                if prompt:
                    for i in range(0, len(phase)):
                        shutil.copy(self.toontown.get()+"/phase_"+phase[i]+".mf", os.getcwd())
                        self.progressone["value"]=i
                        self.infop.set("Copying phase_"+phase[i])
                        self.output.insert(INSERT, "phase_"+phase[i]+" was added.\n")
                        root.update()
                    messagebox.showinfo(title="Finish", message="Setup completed!")
                    self.progressone["value"]=0
                    root.update()
                else:
                    return 0
        self.upackf["state"] = "normal"
        self.packf["state"] = "normal"
        
        self.sunpack["state"] = "normal"
        self.spack["state"] = "normal"
        self.packrestore["state"] = "normal"
        self.exportf["state"] = "normal"
        self.output.configure(state="disabled")
            
        
root = Tk()
#root.iconbitmap('music_icon.ico')
root.geometry("400x300")
root.resizable(False, False)
app = Window(root)
root.mainloop()

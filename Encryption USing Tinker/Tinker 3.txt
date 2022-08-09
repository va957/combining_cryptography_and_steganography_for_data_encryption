import tkinter 
from tkinter import filedialog
from PIL import ImageTk,Image
from code1 import encode,decode
from code2 import encodeImage,decodeImage

window = tkinter.Tk()
window.title("Blackout Poetry")
w = window.winfo_screenwidth()
h = window.winfo_screenheight()
window.minsize(w,h)

text = ""
text_label = ""
image = [[]]
img = [[]]
img2 = [[]]
up_image = [[]]
txt_box=[]
txt_lavel=""
file=""
file2=""

canvas = tkinter.Canvas(window,width=w,height=h,highlightthickness=0)
canvas.place(x=0,y=0)
back=ImageTk.PhotoImage(Image.open('back1.png').resize((w,h), Image.ANTIALIAS))
canvas.create_image(int(w/2),int(h/2), anchor="center", image=back)
canvas.back=back

canvas1 = tkinter.Canvas(window,width=480, height=480,bg="gray50")
canvas1.place(x=300,y=150)
canvas1_label_bg = '#%02x%02x%02x' % (44,37,31)
canvas1_label = tkinter.Label(window, text='Original Image', fg='white', bg=canvas1_label_bg, font=(None,12))
canvas1_label.place(x=500,y=120)

canvas2 = tkinter.Canvas(window,width=480, height=480,bg="gray50")
canvas2.place(x=850,y=150)
canvas2_label_bg = '#%02x%02x%02x' % (46,38,35)
canvas2_label = tkinter.Label(window, text='Updated Image', fg='white', bg=canvas2_label_bg, font=(None,12))
canvas2_label.place(x=1050,y=120)


#adding image buttons : 
upload_image_button=ImageTk.PhotoImage(Image.open('Icons/upload.png').resize((175,40), Image.ANTIALIAS)) #1.2
encode_image_button=ImageTk.PhotoImage(Image.open('Icons/encode.png').resize((118,33), Image.ANTIALIAS)) #1.3
decode_image_button=ImageTk.PhotoImage(Image.open('Icons/decode.png').resize((118,33), Image.ANTIALIAS)) #1.3
proceed_image_button=ImageTk.PhotoImage(Image.open('Icons/proceed.png').resize((128,38), Image.ANTIALIAS)) #1.2
clear_text_image_button=ImageTk.PhotoImage(Image.open('Icons/clear_text.png').resize((93,29), Image.ANTIALIAS))
clear_images_image_button=ImageTk.PhotoImage(Image.open('Icons/clear_images.png').resize((110,29), Image.ANTIALIAS))
save_image_button=ImageTk.PhotoImage(Image.open('Icons/save.png').resize((106,38), Image.ANTIALIAS))
exit_image_button=ImageTk.PhotoImage(Image.open('Icons/exit.png').resize((87,39), Image.ANTIALIAS)) #1.3
encode_set_image=ImageTk.PhotoImage(Image.open('Icons/encode_set.png').resize((118,33), Image.ANTIALIAS)) #1.3
decode_set_image=ImageTk.PhotoImage(Image.open('Icons/decode_set.png').resize((118,33), Image.ANTIALIAS)) #1.3
upload_image2_button=ImageTk.PhotoImage(Image.open('Icons/upload.png').resize((140,33), Image.ANTIALIAS)) #1.5
enter_text_button=ImageTk.PhotoImage(Image.open('Icons/text.png').resize((76,32), Image.ANTIALIAS)) #1.5



#adding upload image box
def upload_image() :
    global file
    file = filedialog.askopenfilename(initialdir = "/", 
                    title="Select An Image",
                    filetype=(("PNG","*.png"),("JPEG","*.jpg"),("Bitmap","*.bmp")))
    label = tkinter.Label(window,text=file[:14]+str("...")+file[-12:],font="Helvetica 8 italic")
    label.place(x=30,y=200)
    disp_image(file)

uploadbg = '#%02x%02x%02x' % (50, 39, 35)
upload = tkinter.Button(window,
                image=upload_image_button,
                command=upload_image,
                borderwidth=0,
                bg=uploadbg,
                cursor='hand2',
                activebackground=uploadbg,
                highlightthickness=0)
upload.place(x=30,y=150)

#displaying uploaded image
def disp_image(file) :    
    global image 
    global img
    img = Image.open(file)
    img = img.convert('RGB')
    r_img = img     #resized image for canvas
    width,height = img.size
    ratio = width/height
    if (ratio>1) :   # landscape image
        width = 480     # max possible width in canvas
        height = (int)(width/ratio)
        r_img = img.resize((width,height), Image.ANTIALIAS)
    elif (ratio<1) :     #potrait image
        height = 480    #max possible height in canvas 
        width = (int)(height*ratio)
        r_img = img.resize((width,height), Image.ANTIALIAS)
    else :      #square image
        height = 480 
        width = 480
        r_img = img.resize((width,height), Image.ANTIALIAS)

    image = ImageTk.PhotoImage(r_img)    #converting to image type 
    canvas1.create_image(240,240,image=image)
    canvas1.image = image 



# radio buttons and functions
c = tkinter.IntVar()
d = tkinter.IntVar()

def clicked():
    
    def clicked_2() :
        
        def extract_data() : 

            #calling the functions
            global up_image

            if (c.get()==1 and d.get()==1) :        # encoding with text
                global text
                text = txt_box.get()
                #txt_box.delete(0,'end')    #clear content once entered
                #txt_button['state'] = tkinter.DISABLED     #freeze entry button
                text_label = tkinter.Label(window,text=text,font="Times 12")
                modified_image = encode(img,text)       #modified image is only attributes

            elif (c.get()==2 and d.get()==1) :      # decoding with text
                text,modified_image = decode(img)
                decode_text_bg = '#%02x%02x%02x' % (97,80,70)
                decoded_text_label = tkinter.Label(window,text="Decoded Text : "+text,fg='white',bg=decode_text_bg,font=("Helvatica","12","bold"))
                decoded_text_label.place(x=850,y=650)
            
            elif (c.get()==1 and d.get()==2) :      # encoding with images
                modified_image = encodeImage(img,img2)
            
            elif (c.get()==2 and d.get()==2) :      # decoding with images
                modified_image = decodeImage(img)
                #modified_image = crop_black(modified_image)

            update_image(modified_image)    # display updated image
        
        if (d.get()==1) :
            if (c.get() == 1) :     # enter text box only for encode
                global txt_label
                global txt_box
                message = "Enter Text :"  #enter text to encode
                txt_box = tkinter.Entry(window)                
                txt_label_bg = '#%02x%02x%02x' % (56,47,40)
                txt_label = tkinter.Label(window,text="(alphanumeric values and spaces)",font=(None,7),fg='white',bg=txt_label_bg)
                txt_box.place (x=130,y=335)
                txt_label.place (x=130,y=360)
        
        elif (d.get()==2 and c.get()==1) :      #upload image only for encode
            global file2
            global img2
            file2 = filedialog.askopenfilename(initialdir = "/", 
                    title="Select An Image",
                    filetype=(("PNG","*.png"),("JPEG","*.jpg"),("Bitmap","*.bmp")))
            img2 = Image.open(file2) 
            img2 = img2.convert('RGB')

        proceedbg = '#%02x%02x%02x' % (70,58,51)
        proceed_button = tkinter.Button(window,
                image=proceed_image_button,
                command=extract_data,
                cursor='hand2',
                bg=proceedbg,
                activebackground=proceedbg,
                border=0,
                highlightthickness=0)

        proceed_button.place(x=20,y=480)
        

    rad3 = tkinter.Radiobutton(window, 
            image=enter_text_button,
            variable=d,
            value=1,
            indicator=0,    #to change style     
            background=encodebg,
            border=0,
            command=clicked_2,
            cursor='hand2',
            activebackground=encodebg,
            highlightthickness=0)

    rad4 = tkinter.Radiobutton(window, 
            image=upload_image2_button,
            variable=d,
            value=2,
            indicator=0,    #to change style     
            background=encodebg,
            border=0,
            command=clicked_2,
            cursor='hand2',
            activebackground=encodebg,
            highlightthickness=0)
    
    rad3.place (x=20,y=330)
    rad4.place (x=20,y=380)

    messagebg = '#%02x%02x%02x' % (54,45,37)
    message = tkinter.Label(window,text="Select one of the following :",font="Helvetica 10 italic",fg='white',bg=messagebg)
    message.place(x=20,y=290)


decodebg = '#%02x%02x%02x' % (54,45,37)
encodebg = '#%02x%02x%02x' % (52,41,35)
rad1 = tkinter.Radiobutton(window, 
            image=encode_image_button,
            variable=c,
            value=1,
            indicator=0,    #to change style     
            background=encodebg,
            border=0,
            command=clicked,
            cursor='hand2',
            activebackground=encodebg,
            highlightthickness=0,
            selectimage=encode_set_image)

rad2 = tkinter.Radiobutton(window, 
            image=decode_image_button,
            variable=c,
            value=2,
            indicator=0,    #to change style
            background=decodebg,
            border=0,
            command=clicked,
            cursor='hand2',
            activebackground=decodebg,
            highlightthickness=0,
            selectimage=decode_set_image)

rad1.place(x=20, y=240)
rad2.place(x=155, y=240)



def update_image(modified_image) :    #display updated image
    
    width,height = modified_image.size
    ratio = width/height
    r_img = modified_image 
    if (ratio>1) :   # landscape image
        width = 480     # max possible width in canvas
        height = (int)(width/ratio)
        #print(width,height)
        r_img = modified_image.resize((width,height), Image.ANTIALIAS)
    elif (ratio<1):     #portrait image
        height = 480    #max possible height in canvas 
        width = (int)(height*ratio)
        #print(width,height)
        r_img = modified_image.resize((width,height), Image.ANTIALIAS)
    else :      #square image
        height = 480 
        width = 480
        r_img = modified_image.resize((width,height), Image.ANTIALIAS)

    up_image = ImageTk.PhotoImage(r_img)    #converting to image type
    canvas2.create_image(240,240, image=up_image)
    canvas2.up_image=up_image

    # saving the result
    def save_result() : 
        
        x=file.rfind('/')   # last occurance of / in file name
        y=file.rfind('.')   # last occurance of . in file name
        image_name=file[x+1:y:1]    # to extract only name of the image and not entire path
        result_img = modified_image.save("Saved Images/"+image_name+" result.png")
    
    savebg = '#%02x%02x%02x' % (100,92,80)
    save = tkinter.Button(window,
                image=save_image_button, 
                command=save_result,
                cursor='hand2',
                border=0,
                bg=savebg,
                activebackground=savebg,
                highlightthickness=0)
    save.place(x=1225,y=650)



#reset and exit buttons
def clear_img() :
    canvas1.delete("all")
    canvas2.delete("all")

def clear_text() :
    text=''
    txt_box.delete(0,'end')

clearimgbg = '#%02x%02x%02x' % (70,57,51)
cleartextbg = '#%02x%02x%02x' % (65,52,45)
quitbg = '#%02x%02x%02x' % (80,67,61)

clear_images = tkinter.Button(window,image=clear_images_image_button,command=clear_img,border=0,activebackground=clearimgbg,bg=clearimgbg,highlightthickness=0)
clear_images.place(x=20,y=580)
clear_text = tkinter.Button(window,image=clear_text_image_button,command=clear_text,border=0,activebackground=cleartextbg,bg=cleartextbg,highlightthickness=0)
clear_text.place(x=150,y=580)

quit_button = tkinter.Button(window,
            image=exit_image_button, 
            command=window.quit,
            border=0,
            highlightthickness=0,
            bg=quitbg,
            activebackground=quitbg)
quit_button.place(x=20,y=630)

window.mainloop()

from tkinter import *
from PIL import ImageTk, Image, ImageEnhance, ImageFilter
from tkinter import filedialog, messagebox
from pathlib import Path
import shutil
import cv2
import numpy as np
import os

# definindo front-end
root = Tk()
root.title("Sistema de Manipulação de Imagens")

# obtendo o tamanho do monitor do usuário
monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()

# definindo as dimensões da janela do aplicativo
root.geometry(f"{monitor_width}x{monitor_height}+0+0")
root.state("zoomed")
root.resizable(width=True, height=True)

img_no = 0

bg_image = PhotoImage(file="bgapp.png")
background_label = Label(root, image=bg_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

filename = ["" for x in range(150)]
filename[0] = "noFile"

def openfilename():
    file = filedialog.askopenfilename(title='abrir')
    return file

def openimage():
    x = openfilename()
    img = Image.open(x)
    fileNameWithoutExtension = Path(x).stem
    width, height = img.size
    ratio = round(width/height, 3)
    fra = round(ratio, 3)
    if width > height:
        newHeight = round(650/fra)
        img.resize((650, newHeight)).save('img.png')
    else:
        newWidth = round(650*fra)
        img.resize((newWidth, 650)).save('img.png')
    global filename, img_no
    img_no = img_no + 1
    filename[img_no] = "img.png"
    img = Image.open(filename[img_no])
    #front-end
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.place(x=150, y=40)

def updateimage():
    global filename, img_no
    img_enhance = Image.open(filename[img_no])
    #front-end
    img_enhance = ImageTk.PhotoImage(img_enhance)
    panel = Label(root, image=img_enhance)
    panel.image = img_enhance
    panel.place(x=150, y=40)

def downloadimage():
    global filename, img_no
    # Verificando se a foto teve alterações
    if filename[img_no] != "img.png":
        try:
            # Alterar o caminho da pasta download de acordo com seu PC
            shutil.move(filename[img_no], "C:/Users/Berlatto/Downloads/" + filename[img_no])
            messagebox.showinfo("Sucesso!", "Imagem baixada com sucesso! Verifique sua pasta de downloads.")
        except Exception as e: 
            messagebox.showerror("Erro", f"Erro ao baixar a imagem: {e}")
    else:
        messagebox.showinfo("Inalterada", "Nenhuma imagem para baixar.")

def grayscaleimage():
    global filename, img_no
    if os.path.exists(filename[img_no]):
        img_grayscale = Image.open(filename[img_no])
        color = ImageEnhance.Color(img_grayscale)
        img_no = img_no + 1
        color.enhance(0).save(str(img_no)+'.png')
        filename[img_no] = str(img_no)+'.png'
        updateimage()
    else:
        messagebox.showwarning("Imagem Inexistente", "Abra uma imagem para que possa ser editada!")

def blurimage():
    global filename, img_no
    if os.path.exists(filename[img_no]):
        img_blur = Image.open(filename[img_no])
        filter = img_blur.filter(ImageFilter.BLUR)
        img_no = img_no + 1
        filter.save(str(img_no)+'.png')
        filename[img_no] = str(img_no)+'.png'
        updateimage()
    else:
        messagebox.showwarning("Imagem Inexistente", "Abra uma imagem para que possa ser editada!")


def sharpenimage():
    global filename, img_no
    if os.path.exists(filename[img_no]):
        img_sharpen = Image.open(filename[img_no])
        filter = img_sharpen.filter(ImageFilter.SHARPEN)
        img_no = img_no + 1
        filter.save(str(img_no)+'.png')
        filename[img_no] = str(img_no)+'.png'
        updateimage()
    else:
        messagebox.showwarning("Imagem Inexistente", "Abra uma imagem para que possa ser editada!")


def embossimage():
    global filename, img_no
    if os.path.exists(filename[img_no]):
        img_emboss = Image.open(filename[img_no])
        filter = img_emboss.filter(ImageFilter.EMBOSS)
        img_no = img_no + 1
        filter.save(str(img_no)+'.png')
        filename[img_no] = str(img_no)+'.png'
        updateimage()
    else:
        messagebox.showwarning("Imagem Inexistente", "Abra uma imagem para que possa ser editada!")

def rotateimage():
    global filename, img_no
    if os.path.exists(filename[img_no]):
        img_rotate = Image.open(filename[img_no])
        img_rotated = img_rotate.rotate(90, expand=True, resample=Image.BILINEAR)
        img_no = img_no +1
        img_rotated.save(str(img_no) + '.png')
        filename[img_no] = str(img_no) + '.png'
        updateimage()
    else:
        messagebox.showwarning("Imagem Inexistente", "Abra uma imagem para que possa ser editada!")

def MinImage():
    global filename, img_no
    if os.path.exists(filename[img_no]):
        img = Image.open(filename[img_no])
        width, height = img.size
        newHeight = int (height*0.5)
        newWidth = int (width*0.5)
        imageMin = img.resize((newWidth,newHeight), Image.BILINEAR)
        imageMin.save("imagemmin.png")
        img_no = img_no + 1
        filename[img_no] = ("imagemin.png")
        updateimage()
    else:
        messagebox.showwarning("Imagem Inexistente", "Abra uma imagem para que possa ser editada!")

def MaxImage():
    global filename, img_no
    if os.path.exists(filename[img_no]):
        img = Image.open(filename[img_no])
        width, height = img.size
        newHeight = int (height*2)
        newWidth = int (width*2)
        imageMin = img.resize((newWidth,newHeight), Image.BILINEAR)
        imageMin.save("imagemmax.png")
        img_no = img_no + 1
        filename[img_no] = ("imagemax.png")
        updateimage()
    else:
        messagebox.showwarning("Imagem Inexistente", "Abra uma imagem para que possa ser editada!")  

def translationImage():
    global filename,img_no
    if os.path.exists(filename[img_no]):
        imagem = cv2.imread(filename[img_no])

        # Define o deslocamento desejado (25 pixels para direita e 50 pixels para baixo)
        deslocamento = np.float32([[1, 0, 25], [0, 1, 50]])

        # Aplica a translação usando o método warpAffine
        imagem_transladada = cv2.warpAffine(imagem, deslocamento, (imagem.shape[1]+25, imagem.shape[0]+50),cv2.INTER_LINEAR)

        # salva a imagem e exiba ela na interface
        cv2.imwrite("imagem_transladada.png", imagem_transladada)
        img_no = img_no +1
        filename[img_no] = ("imagem_transladada.png")
        updateimage()
    else:
        messagebox.showwarning("Imagem Inexistente", "Abra uma imagem para que possa ser editada!")

## Carregando a imagem de fundo
#imagem_de_fundo = Image.open("bgapp.jpg")
#imagem = ImageTk.PhotoImage(imagem_de_fundo)
## Criando um label com a imagem de fundo
#label_imagem = Label(root, image=imagem_de_fundo)
#label_imagem.place(x=0, y=0, relwidth=1, relheight=1)

Button(root, text='Abrir Imagem', height="1", width="15", bg="#9CD941", fg="#D9D9D9", bd="0", cursor="hand2", font="Montserrat", command=openimage).place(x=2, y=2)
#Label(root, text='Selecione uma opção', font="Montserrat", bg="#404040", fg="white").place(x=2, y=300)
Button(root, text='Escala de Cinza', height="1", width="15", bg="#9CD941", fg="#D9D9D9", bd="0", cursor="hand2", font="Montserrat", command=grayscaleimage).place(x=2, y=350)
Button(root, text='Efeito Blur', height="1", width="15", bg="#9CD941", fg="#D9D9D9", bd="0", cursor="hand2", font="Montserrat", command=blurimage).place(x=2, y=375)
Button(root, text='Efeito Sharpen', height="1", width="15", bg="#9CD941", fg="#D9D9D9", bd="0", cursor="hand2", font="Montserrat", command=sharpenimage).place(x=2, y=600)
Button(root, text='Efeito Emboss', height="1", width="15", bg="#9CD941", fg="#D9D9D9", bd="0", cursor="hand2", font="Montserrat", command=embossimage).place(x=2, y=650)
Button(root, text='Rotacionar', height="1", width="15", bg="#9CD941", fg="#D9D9D9", bd="0", cursor="hand2", font="Montserrat", command=rotateimage).place(x=2, y=390)
Button(root, text='Minimizar', height="1", width="15", bg="#9CD941", fg="#D9D9D9", bd="0", cursor="hand2", font="Montserrat", command=MinImage).place(x=2, y=450)
Button(root, text='Maximizar', height="1", width="15", bg="#9CD941", fg="#D9D9D9", bd="0", cursor="hand2", font="Montserrat", command=MaxImage).place(x=2, y=500)
Button(root, text='Download', height="1", width="15", bg="#9CD941", fg="#D9D9D9", bd="0", cursor="hand2", font="Montserrat", command=downloadimage).place(x=400, y=650)
Button(root, text='Transladar', height="1", width="15", bg="#9CD941", fg="#D9D9D9", bd="0", cursor="hand2", font="Montserrat", command=translationImage).place(x=2, y=550)

#Rodar o App
root.mainloop()
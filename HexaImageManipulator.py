from tkinter import *
from PIL import ImageTk, Image, ImageEnhance, ImageFilter
from tkinter import filedialog, messagebox
from pathlib import Path
import tkinter as tk
import shutil
import cv2
import numpy as np
import os
import keyboard

# definindo front-end
root = Tk()
root.title("Hexa Image Manipulator")

# obtendo o tamanho do monitor do usuário
screen_height = root.winfo_screenheight()
screen_width = root.winfo_screenwidth()

# definindo as dimensões da janela do aplicativo
root.geometry(f"{screen_width}x{screen_height}+0+0")
root.state("zoomed")
root.resizable(width=True, height=True)

img_no = 0

bg_image = Image.open("BackgroundAppNasa.png")
bg_image = bg_image.resize((screen_width, screen_height))  # redimensionando a imagem para o tamanho da tela
bg_image = ImageTk.PhotoImage(bg_image)

# criando um label para exibir a imagem de fundo
background_label = tk.Label(root, image=bg_image)
background_label.place(relx=0, rely=0, relwidth=1, relheight=1)  # Ocupa toda a tela

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
    global filename, img_no, panel
    img_no = img_no + 1
    filename[img_no] = "img.png"
    img = Image.open(filename[img_no])
    #front-end
    img = ImageTk.PhotoImage(img)
    panel = tk.Label(root, image=img)
    panel.image = img
    panel.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

def updateimage():
    global filename, img_no
    img_enhance = Image.open(filename[img_no])
    img_enhance = ImageTk.PhotoImage(img_enhance)
    # utilizando o panel já iniciado em "openimage"
    panel.configure(image=img_enhance)
    panel.image = img_enhance
    panel.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

def downloadimage():
    global filename, img_no
    filedownload = filedialog.askdirectory()
    # Verificando se a foto teve alterações
    if filename[img_no] != "img.png":
        try:
            # Alterar o caminho da pasta download de acordo com seu PC
            shutil.move(filename[img_no], os.path.join(filedownload, filename[img_no]))
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
        img_rotated = img_rotate.rotate(90, expand=True)
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
        newHeight = int (height*0.8)
        newWidth = int (width*0.8)
        imageMin = img.resize((newWidth,newHeight), Image.BILINEAR)
        img_no = img_no + 1
        imageMin.save(str(img_no) + ".png")
        filename[img_no] = str(img_no) + ".png"
        updateimage()
    else:
        messagebox.showwarning("Imagem Inexistente", "Abra uma imagem para que possa ser editada!")

def MaxImage():
    global filename, img_no
    if os.path.exists(filename[img_no]):
        img = Image.open(filename[img_no])
        width, height = img.size
        newHeight = int (height*1.2)
        newWidth = int (width*1.2)
        imageMax = img.resize((newWidth,newHeight), Image.BILINEAR)
        img_no = img_no + 1
        imageMax.save(str(img_no) + ".png")
        filename[img_no] = str(img_no) + ".png"
        updateimage()
    else:
        messagebox.showwarning("Imagem Inexistente", "Abra uma imagem para que possa ser editada!")  

def translationImage():
    global filename,img_no
    x, y = 0, 0
    last_key = None
    if os.path.exists(filename[img_no]):
        imagem = cv2.imread(filename[img_no])

        # Define o deslocamento desejado (x e y)
        deslocamento = np.float32([[1, 0, x], [0, 1, y]])
        updateimage()
        key = keyboard.read_event(suppress=True).name

        if key != last_key:
            if key == 'up':
                y -= 10
            elif key == 'down':
                y += 10
            elif key == 'left':
                x -= 10
            elif key == 'right':
                x += 10

            deslocamento = np.float32([[1, 0, x], [0, 1, y]])
            imagem_transladada = cv2.warpAffine(imagem, deslocamento, (imagem.shape[1], imagem.shape[0]),cv2.INTER_LINEAR)
            # salva a imagem e exiba ela na interface
            cv2.imwrite("imagem_transladada.png", imagem_transladada)
            img_no = img_no +1
            filename[img_no] = ("imagem_transladada.png")
            updateimage()

            last_key = key
    else:
        messagebox.showwarning("Imagem Inexistente", "Abra uma imagem para que possa ser editada!")

def sobreoapp():
    janela_sobre = tk.Toplevel()
    janela_sobre.title("Sobre o App")

    # definindo as dimensões da janela do aplicativo
    janela_sobre.geometry("500x600")
    janela_sobre.resizable(width=False, height=False)

    janela_sobre.configure(bg="#A1A2A6")

    label_infoname = tk.Label(janela_sobre, text="Hexa Image Manipulator\nVersão 1.0", font=("Montserrat", 14), bg="#A1A2A6")
    label_infoname.pack(pady=20)

    label_infodescription = tk.Label(janela_sobre, text="O Hexa Image Manipulator é um aplicativo que permite manipular uma imagem modificando sua rotação, translação e tamanho. É possível também aplicar filtros"
    + ", permitindo que a foto fique em escala de cinza, blur, sharpen e emboss\n\n Autores: Eduardo Berlatto, Mariana Rosendo, Osmar Jatobá Neto, Pedro Henrique Freire de Oliveira, Vitor Nunes Oliveira\n\n"
    +"Contato: eduardoberlattousjt@gmail.com\n\nObrigado por usar o app!", font=("Montserrat", 12), wraplength= 450, bg="#A1A2A6")
    label_infodescription.pack(pady=40)

    botao_fechar = tk.Button(janela_sobre, text='Fechar', height="1", width="15", bg="#56735A", fg="#FFFFFF", bd="0", cursor="hand2", font="Montserrat", command=janela_sobre.destroy).place(relx=0.38, rely = 0.95)


Button(root, text='Abrir Imagem', height="2", width="15", bg="#56735A", fg="#FFFFFF", bd="0", cursor="hand2", font="Montserrat", command=openimage).place(relx=0.001, rely=0.002)
Button(root, text='Escala de Cinza', height="1", width="15", bg="#56735A", fg="#FFFFFF", bd="0", cursor="hand2", font="Montserrat", command=grayscaleimage).place(relx=0.001, rely=0.30)
Button(root, text='Efeito Blur', height="1", width="15", bg="#56735A", fg="#FFFFFF", bd="0", cursor="hand2", font="Montserrat", command=blurimage).place(relx=0.001, rely=0.35)
Button(root, text='Efeito Sharpen', height="1", width="15", bg="#56735A", fg="#FFFFFF", bd="0", cursor="hand2", font="Montserrat", command=sharpenimage).place(relx=0.001, rely=0.40)
Button(root, text='Efeito Emboss', height="1", width="15", bg="#56735A", fg="#FFFFFF", bd="0", cursor="hand2", font="Montserrat", command=embossimage).place(relx=0.001, rely=0.45)
Button(root, text='Rotacionar', height="1", width="15", bg="#56735A", fg="#FFFFFF", bd="0", cursor="hand2", font="Montserrat", command=rotateimage).place(relx=0.001, rely=0.55)
Button(root, text='Minimizar', height="1", width="15", bg="#56735A", fg="#FFFFFF", bd="0", cursor="hand2", font="Montserrat", command=MinImage).place(relx=0.001, rely=0.60)
Button(root, text='Maximizar', height="1", width="15", bg="#56735A", fg="#FFFFFF", bd="0", cursor="hand2", font="Montserrat", command=MaxImage).place(relx=0.001, rely=0.65)
Button(root, text='Transladar', height="1", width="15", bg="#56735A", fg="#FFFFFF", bd="0", cursor="hand2", font="Montserrat", command=translationImage).place(relx=0.001, rely=0.70)
Button(root, text='Sobre o App', height="1", width="15", bg="#56735A", fg="#FFFFFF", bd="0", cursor="hand2", font="Montserrat", command=sobreoapp).place(relx=0.001, rely=0.95)
Button(root, text='Download', height="1", width="15", bg="#56735A", fg="#FFFFFF", bd="0", cursor="hand2", font="Montserrat", command=downloadimage).place(relx=0.5, rely=0.95, anchor=tk.CENTER)

#Rodar o App
root.mainloop()
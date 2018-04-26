# coding=utf-8
# cat sitecustomize.py
import sys
from bs4 import BeautifulSoup
import shutil
import wget
from pyunpack import Archive
from Tkinter import *
from google import google
import ntpath
import urllib
from tkFileDialog import askopenfilename
from os import *
raiz = Tk()
global filename
global nombreArchivo
global rutaBase
cadenaDeBusqueda = ""
def  MainWindow():
    reload(sys)
    sys.setdefaultencoding('utf8')
    cmd_seleccionarVideo = Button(raiz, text="Seleccione archivo", command=seleccionarArchivo)
    cmd_seleccionarVideo.grid(rows=5,column=0)
    cmd_buscarYdescargar = Button(raiz, text="Descargar subtitulos", command=buscarSubtitulos)
    cmd_buscarYdescargar.grid(rows=4,column=0)
    raiz.geometry("600x600+0+0")
    raiz.mainloop()
    pass


def seleccionarArchivo():
    global filename
    filename= askopenfilename(filetypes=[("Video","*.avi"), ("Todos los archivos", "*.*")], initialdir = "C:\\", title = "Selecciona el archivo")
    global nombreArchivo
    nombreArchivo= (path.basename(filename)).replace(".mp4", "")
    global rutaBase
    rutaBase= path.dirname(filename)
    global cadenaDeBusqueda
    cadenaDeBusqueda = (nombreArchivo+ " subtitulos en español").replace(" ", "+")
    pass

def buscarSubtitulos():
    links = google.search(cadenaDeBusqueda,1)
    downloadLink = ""
    nLinBus = 0
    bajar = False
    for resultados in links:
            if (bajar == True):
                break
            contenido = urllib.urlopen(resultados.link)
            paginaDeDescarga = BeautifulSoup(contenido, "html.parser")
            for link in paginaDeDescarga.select("a[href*='bajar.php']"):
                if (nLinBus == 1):
                    bajar = True
                    break
                nLinBus = nLinBus + 1
                href = BeautifulSoup(str(link), "html.parser")
                downloadLink = href.a['href']
                nameRar = nombreArchivo + ".rar"
                urllib.urlretrieve(downloadLink, filename=rutaBase + "/" + nameRar)
                directorio =rutaBase+"/" + nombreArchivo.replace(" ", "-")
                if not path.exists(rutaBase + "/" + nombreArchivo):
                    makedirs(rutaBase + "/" + nombreArchivo)
                Archive(rutaBase + "/" + nameRar).extractall(rutaBase + "/" + nombreArchivo)
                contadorArchivos = 0
                for filename in listdir(rutaBase + "/" + nombreArchivo) :
                    contadorArchivos = contadorArchivos + 1
                    nombreNuevo = (rutaBase + "/" + nombreArchivo + "-" + str(contadorArchivos) + ".srt")
                    rename(rutaBase + "/" + nombreArchivo+"/" +filename,  nombreNuevo)
                    pass
                rmdir(rutaBase + "/" + nombreArchivo)
                remove(rutaBase + "/" + nameRar)
    pass

MainWindow()

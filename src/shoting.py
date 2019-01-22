import pyscreenshot as ImageGrab
#from pywinauto import application

def main():
    imagem = ImageGrab.grab()
    imagem.save('screenShot1.jpg', 'jpeg')

def region_of_image():
    im=ImageGrab.grab(bbox=(10,10,500,500))
    im.save('screenShot2.jpg', 'jpeg')

def allwindow():
    childprocess = True
    bbox = (10, 10, 510, 510)  # X1,Y1,X2,Y2
    backend = 'gnome-screenshot'

    im = ImageGrab.grab(bbox=bbox, backend=backend, childprocess=childprocess)
    print(im.size)

#run in windows
# def start_and_print():
#     app = application.Application().start("notepad")
#     app.Untitled_Notepad.capture_as_image().save('window.png')

def teste():
    print(ImageGrab.backends())
    im = ImageGrab.grab(bbox=None, backend='gnome-screenshot', childprocess='gnome-calculator')
    im.save('screenShot1.jpg', 'jpeg')

if __name__ == "__main__":
    #main()
    #region_of_image()
    #allwindow()
    #start_and_print()
    teste()
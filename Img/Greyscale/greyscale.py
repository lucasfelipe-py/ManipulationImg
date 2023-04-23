# Importando as libs
from PIL import Image
import os

# Criando nova pasta para receber as imagens em escala de cinza
greyscale_imgs = "greyscale_imgs"
if greyscale_imgs not in os.listdir():
    os.mkdir(greyscale_imgs)
    
# Listando imagens dentro da pasta "fotos"
file_path = "fotos"
files = [i for i in os.listdir(file_path) if os.path.isfile(os.path.join(file_path, i))]

# Realizando conversão de cores
for file in files:
    # Atribuindo os caminhos às variáves
    img_path = os.path.join(file_path, file)
    new_path = os.path.join(greyscale_imgs, file)
    
    # Convertendo as cores da img para escala de cinza
    img = Image.open(img_path).convert('L')
    
    # Salvando nova imagem
    img.save(new_path, 'PNG', optimize=True)
    

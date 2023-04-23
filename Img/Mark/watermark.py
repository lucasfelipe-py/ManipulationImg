from PIL import Image
import os

# Redimensionando watermark
watermark = Image.open("watermark.png")
width_w, height_w = watermark.size

# Criando nova pasta
watermark_imgs = "watermark_imgs"
if watermark_imgs not in os.listdir():
    os.mkdir(watermark_imgs)
    
# Listando imagens dentro da pasta "fotos"
file_path = "fotos"
files = [i for i in os.listdir(file_path) if '.jpg' in i]

for file in files:
    # Atribuindo os caminhos às variáves
    img_path = os.path.join(file_path, file)
    new_path = os.path.join(watermark_imgs, file)
    
    # Abrindo imagem e extraindo tamanho da larg x alt
    img = Image.open(img_path)
    width_i, height_i = img.size
    
    # Posicionando watermark no canto inferior direito
    base_width = int(0.2 * width_i)
    w_percent = base_width / float(width_w)
    h_size = int(height_w * w_percent)
    
    watermark = watermark.resize((base_width, h_size))
    img.paste(watermark, (width_i - base_width, height_i - h_size), watermark)
    
    # Salvando nova imagem
    img.save(new_path)
# Importando as libs
from PIL import Image
import os

# Fator de redução
reduct_fact = 0.5

# Nome da nova pasta
compressed_path = "fotos_comprimidas"

# Criando nova pasta
if compressed_path not in os.listdir():
    os.mkdir(compressed_path)

# Listando imagens dentro da pasta "fotos"
file_path = "fotos"
files = [i for i in os.listdir(file_path) if os.path.isfile(os.path.join(file_path, i))]

# Iniciando variáveis de comparação
size_before, size_after = 0, 0

# Realizando compressão
for file in files:
    # Atribuindo os caminhos às variáves
    img_path = os.path.join(file_path, file)
    new_path = os.path.join(compressed_path, file)
    
    # Tamanho do arquivo antes da compressão
    size_before += os.stat(img_path).st_size
    
    # Abrindo imagem e aplicando o fator de redução
    img = Image.open(img_path)
    new_w = int(img.size[0] * reduct_fact)
    new_h = int(img.size[1] * reduct_fact)
    
    # Redimensionando imagem
    img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    # Salvando nova imagem
    img.save(new_path, 'PNG', optimize=True, quality=90)
    size_after += os.stat(new_path).st_size

# Convertendo tamanho para mb
size_before /= (1024 ** 2)
size_after /= (1024 ** 2)

# Comparando tamanho antes x depois da compressão (mb)
dif = size_before - size_after
percent = (dif / size_before) * 100

# OUTPUT
print(f"Diferença absoluta: -{round(dif, 2)}mb\nDiferença percentual: -{round(percent, 2)}%")
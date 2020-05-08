import glob, shutil


# Modifique esses caminhos para se adequarem a suas pastas, lembrem-se de trocar '\' por '/'
imagens = 'C:/Users/leona/Pictures'
executaveis = 'C:/Users/leona/Downloads/Executaveis'
zips = 'C:/Users/leona/Downloads/Zip'
isos = 'C:/Users/leona/Downloads/Iso'
pdfs = 'C:/Users/leona/Downloads/PDFs'
gerais = 'C:/Users/leona/Downloads/Gerais'
livros = 'C:/Users/leona/Desktop/Livros'
musicas = 'C:/Users/leona/Desktop/Musicas'

arquivos = glob.glob('C:/Users/leona/Downloads/*.*')

for i in arquivos:
    aux = i.split('.')
    tipo =aux[len(aux)-1]

    if (tipo == 'jpeg') or (tipo == 'jpg') or (tipo == 'png') or (tipo == 'JPG'):
        shutil.move(i,imagens)
        print("Arquivo " + aux[len(aux)-2] + " movido para " + imagens)

    elif tipo == "exe":
        shutil.move(i,executaveis)
        print("Arquivo " + aux[len(aux)-2] + " movido para " + executaveis)

    elif tipo == 'zip' or tipo == 'rar' or tipo == '7z' or tipo == 'tar':
        shutil.move(i,zips)
        print("Arquivo " + aux[len(aux)-2] + " movido para " + zips)

    elif tipo == 'iso':
        shutil.move(i,isos)
        print("Arquivo " + aux[len(aux)-2] + " movido para " + isos)

    elif tipo == 'pdf':
        nomepdf = i.split('\\')
        ehlivro = nomepdf[len(nomepdf)-1].split('-')
        if ehlivro[0] == 'livro':
            shutil.move(i,livros)
            print("Arquivo " + aux[len(aux)-2] + " movido para " + livros)
        else:
            shutil.move(i,pdfs)
            print("Arquivo " + aux[len(aux)-2] + " movido para " + pdfs)

    elif tipo == 'mp3':
        shutil.move(i,musicas)
        print("Arquivo " + aux[len(aux)-2] + " movido para " + musicas)
    
    else:
        shutil.move(i,gerais)
        print("Arquivo " + aux[len(aux)-2] + " movido para " + gerais)

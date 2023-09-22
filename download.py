## Raimundo Fenoll. Obtener enlaces de descarga de una web
## El enlace de descarga que genera la pagina es: https://dl.opensubtitles.org/es/download/sub/XXXXX
## Esos XXXXXX los obtengo del codigo fuente de la pagina. Recorro el fichero y corto justo antes y justo después

splitAfterThis = "/es/subtitleserve/sub/"
splitBeforeThis = "\" onclick"
perfectDownloadLink = "https://dl.opensubtitles.org/es/download/sub/"
listIdDownloads = []

#Methods
def exists(line):
    return splitAfterThis in line

#Main
def main() :
    #Open web
    f_web = open("web.txt", "r")
    randomLines = f_web.readlines()

    f_downloadsLinks = open("downloadLinks.txt", "w")

    for line in randomLines:
        if exists(line) :
            downloadId = (line.split(splitAfterThis)[1]).split(splitBeforeThis)[0]
            listIdDownloads.append(downloadId)

    with open("downloadLinks.txt", "w") as file :
        for itemDownloadId in listIdDownloads:
            file.write(perfectDownloadLink + itemDownloadId + "\n")
            
    f_downloadsLinks.close()
    f_web.close()











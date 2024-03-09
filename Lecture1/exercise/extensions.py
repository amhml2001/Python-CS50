def main():
    file = input("File name: ")
    print(ext(file))

def ext(f):
    match str(f).lower().split(".")[1]:
        case "gif":
            return "image/gif"
        case "jpg":
            return "image/jpeg"
        case "jpeg":
            return "image/jpeg"
        case "png":
            return "image/png"
        case "pdf":
            return "application/pdf"
        case "txt":
            return "text/plain"
        case "zip":
            return "application/zip"
        case _ :
            return "application/octet-stream"
            


main()
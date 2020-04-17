#!/usr/bin/python3
import sharepy
import os

def UploadToSharepoint(event=None, context=None):
    SPUrl =  os.environ['SPUrl']
    siteName = os.environ['siteName']
    libraryName = os.environ['libraryName']
    username = os.environ['username']
    password = os.environ['password']

    os.chdir("/tmp/")
    s = sharepy.connect(SPUrl,username,password)
    s.save()
    headers = {"accept": "application/json;odata=verbose",
    "content-type": "application/x-www-urlencoded; charset=UTF-8"}
    fileToUpload = "/var/task/uploadfile.txt"
    file_name=os.path.basename(fileToUpload)

    with open(fileToUpload, 'rb') as read_file:
        content = read_file.read()
        p = s.post(f"{SPUrl}/sites/{siteName}/_api/web/GetFolderByServerRelativeUrl('{libraryName}')/Files/add(url='{file_name}',overwrite=true)", data=content, headers=headers)
        print("File Successfully Uploaded!")
    return(file_name)

if __name__ == "__main__":
   UploadToSharepoint()

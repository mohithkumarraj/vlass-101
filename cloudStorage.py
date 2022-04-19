import dropbox 

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
    
    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)

        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token = 'sl.BGCMybcEBUMf0bXADWSkMMuxHL2VTWjYZGlfDYAx5LEQcpadmnXleuBri6I2tRG9-MRX9pKPbQlqzTitZXhXBCyEGnMuWlo7wxTOO6VbLi-cNqENQRyp-cHTXS2vTO7TAApFbz0'
    transferData = TransferData(access_token)
    file_from = input("enter the file path to transfer- ")
    file_to = input("enter the full path to upload to dorpbox- ")

    transferData.upload_file(file_from,file_to)
    print("file has been moved")

main()
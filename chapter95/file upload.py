import requests
testUrl = "http://httpbin.org/post"
testFiles = {
    "test_file_1": open("file1.txt", "rb")
    
}

responseVar = requests.post(testUrl, files = testFiles)
if responseVar.ok:
    print("Successfully Uploaded all files !")
    print(responseVar.text)
else:
    print("Upload failed !")
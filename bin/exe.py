from subprocess import PIPE, Popen
import urllib.request

def cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]

result=cmdline(r"C:\Users\SAMSUNG\Desktop\★코드분석-release_64\release_64\release_64\bin\vamp-simple-host.exe nnls-chroma:chordino:simplechord ..\01-산토끼.wav")
result = str(result)
result = result.replace("\\","")

Senten="";Sootja=""
char_li=[];int_li=[];cnt=0
result_size = len(result)
result = result.replace(": ",":")
result = result.split(' ')

for i in range(1,len(result)):
    time,code = result[i].split(':')
    print(time,":",code[:-2])

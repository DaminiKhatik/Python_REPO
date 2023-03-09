
from subprocess import check_call
ok = check_call(['ffmpeg','-i','C:/Users/MyHP/Desktop/PYTHONbook/chapter181/Download-Free-Airtel-New-Ringtone.wav']) 
if ok:    
    with open('output.wav', 'rb') as f:
        wav_file = f.read()

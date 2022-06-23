import os
import pytesseract as pt
from PIL import Image
from operator import itemgetter
from stat import S_ISREG, ST_CTIME, ST_MODE
import glob

tess_path = r'C:\Users\Ganga Babu.M\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
pt.pytesseract.tesseract_cmd = tess_path

path = r'C:\Users\Ganga Babu.M\AppData\Local\Packages\Microsoft.ScreenSketch_8wekyb3d8bbwe\TempState'
dir_path = path
entries = (os.path.join(dir_path, file_name) for file_name in os.listdir(dir_path))
entries = ((os.stat(path), path) for path in entries)
entries = ((stat[ST_CTIME], path)for stat, path in entries if S_ISREG(stat[ST_MODE]))
entries = sorted(list(entries), key=itemgetter(0), reverse=True)
img = entries[0][1]
# print(img)
img1 = Image.open(img)

text = pt.image_to_string(img1)
print('Extracted Information:')
print('\n')
print(text)
print('='*80)
img1.show()

cond = input('Would you like to Flush the Screen Shot Folder ? Press(Y/N) : ')

if cond == 'Y' or cond == 'y':
    for f in entries:
        print(f[1])
        os.remove(f[1])
    print('Folder Flushed.')
else:
    print('Folder Flused cancelled')

    

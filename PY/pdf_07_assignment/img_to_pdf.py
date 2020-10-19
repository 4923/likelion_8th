# 이미지 다운받을때 쓰는 라이브러리
import urllib.request

urls = []
for i in range(1,18):
  # url 목록 만들기
  url = 'http://contents.hufs.ac.kr/contents/univ/Y61614/2016/031/slidebook/pages/' + str(i) + '.png'
  urls.append(url)
  # url로 이미지 다운받기
  url_n = ''.join(urls[i-1])
  urllib.request.urlretrieve(url_n, 'image'+str(i)+'.png')

# 묶어서 pdf로 변환하기
from PIL import Image

image1 = Image.open(r'C:\Users\dmatm\OneDrive\바탕 화면\2020\like lion\코딩 세션\PY\pdf_07_assignment\image1.png')
im1 = image1.convert('RGB')

imagelist = []
for i in range(2,18):
  image = Image.open(r'C:\Users\dmatm\OneDrive\바탕 화면\2020\like lion\코딩 세션\PY\pdf_07_assignment\image'+str(i)+'.png')
  im = image.convert('RGB')
  imagelist.append(im)

im1.save(r'C:\Users\dmatm\OneDrive\바탕 화면\2020\like lion\코딩 세션\PY\pdf_07_assignment\assi_0731.pdf',save_all=True, append_images=imagelist)
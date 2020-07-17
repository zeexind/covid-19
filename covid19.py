#Coded by ZeeX_IND
#CytoXploit
#Galaxy Xploiter Team
from bs4 import BeautifulSoup as Jx
import requests, os

os.system('clear')
os.system('figlet -f standard "Covid19" | lolcat')
print (" Coded By ZeeX_IND - Galaxy Xploiter Team // CytoXploit ")
corona = requests.get('http://covid19.go.id')
soup = Jx(corona.text, 'html.parser')
find_1 = soup.find_all('strong')
find_2 = soup.find_all('div', {'class:', 'pt-4 text-color-grey text-1'})
find_3 = soup.find_all('div', {'class:', 'col-md-3 text-color-black p-4'})
negara = find_1[0].text
terkonfirmasi = find_1[1].text
meninggal = find_1[2].text
update = find_2[0].text
petugas = find_3[1].text
positif_indo = find_1[3].text
sembuh_indo = find_1[4].text
meninggal_indo = find_1[5].text

print "\033[31;1m\t"
print '============= GLOBAL  ============='
print 'Total Negara :', negara
print 'Terkonfirmasi :', terkonfirmasi
print 'Meninggal :', meninggal
print "\033[33;1m\t"
print '============ INDONESIA ============ '
print 'Positif :', positif_indo
print 'Sembuh :', sembuh_indo
print 'Meninggal :', meninggal_indo 
print update
print "\033[32;1m\t"
print '*Note:'
print 'Data Statistik Ini Akan Selalu Update Secara Otomatis'
print 'remember to..'
print 'Stay At Home!'


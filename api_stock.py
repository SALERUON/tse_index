import requests
r=requests.get("http://en.tsetmc.com/Loader.aspx")
rt=r.text
from bs4 import BeautifulSoup
soup=BeautifulSoup(rt,"html.parser")

#re=soup.prettify(formatter="html")    run this line to find your target in the html scripts
val_0=soup.find_all("tr",attrs={"id":"32097828799138957"})

rt1=str(val_0) #val_0 is class most be change to str 

import regex
re00=regex.sub (r"\s+","",rt1)
re0=regex.findall(r"[^*]{90}<td>([\d|-]\d*\.\d{2})",re00)

print (r.status_code)# status of connection 
#print (re00)
print (float(re0[0])) 
import string as s
import random
import re

def tesaduf(uzunluq=8,mod=True):
	"""
	Bu modul tesadufi sekilde bir araya
	gelmis herf ve reqem toplusundan iba-
	ret, daxil edilmis uzunluqda bir 
	deyer qaytarir. Eyer daxil etmemisiniz-
	se default olaraq 8 xarakterlik deyer 
	qaytarir. 
	Bundan basqa siz
	funksiyaya mod="nomre" eyni zamanda
	mod="herf" acar sozlerini daxil etmekle
	yalniz reqemlerden yaxud yalniz herfler-
	den ibaret deyerler de elde ede bilersi-
	niz. Numuneler
	
	n=tesaduf() / 5h8D67k0
	n=tesaduf(5) / 5z6f9
	n=tesaduf(4,mod="herf") / gDRn
	n=tesaduf(5,mod='nomre') / 47587
	n=tesaduf(mod='herf') / yzTVcRRx
	n=tesaduf(mod='nomre') / 74863259
	
	ilk versiya HERAKL
	hec bir istediyinizi ede bilersiniz.
	"""
	herfler=list(s.ascii_letters)
	tesaduf=""
	r=0
	try:
		while r<=uzunluq:
			x=herfler[random.randint(0,len(herfler)-1)]
			y=random.randint(0,len(herfler))
			if mod=='herf':
				tesaduf=tesaduf+x
			elif mod=='nomre':
				tesaduf=tesaduf+str(y)
			else:
				tesaduf=tesaduf+x+str(y)
			r=r+1
		return tesaduf[:uzunluq]
	except TypeError:
		print('zehmet olmasa tam eded daxil edin')
def nomre_yoxla(v,say=8):
        p="[^a-zA-Z\W]+"
        check = re.search(p,str(v))
        if check:
            if len(str(v)) == say:
                return True
            else:
                return False
        else:
            return False
        
def nomre_tester(v):
    try:
        float(v)
        return True
    except ValueError:
        return False

        


            
            
            
    



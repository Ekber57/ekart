import re
class form_manager:
    """
                         KLAS HAQQINDA MELUMAT VE ISLETME NUMUNELERI
    
    Class bezi metinlerde gormek istemediyiniz sozleri istediyiniz sozle evez etmek ucun
    elverisli metodlara malikdir. Bundan elave siz xaricden oz ifadelerinizi ve onlari
    evez eden sozleri elave ede bilersiniz . Daxili ifade evezleyicileri istifade etmek is-
    teyirsinizse:
        
        obyekt=form_manager('sizin metn') yazmaqiniz kifayet edir
    Bundan basqa siz xaricden ifade ve evezini de daxil ede bilersiniz....................
    Oz ifadelerinizi daxil etmek ucun siz konstruktor icerisine develop=True acarini daxil
    etmelisiniz byekt=replacer(metn,luqet,develop=True) luqetin dictionary formatinda  
    olmasi sertdir...
    Numune:
        
         metn='en gozel cihaz n1-dir
         luqet = {'en gozel cihaz':'asus'} / cumle tapa bilmedim :)
         obyekt=form_manager(metn,luqet,develop=True) 
         obyekt.translate()
         
         cixis:
             
             asus n1-dir

             
    Yuxaridaki numunede sadece cumlede belli metin evezlenecek eyer ifadenin kecdiyi her bir yeri evezle-
    mek isteyirsinizse translate(any=True) seklinde yazmalisiniz
    Numune:
         metn='en gozel cihaz n1-dir
         luqet = {'en gozel cihaz':'asus'} / cumle tapa bilmedim :)
         obyekt=form_manager(metn,luqet,develop=True) 
         obyekt.translate() //
         bu numuneni deyisdirib metn='en gozel cihaz n1-dirler' yazsaq islemeyecek bunun ucun bucur yazilmalidir
         Numune:
         metn='en gozel cihaz n1-dir' / sonra istenilen xarakter ola biler
         luqet = {'en gozel cihaz':'asus'} / cumle tapa bilmedim :)
         obyekt=form_manager(metn,luqet,develop=True) 
         obyekt.translate(any=True)
        
    Yuxaridaki numunede translate metodu icerisine up=True acarini daxil etseniz cumlenin
    ilk herfi boyudulecek  ve  noqteden sonraya bosluq elave edilecek ve noqteden sonraki ilk herf boyu-
    dulecek...
    Numune:
        
        obyekt.translate(up=True)
        
    Hemcinin klasda metinde tekrar olunan soz ve on-
    larin sayini gosteren, cumlenin uzunluq hecmi, xarakterlerin tekrar sayi, bosluq
    kimi atrribular movcuddur.
    
    Numune:
        obyekt.uzunluq / cumlenin xarakter sayi
        obyekt.bosluq /  cumledeki sozler arasi bosluq sayi
        obyekt.sozlerin_tekrar_sayi / cumledeki her soz ve onlarin cumlede islenme sayi (dictionary formatinda)
        obyekt.tekrar_xarakter_sayi / cumledeki her bir xarakter ve onun tekrar sayi (dictionary formatinda)
    
    _____________________________Konstruktor olmadan da isleyecek metodlar______________________________
    Bundan basqa siz form_manager klasinin konstruktorunu bos qoyaraq da nomre yoxlama kimi metodddan istifade 
    ede bilersiniz
    Numune:
        opyekt=form_manager()
        obyekt.nomer('sizin nomre') // bu formatda meselen 0555555555
        Nomer metodu size nomrein standarta uyqun olub olmadiqini bildiren deyer True yaxud False qaytarir
        Siz metoddan istifade etdikden sonra onun operator ve format atributlarini ala bilersiniz
        Numune:
            opyekt=form_manager()
            obyekt.nomer('sizin nomre') // bu formatda meselen 0555555555
            obyekt.format // nomrenin formati meselen 055
            obyekt.operator // nomrenin operatoru meselen Bakcell
            
            
     Mail metodu daxil olan formatinin duzgun olub olmadiqini gosterir ve gmail mail servislerini destekleyir
     Numune:
         
         obyekt.mail('asus_09@gmail.com') / True qaytaracaq
         obyekt.mail('asus_09@mail.ru') / True qaytaracaq
         Xatirladim ki mailde reqem ve altdan xett (_)-e icaze verilir normal mailde olduqu kimi
         
    Sayt metodu duzgun sayt girmeye xidmet edir:
        Numune:
            
            obyekt.sayt('sayt.az') // True qaytaracaq
            xatirladim ki sayt adi minimum uc maksimum 10, domen adi is minimum 2 maksimum 5 herfli ola biler
            sayt adinda reqemlere icaze verilir
            obyekt.sayt('sensiz52.com') // True qaytaracaq
         
         
    
    SOKUN OYRENIN PAYLASIN ILK VERSIYA HERAKL TEREFINDEN YAZILIB    
    
    """
    __metn=''
    __ifade=['ekber']
    __evezi=['*']
    __tam_metn=''
    __parcalanma=''
    uzunluq=0
    bosluq=0
    sozlerin_tekrar_sayi={}
    tekrar_xarakter_sayi={}
    __nomer=''
    __pattern='^[0][5|7][7|5|1|0][0-9]{7}$'
    format=''
    operator=''
   
    
    def __init__(self,sizin_metn='',luqet={},develop=False):
        self.__metn=sizin_metn
        self.__parcalanma=self.__metn.split(' ')
        
        if develop == True:
            self.__ifade=list(luqet.keys())
            self.__evezi=list(luqet.values())
    def __replacer(txt,ifade,evezi,any):
        tam=''
        for x in txt:
           for y in range(0,len(evezi)):
               soz=x
               if any==True:
                   soz=soz.replace(ifade[y],evezi[y])
               else:
                   if re.search('^'+ifade[y]+'$',soz):
                       soz=soz.replace(ifade[y],evezi[y])
                       pass
                   else:
                       pass
               
               
                   
               pass
           if len(tam)==0:
               tam=soz
               pass
           else:
               tam=tam+" "+soz
               
           pass
        return tam
    def nomer(self,number):
            
            preg=re.search(self.__pattern,number)
            self.__nomer=number
            if preg:
                self.format=preg.group()[:3]
                if str(preg.group()[:3]) == str('051' or '050'):
                    self.operator='Azercell'
                elif str(preg.group()[:3]) == str('055'):
                    self.operator='Bakcell'
                else:
                    self.operator='Narmobile'
                return True
    def mail(self,email):
        if re.search('^[a-zA-Z][a-zA-Z_\d]+@g?mail\.(com|ru)\s*$',email):
            return True 
        else:
            return False
    def sayt(self,sayt):
        if re.search('^[a-zA-Z][a-zA-Z\d]{3,10}\.{1}[a-zA-Z]{2,5}',sayt):
            return True
        else:
            return False
    
    def translate(self,up=False,any=False):
        '''
        Bu funksiya sozleri diger sozle evez eden metodu caqirir eyni zamanda cumle uzunluqunu,
        her sozun tekrarlanma sayini, her xarakterin tekrarlanma sayini, cumledeki umumi bosluq sayini
        hesablayan xirda elaveleri ozunde birlesdirir
        '''
        if self.__metn !='':
                 # sozleri evezleme
                 self.__tam_metn=form_manager.__replacer(self.__parcalanma,self.__ifade,self.__evezi,any)
                 # cumlenin uzunluqunu tapma
                 self.uzunluq=len(self.__tam_metn)
                 # bosluq saylarini tapma
                 self.bosluq=self.__tam_metn.count(" ")
                 # sozlerin tekrar sayini tapma
                 soz_sayi={}
                 for soz in self.__tam_metn.split(' '):
                      soz_sayi[soz]=self.__tam_metn.count(soz)
                 self.sozlerin_tekrar_sayi=soz_sayi
                 # xarakterlerin tekrar sayini tapma
                 xarakter_tekrar_sayi={}
                 for soz in self.__tam_metn:
                     xarakter_tekrar_sayi[soz]=self.__tam_metn.count(soz)
                 self.tekrar_xarakter_sayi=xarakter_tekrar_sayi
        # metnin ilk sozunun ve .noqtlerden sonraki ilk herfin boyudulmesi
                 if up==False:
                      return self.__tam_metn
                 else:
                     cumle=''
                     for x in self.__tam_metn.split('.'):
                         x=x.strip()
                     cumle=cumle+x[0].upper()+x[1:]+'. '
                     return  cumle
        
        
        
    

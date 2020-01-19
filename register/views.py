from django.shortcuts import render,redirect
from .models import user
from .my_modul import tesaduf
from .form_manager import * 
def index(request):
    if 'login' in request.session:
        return redirect('/office')
    else:
        return render(request,'register.html')
# Create your views here.
def registiration(request):
    if request.method=='POST':
        data={}
        if 'login' not in request.session:
            ad=request.POST.get('ad')
            soyad=request.POST.get('soyad')
            login=request.POST.get('login')
            mail=request.POST.get('mail')
            nomre=request.POST.get('nomre')
            sifre=request.POST.get('sifre')
            ckod=tesaduf(8,mod='nomre')
            if (ad,soyad,login,mail,nomre,sifre,ckod):
                fm=form_manager()
                if fm.nomer(nomre):
#                    nomre duzduse
                    if fm.mail(mail): 
                        if len(sifre) >= 6:
#                            sifre duzduse
                            if len(login) >= 6:
#                                login duzdusse
                                if not user.objects.filter(mail=mail.lower()):
#                                    mailyoxdusa
                                    if not user.objects.filter(login=login):
#                                        eyer login yoxdusa
                                        if not user.objects.filter(nomre=nomre):
                                            ck=tesaduf(7,mod='nomre')
                                            obyekt=user(ad=ad,soyad=soyad,mail=mail.lower(),nomre=nomre,sifre=sifre,login=login,status=False,balans='0.00',ckod=ck)
                                            obyekt.save()
                                            data['alert']='tebrik edirik'
                                            return render(request,'register.html',data)
                                            
#                                            eyer nomre yoxdusa 
                                            pass
                                        else:
#                                                eyer nomre varsa
                                            data['alert']='nomre qeydiyyat olunub'
                                            return render(request,'register.html',data)
#                                        
                                    else:
                                        #      eyer login varsa
                                        data['alert']='login qeydiyyat olunub'
                                        return render(request,'register.html',data)
                                        pass

                                    
                                else:
#                                    mail varsa
                                    data['alert']='mail qeydiyyat olunub'
                                    return render(request,'register.html',data)
                                    pass
                                    
                            else:
#                                login sehvdirse
                                data['alert']='login  duzgun  deyil'
                                return render(request,'register.html',data)
                                pass
                        else:
#                            sifre sehvdirse
                            data['alert']='sifre duzgun deyil'
                            return render(request,'register.html',data)
                            pass
                   
                    else:
#                        mail sehvdirse
                        data['alert']='mail duzgun deyil'
                        return render(request,'register.html',data)

                
                else:
#                    nomre sehvdirse
                    data['alert']='nomre duzgun deyilse'
                    return render(request,'register.html',data)
                    pass
            else:
#                sessya varsa
                return redirect('/')
                pass
        else:
#            method getdirse
            pass
                    
                    
                
                
                
                
                
                
                
                
                
                
                
                
                
      
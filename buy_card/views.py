from django.shortcuts import render,redirect
from .models import card
from register.models import user
from register.my_modul import nomre_tester,nomre_yoxla,tesaduf
def index(request):
    if 'login' in request.session:
        login=request.session['user_login']
        obyekt=user.objects.get(login=login)
        status = obyekt.status
        if status == True:
    #        eyer sessiya varsap
            data={
                'sesya':True,
                'balans':obyekt.balans,
                'CK': obyekt.ckod,
                }
            return render(request,'buy_card.html',data)
        else:
            return redirect('/office')
    else:
#        eyer sesya yoxdursa
        return render(request,'buy_card.html')
    
        pass
def transfer(request):
    if request.method=='POST':
#        metod postusa
        data={}
        ck=request.POST.get('ck')
        cs=request.POST.get('sifre')
        amount=request.POST.get('amount')
        if 'login' in request.session:
            user_ob=user.objects.get(login=request.session['user_login'])
            ck=user_ob.ckod
            cs=user_ob.sifre
            data['sesya']=True,
            data['CK']=ck
            data['balans']=user_ob.balans
        if ck and cs and amount:
#            eyer post vaersa
            if nomre_yoxla(ck,8):
#                eyer ck duzduse
                obyekt=user.objects.filter(ckod=ck)
                if obyekt:
#                    eyer ck varsa
#                    
                    obyekt=user.objects.get(ckod=ck)
                    if cs == obyekt.sifre:
                        balans=obyekt.balans
                        if float(balans) >= 0.2:
    #                              balans var
                            if nomre_tester(amount) and float(amount) >= 0.2:
    #                            eyer amount duzudse
                                if float(amount) <= float(balans):
    #                                eyer kifayet qeder vesait varsa
                                    obyekt_user=user.objects.get(ckod=ck)
                                    obyekt_user.balans=round(float(obyekt.balans) - float(amount),2)
                                    obyekt_user.save()
                                    ks=tesaduf(13,mod='nomre')
                                    kk=tesaduf(7)
                                    obyekt_card=card(CK=ck,status=True,KG='',amount=amount,KS=ks,KK=kk)
                                    obyekt_card.save()
                                    data['alert']='''tebrikler kart alindi kart melumatlari:
                                        KS = ''' + ks + ''' \n
                                        KK = ''' + kk + '''
                                        deyer = ''' + amount + ' azn'
                                        
                                    data['alert'].format(ks,kk)
                                    return render(request,'buy_card.html',data)
                                    pass
                                else:                                  
                                    #                              vesait yoxdusa
                                    data['alert']='əməliyyatı icra etmək üçün kifayət qədər vəsaitiniz yoxdur'
                                    return render(request,'buy_card.html',data)
    
    
                                    pass
                            else:
                                #                            amount sehvdise
                                 data['alert']='məbləğ düzgün daxil edilməyib min 0.2 azn dəyərində ekart alina bilər'
                                 return render(request,'buy_card.html',data)
    #                  
                            pass
                        else:
    #                        balans yoxdu
                             data['alert']='bu əməliyyat üçün balansınız çox azdır'
                             return render(request,'buy_card.html',data)
                    else:
#                        cs sehvdi
                         data['alert']='cüzdan şifrəsi səhvdir'
                         return render(request,'buy_card.html',data)
                else:
#                    ck tapilmadi
                     data['alert']='cüzdan tapılmadı'
                     return render(request,'buy_card.html',data)
            
            else:
#                eyer ck duzse
                 data['alert']='cüzdan kodu səhvdir'
                 return render(request,'buy_card.html',data)
        else:
#            eyer post yoxsa
             data['alert']='məlümatları tam daxil edin'
             return render(request,'buy_card.html',data)
#            pass
    else:
#        metod getdise
        pass

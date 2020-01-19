from django.shortcuts import render,redirect
from buy_card.models import card
from register.models import user
from register.my_modul import tesaduf
def index(request):
    if 'login' in request.session:
#        eyer sesya varsa
        login=request.session['user_login']
        obyekt=user.objects.get(login=login)
        status=obyekt.status
        if status == True:
    #        eyer aktiv userdirse
            data={
                'balans':obyekt.balans,
                'CK': obyekt.ckod,
                }
            return render(request,'send_card.html',data)
        else:
#            eyer aktiv user deyilse
            return redirect('/office')
    else:
#        eyer sesya yoxdursa
        return render(request,'send_card.html')
def tranzaksiya(request):
    if request.method == 'POST':
#        eyer metod postdursa
        data={}
        if 'login' in request.session:
#            sessya varsa
            data['CK']=user.objects.get(login=request.session['user_login']).ckod
            data['balans']=user.objects.get(login=request.session['user_login']).balans
            
        ck=request.POST.get('ck')
        ks=request.POST.get('ks')
        kk=request.POST.get('kk')
        if 'login' in request.session:
            ck=user.objects.get(login=request.session['user_login']).ckod
            
        if len(ck): # ''' and len(ks) and len(kk) > 0''' :
#             eyer post varsa
       
            if ck.isalnum() == True and len(ck) >= 6:
#                eyer ck duzdurse 
                if user.objects.get(ckod=ck).status == True:
    #                    eyer status aktiv suerdirse 
                        
                    if len(ks)==13 and ks.isalnum()==True:
    #                    eyer ks duzduse
                        user_obyekt=user.objects.filter(ckod=ck)
                        card_obyekt=card.objects.filter(KS=ks)
                        if user_obyekt:
    #                        user varsa
                            if card_obyekt:
    #                            kart varsa
                                if kk==card.objects.get(KS=ks).KK:
    #                                eyer kod duzdurse
                                    if card.objects.get(KS=ks).CK == ck:
    #                                    kart zaten cuzdandadi 
                                        data['alert']='kart cuzdandadir'
                                        return render(request,'send_card.html',data)
                                        pass
                                    else:
    #                                    kart cuzdanda deyilse davam
                                        if card.objects.get(KS=ks).status == True:
    #                                        eyer kart islenmeyibse ->>>>>>>>>>>>>>>
                                            c_ob=card.objects.get(KS=ks)
                                            c_ob.CK=ck
                                            c_ob.KK=tesaduf(8)
                                            c_ob.save()
    #                                        her sey duzgundur
                                            data={
                                                'success':True,
                                                'alert':' Tebrikler kart cuzdana elave olundu'
                                                }
                                            return render(request,'send_card.html',data)
                                            
                                            
    #                                        >>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                            pass
                                        else:
    #                                        kart islenibse
                                            data['alert']='kart islenib'
                                            return render(request,'send_card.html',data)
                                            pass
                                else:
    #                                kod sehdirse:
                                    data['alert']='kart kodu sehvdir'
                                    return render(request,'send_card.html',data)
                                    pass
                            else:
    #                            kart yoxdusa
                                data['alert']='kart movcud deyil'
                                return render(request,'send_card.html',data)
                                pass
                        else:
    #                        user yoxdusa
                            data['alert']='cuzdan tapilmadi'
                            return render(request,'send_card.html',data)
                            pass
                    else:
    #                    ks sehvdise
                        data['alert']='ks sehvdir'
                        return render(request,'send_card.html',data)
                    pass
                else:
#                    eyer status aktivdeyilse
                    return redirect('/office')
                    
                        
   
            else:
#                ck sehvdirse
                data['alert']='ck sehvdir'
                return render(request,'send_card.html',data)
                pass
        else:
#            post yoxsa
            data['alert']='melumat doldurulmayib'
            return render(request,'send_card.html',data)
            pass
    else:
        #        eyer metod getdirse
#        data['alert']='kart islenib'
        return render(request,'send_card.html')
        pass
    
# Create your views here.

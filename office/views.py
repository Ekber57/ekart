from django.shortcuts import render,redirect
from register.models import user
from buy_card.models import card
from django.db.models import Sum
def index(request):
    if 'login' in request.session:
        obyektler=user.objects.get(login=request.session['user_login'])
        status=obyektler.status
      
        kart_sayi=card.objects.all().filter(CK=obyektler.ckod).count()
        if kart_sayi > 0:
            kart_mebleqi=round(card.objects.filter(CK=obyektler.ckod).aggregate(Sum('amount'))['amount__sum'],3)
            pass
        else:
            kart_mebleqi=0
            pass
        if float(obyektler.balans):
            umumi_balansim=round(float(obyektler.balans) + kart_mebleqi,2)
            pass
        else:
            umumi_balansim=kart_mebleqi
        data={
            'ad':obyektler.ad,
            'soyad':obyektler.soyad,
            'balans':obyektler.balans,
            'ckod':obyektler.ckod,
            'kartlar':card.objects.all().filter(CK=obyektler.ckod,status=True),
            'kart_sayi':card.objects.all().filter(CK=obyektler.ckod).count(),
            'kart_mebleqi':kart_mebleqi,
            'umumi_balansim':umumi_balansim
            }
        if status==True:
#            eyer user aktivdirse
            data['status']=True
        return render(request,'kabinet.html',data)
    else:
#        eyer user passivdirse
        return redirect('/')
            
        
#    	data={
#        'ad':obyektler.ad,
#        'ckod':ckod,
#        'soyad':obyektler.soyad,
#        'balans':obyektler.balans,
#        'kartlar': card.objects.all().filter(CK=ckod,status=True),
#        'kart_sayi':card.objects.all().filter(CK=ckod).count(),
#        'kart_mebleqi':round(card.objects.filter(CK=ckod).aggregate(Sum('amount'))['amount__sum'],3),
#        'umumi_balansim':round(round(card.objects.filter(CK=ckod).aggregate(Sum('amount'))['amount__sum'],3)+float(obyektler.balans),3)
#        
#        }

def cixis_et(request):
    del request.session['login']
    return redirect('/')

# Create your views here.

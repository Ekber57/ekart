from django.shortcuts import render,redirect
from register.models import user
from register.my_modul import nomre_yoxla

import re
def index(request):
    if 'login' in request.session:
#        sessya varsa
        obyekt=user.objects.get(login=request.session['user_login'])
        balans=obyekt.balans
        ck=obyekt.ckod
        status=obyekt.status
        if status ==True:
#            eyer status aktivdirse
            data={
                    'balans':balans,
                    'CK':ck
                    }
            return render(request,'pul_gonder.html',data)
        else:
#            eyer status passivdirse
            return redirect('/office')
    else:
#        sessya yoxsa
        return redirect('/')
        
        



def transfer(request):
    if request.method=="POST":
        #eyer  method postdursa
        if 'login' in request.session:
            data={
                 'CK':user.objects.get(login=request.session['user_login']).ckod,
                }
#            eyer sessiya varsa
            gck=request.POST.get('GCK')
            gpm=request.POST.get('GPM')
            
            
            if gck and gpm:
                if nomre_yoxla(gck):
    #                eyer post olundusa
                    sender=request.session['user_login']
                    sender_balans=user.objects.get(login=sender).balans
                    CK=user.objects.get(login=sender).ckod
    #                data['CK']=CK
                    data['balans']=sender_balans
                    send_to=user.objects.filter(ckod=gck)
                    if send_to:
    #                    eyer cuzdan varsa
                        if re.search('[^A-Za-z\W]',gpm) and re.search('[^A-Za-z\W]',gck):
                            gpm=float(request.POST.get('GPM'))
                            if gpm > float(sender_balans):
        #                        eyer gonderilen pul balansda yoxdursa
                                data['alert']='balansda kifayet qeder vesait yoxdur!'
                                return render(request,'pul_gonder.html',data)
                            else:
        #                        eyer pul varsa
                                if float(gpm) >=0.1:
        #                            eyer pul 20 qepikden boyukduse
                                    if gck != CK:
                                        sender_obyekt=user.objects.get(login=sender)
                                        sender_obyekt.balans=str(round(float(sender_obyekt.balans)-float(gpm),2))
                                        sender_obyekt.save()
                                        send_to=user.objects.get(ckod=gck)
                                        send_to.balans=str(round(float(send_to.balans)+float(gpm),2))
                                        send_to.save()
                                        data['alert']='tebrikler vesait gonderildi!'+str(gpm)
                                        return render(request,'pul_gonder.html',data)
                                    else:
                                        data['alert']='siz oz cuzdaniniza pul gondere bilmezsiniz'
                                        return render(request,'pul_gonder.html',data)
                                        
                                else:
        #                            eyer pul 10 qepikden kicikdise
                                    data['alert']='gonderilen pul minimum 10 qepik ola biler'
                                    return render(request,'pul_gonder.html',data)
                        else:
    #                        eyer duzgun daxil etme yoxdursa
                            data['alert']='aqzina geleni reqem yerne yazma'
                            return render(request,'pul_gonder.html',data)
                        
                            
                    else:
    #                    eyer cuxdan yocdursa
                        data['alert']='cuzdan tapilmadi'
                        return render(request,'pul_gonder.html',data)
                    
                    pass
                else:
                    data['alert']='cuzdan kodu sehvdir'
                    return render(request,'pul_gonder.html',data)
                
#                >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            else:
#                eyer post yoxdursa 
                data['alert']='melumatlari tam doldurun'
                return render(request,'pul_gonder.html',data)
            
            
            
        else:
#            eyer sessiya yoxdusa
            return redirect('/')
    else:
#        metod getdirse
	    return redirect('/')
		    
# Create your views here.
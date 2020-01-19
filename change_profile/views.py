from django.shortcuts import render,redirect
from register.models import user
from register.form_manager import form_manager
def index(request):
    if 'login' in request.session:
#        eyer sessya varsa
        obyekt=user.objects.get(login=request.session['user_login'])
        status=obyekt.status
        if status == True:
#            eyer user aktivdirse
            data={
                'sesya':True,
                'ckod': obyekt.ckod,
                'cari_mail':obyekt.mail,
                'cari_nomre':obyekt.nomre
                }
            return render(request,'change_profile.html',data)
        else:
#            eyer user passivdirse
            return redirect('/office')
    else:
#        eyer sesya yoxdursa 
        pass
# Create your views here.
def change(request):
    if 'login' in request.session:
#        eyer sessya varsa
        obyekt=user.objects.get(login=request.session['user_login'])
        data={
            'sesya':True,
            'ckod':obyekt.ckod,
            'cari_mail':obyekt.mail,
            'cari_nomre':obyekt.nomre
            }
        status=obyekt.status
        if status == True:
            
#            eyer user aktivdirse
            fm=form_manager()
            if request.method  == 'POST':
#                eyer metod postdursa
                mail=request.POST.get('mail')
                nomre=request.POST.get('nomre')
                if mail and nomre:
#                    eyer post varsa
                    if fm.mail(mail):
#                        eyer mail duzdurse 
                        if fm.nomer(nomre):
#                            eyer nomre duzdurse et
                            if not user.objects.filter(mail=mail.lower()):
#                                eyer mail yoxdusa
                                if not user.objects.filter(nomre=nomre):
#                                    eyer nomre yoxdursa
                                    obyekt.mail=mail.lower()
                                    obyekt.nomre=nomre
                                    obyekt.save()
                                    data['alert']='tesekkur edirik melumatlariniz yenilendi'
                                    return render(request,'change_profile.html',data)
                                else:
#                                    eyer nomre varsa
                                    if user.objects.get(nomre=nomre).ckod == obyekt.ckod:
#                                        eyer cari nomre daxil olunubsa 
                                        data['alert']='cari nömrəni dəyişmək üçün fərqli nömrə daxil edin'
                                        return render(request,'change_profile.html',data)
                                    else:
#                                        eyer cari nomre daxil olunubsa 
                                        data['alert']='mail artıq sistemdə mövcuddur'
                                        return render(request,'change_profile.html',data)
                                        
                                    
                            else:
#                                eyer mail varsa
                                 if user.objects.get(mail=mail.lower()).ckod == obyekt.ckod:
#                                     eyer cari mail daxil olunubsa 
                                     data['alert']='cari maili dəyişmək üçün fərqli mail daxil edin'
                                     return render(request,'change_profile.html',data)
                                 else:
#                                     cari mail daxil olunmayibsa
                                     data['alert']='mail artıq sistemdə mövcuddur'
                                     return render(request,'change_profile.html',data)
                                     
                            
                            
                        else:
#                            eyer nomre sehvdirse
                            data['alert']='nomre duzgun deyil'
                            return render(request,'change_profile.html',data)
                    else:
#                        mail sehvdirse
                        data['alert']='mail duzgun deyil'
                        return render(request,'change_profile.html',data)
                else:
#                    eyer post yoxdursa
                    data['alert']='melumatlari tam doldurun'
                    return render(request,'change_profile.html',data)
            else:
#                eyer metod getdirse
                return redirect('/')
        else:
#            eyer user passivdirse
            return redirect('/')
    else:
        return redirect('/')
#        sesya yoxdursa
        
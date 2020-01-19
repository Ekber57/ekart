from django.shortcuts import render,redirect
from register.models import user
def index(request):
    return render(request,'login.html')
def login(request):
    if request.method=="GET":
        return redirect('/')
    else:
        login=request.POST.get('login')
        sifre=request.POST.get('sifre')
        ob=user.objects.filter(login=login)
        if login and sifre:
             if ob:
                 uspass=user.objects.get(login=login).sifre
                 if uspass == sifre:
                     request.session['login']=True
                     request.session['user_login']=login
                     return redirect('/office')
                 else:
                     return render(request,'login.html',{'alert':'Məlümatlar yanlışdır! Şifrə düzgün deyil!'})
                                    
                                    
                     
                
             else:
                 return render(request,'login.html',{'alert':'Login və ya şifrəniz yanlışdır! İstifadəçi tapılmadı'})
                 
            
        else:
            if not (login or sifre):
                alert='Məlümatları boş buraxmayın!'
                
            return render(request,'login.html',{'alert':alert})
def logout(request):
    if 'login' in request.session:
        del request.session['login']
        return redirect('/')
    else:
        return redirect('/')

# Create your views here.

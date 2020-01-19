from django.db import models

# Create your models here.
class user(models.Model):
	ckod=models.CharField(max_length=15,verbose_name='cüzdan kodu')
	balans=models.CharField(max_length=15,verbose_name='balans')
	ad=models.CharField(max_length=10,verbose_name='ad')
	soyad=models.CharField(max_length=10,verbose_name='soyad')
	login=models.CharField(max_length=10,verbose_name='login')
	mail=models.CharField(max_length=30,verbose_name='mail')
	nomre=models.CharField(max_length=10,verbose_name='nomre')
	sifre=models.CharField(max_length=15,verbose_name='sifre')
	status=models.BooleanField(verbose_name='status')
	def __str__(self):
		return self.login

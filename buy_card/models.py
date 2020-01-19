from django.db import models
class card(models.Model):
	KS=models.CharField(max_length=13,verbose_name="kartın seriası")
	KK=models.CharField(max_length=12,verbose_name="kartın kodu")
	KG=models.CharField(max_length=13,verbose_name="kartı göndərən cüzdan")
	CK=models.CharField(max_length=13,verbose_name="cüzdan kodu")
	amount=models.CharField(max_length=13,verbose_name="kartın məbləği")
	status=models.BooleanField(verbose_name="status")
	def __str__(self):
		return self.KS
	
	
# Create your models here.

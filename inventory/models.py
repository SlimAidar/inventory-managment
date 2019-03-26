from django.db import models


class Category(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name		


class Item(models.Model):
	name 	 = models.CharField(max_length=50)
	category = models.ForeignKey(Category,on_delete=models.CASCADE)
	quantity = models.IntegerField(default=0)

	def __str__(self):
		return self.name



class Transaction(models.Model):
	quantity = models.IntegerField()
	time 	 = models.DateTimeField(auto_now=True)
	item 	 = models.ForeignKey(Item, on_delete=models.CASCADE,blank=False, null=False)
	Client 	 = models.CharField(max_length=300, blank=True, null=True)

	class Meta:
		ordering = ['-id']
			

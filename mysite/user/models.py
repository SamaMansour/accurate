from django.db import models


class Medicine (models.Model):
   name = models.CharField(max_length =120)
   dosage = models.TextField(blank =True, null=True)
   frequancy = models.TextField(blank =True, null=True)
 
  
from django.db import models


# Create your models here.
class Transaction(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    cc_num = models.CharField(max_length=250)
    exp_date = models.CharField(max_length=250)
    cvc_num = models.CharField(max_length=250)

    def __str__(self):
        return "Transaction " + str(self.id)

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])


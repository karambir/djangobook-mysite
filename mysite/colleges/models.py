from django.db import models
from django.contrib.auth.models import User

class allcollege(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1500, verbose_name='College Name')
    address = models.CharField(max_length=2400, blank=True, verbose_name='College Address')
    estd = models.IntegerField(blank=True, verbose_name='Year of Estd') # This field type is a guess.
    class Meta:
        db_table = u'allcollege'

    def __unicode__(self):
        return u'%s' %self.name

class StudentProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email=models.EmailField()
    college = models.ForeignKey(allcollege)
    
    def __unicode__(self):
        return u'%s | %s %s' %(self.user, self.first_name, self.last_name)



    


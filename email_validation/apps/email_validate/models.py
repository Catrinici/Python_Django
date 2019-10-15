from __future__ import unicode_literals
from django.db import models
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class EmailValidate(models.Manager):
    def validate(self,postData):
        if not EMAIL_REGEX.match(postData):
            return False
        else:
            try:
                newemail=Email(emailaddress=postData)
                newemail.save()
            except Exception as e:
                print e
                if str(e).find('not unique'):
                    return 'dup'
                else:
                    return 'error'
            return True

class Email(models.Model):
    emailaddress = models.CharField(max_length=100,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    validate=EmailValidate()
    objects=models.Manager()  #need to ask teacher

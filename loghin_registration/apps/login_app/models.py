from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.
class UserManager(models.Manager):
    def add_user(self, postData):
        errors = []
        if not len(postData['first_name']) > 2:
            errors.append('First name must be at list 2 characters!')
        if not len(postData['last_name']):
            errors.append('Last name must be at list 2 characters!')
        if not len(postData['email']):
            errors.append("Email must be there!")
        if not EMAIL_REGEX.match(postData['email']):
            errors.append('Must have a valid email')
        if len(postData['password']) < 8:
            errors.append("Password must be at least 8 characters long!")
        if not postData['password'] == postData['confirm_password']:
            errors.append('Passwords must match!')

        user = self.filter(email = postData['email'])

        if user:
            errors.append('Email already exists!')

        modelResponse = {}
        #if failed validations , send response to views.py
        print errors
        if errors:
            modelResponse['status'] = False
            modelResponse['errors'] = errors
        #save the user to the DB
        else:
            hashed_password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            user = self.create(first_name = postData['first_name'], last_name = postData['last_name'], email = postData["email"], password = hashed_password)

            modelResponse['status'] = True
            modelResponse['user'] = user

        #send modelResponse to views
        print modelResponse
        return modelResponse

    def check_user(self, postData):
        errors = []
        user = self.filter(email = postData['email'])
        #check to see if user is in DB
        modelResponse = {}
        if user:
            #check for Passwords
            if not bcrypt.checkpw(postData['password'].encode(), user[0].password.encode()):
                errors.append('Invalid email/password combination!')
            #succes login
            else:
                modelResponse['status'] = True
                modelResponse['user_id'] = user[0].id
        else:
            errors.append('Invalid email')
        if errors:
            modelResponse['status'] = False
            modelResponse['errors'] = errors
        return modelResponse

class User(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    email = models.EmailField()
    password = models.CharField(max_length= 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()

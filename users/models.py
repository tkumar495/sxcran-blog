#//************************************************************************//#
#//************************************************************************//#
# Author : Chandan Mahto
# Date : 25-10-2018
# Version : 1.0.0
# Changelog : #v 1.0.0 : +added posts model to store posts and manage them 
#			  #v 1.1.0 : +added comment model to store comments and manage them
#//************************************************************************//#
#//************************************************************************//#

from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

#//************************************************************************//#

class posts(models.Model):
	''' post_heading = VARCHAR field to store the heading of a post of max length 150.
					   cannot be a null or empty value
		post_body = VARCHAR field to store the body of the post.
					cannot be null or empty.
		post_op = Foreign Key which maps the User table to the posts table in a one to many 
				  relationship
	'''
	post_op = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
	post_op_name = models.CharField(max_length=150, null=False, default = "Anonymous")
	post_heading = models.CharField(max_length=150, null=False)
	post_body = models.CharField(max_length = 1000, blank=False)
	post_time = models.DateTimeField(default = datetime.now())
#//************************************************************************//#

class comments(models.Model):
	comment_op = models.ForeignKey(User,on_delete = models.CASCADE, null = True)
	comment_body = models.CharField(max_length=150, null=False)
	comment_post = models.ForeignKey(posts, on_delete = models.CASCADE, null=True)
	comment_time = models.DateTimeField(default = datetime.now())

#//************************************************************************//#
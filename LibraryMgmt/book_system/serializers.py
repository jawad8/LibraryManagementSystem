from dataclasses import fields
from rest_framework import serializers
from . import models
import json

class BooksSerializer(serializers.ModelSerializer):

        class Meta:
            model = models.BOOKS
            fields = '__all__'


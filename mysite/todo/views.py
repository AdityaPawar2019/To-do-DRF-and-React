from django.shortcuts import render
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.generics import GenericAPIView
from rest_framework import mixins

class TodoView(GenericAPIView,mixins.RetrieveModelMixin,mixins.ListModelMixin):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'id'

    def get(self,request,id = None):
        if id:
            return self.retrieve(request)
        else :
            return self.list(request)
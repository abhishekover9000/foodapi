from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.


class OrderView(APIView):
    def get(self, request):
        print(request.user)
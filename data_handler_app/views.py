from django.shortcuts import render
import requests
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Account, Destination
from .serializer import AccountSerializer, DestinationSerializer

#AccoutView performs CRUD operations using inbuild method
class AccountView(viewsets.ModelViewSet):
  queryset = Account.objects.all()
  serializer_class = AccountSerializer

#DestinationView performs CRUD operations using inbuild method
class DestinationView(viewsets.ModelViewSet):
  queryset = Destination.objects.all()
  serializer_class = DestinationSerializer

class DataHandler(APIView):

    def post(self, request):
        #validating the app_token
        secret_token = request.headers.get('CL-X-TOKEN')
        account = Account.objects.filter(app_secret_token=secret_token).first()
        if not account:
            return Response({"error": "Un Authenticate"}, status=status.HTTP_401_UNAUTHORIZED)

        data = request.data
        destinations = Destination.objects.filter(account=account)
        for destination in destinations:
            print(destination.http_method)
            if destination.http_method.lower() == 'get':
                response = requests.get(destination.destination_url, params=data, headers=destination.header)
            elif destination.http_method.lower() in ['post', 'put']:
                response = requests.post(destination.destination_url, json=data, headers=destination.header)

            # check if request was successful
            if response.status_code != 201 and response.status_code != 200:
                return Response({"error": f"Failed to send data to destinationId - {destination.id}"}, status=response.status_code)

        return Response({"message": "Data sent to all destinations successfully"}, status=status.HTTP_200_OK)
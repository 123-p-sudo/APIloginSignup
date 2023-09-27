from logging import raiseExceptions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from account.serializers import  UserRegisterationSerializer,UserLoginSerializer
from django.contrib.auth import authenticate
from account.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from account.serializers import UserProfileSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from django.shortcuts import render
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User



#generate token manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }



class UserRegisterationView(APIView):
        
  renderer_classes = [UserRenderer]

  def post(self,request,format=None):
            serializer = UserRegisterationSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                  user = serializer.save()
                  user.set_password(request.data['password'])
                  user.save()
                  #token = get_tokens_for_user(user)
                  #access_token = token['access']
                  #refresh_token = token['refresh']
                  #print("access_token:" ,access_token)
                  #print("refresh_token:",refresh_token)
                  #return Response({'msg':'Registeration Success','token':token},status=status.HTTP_201_CREATED)
                  token = Token.objects.create(user=user)
                  print(token)
                  return Response({'msg':'Registeration Success',"token":token.key},status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
            #return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
  


class UserLoginView(APIView):
      renderer_classes = [UserRenderer]
      def post(self,request,format=None):
             serializer = UserLoginSerializer(data = request.data)
             if serializer.is_valid(raise_exception=True):
                   email = serializer.data.get('email')
                   password = serializer.data.get('password')
                   user = authenticate(email = email,password=password)
                   if user is not None:
                         token,created = Token.objects.get_or_create(user=user)
                         #refresh_token_login=token['refresh']
                         #access_token_login=token['access']
                         #print("access_token:" ,access_token_login)
                         #print("refresh_token:",refresh_token_login)
                         print(token)

                         return Response({'msg':'Login Success','token':token.key},status=status.HTTP_200_OK)
                   else:
                          return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}},status=status.HTTP_404_NOT_FOUND)
                   

             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
      
     


class UserProfileView(APIView):
      renderer_classes=[UserRenderer]
      permission_classes=[IsAuthenticated]
      authentication_classes=([SessionAuthentication,TokenAuthentication])
      def get(self,request,format=None):
            serializer = UserProfileSerializer(request.user) 
            return Response(serializer.data, status=status.HTTP_200_OK)
      


      






      




             




                         
        



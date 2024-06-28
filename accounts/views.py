from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UserSerializer, VerifyAccountSerializer
from .emails import send_otp_via_email
from .models import User

# Create your views here.
class RegisterAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                send_otp_via_email(serializer.data['email'])
                return Response({
                    'status' : 200,
                    'message' : 'Registration Successful, Check email for OTP',
                    'data' : serializer.data,
                })
            return Response({
                'status' : 400,
                'message' : 'Something went wrong',
                'data' : serializer.errors,
            })

        except Exception as e:
            print(e)
            return Response({
                'status': 500,
                'message': 'Internal Server Error',
                'data': str(e),
            })


class VerifyOTP(APIView):
    def post(self, request):
        try:
            data=request.data
            serializer = VerifyAccountSerializer(data=data)
            if serializer.is_valid():
                email = serializer.data['email']
                otp = serializer.data['otp']                   
                user = User.objects.filter(email=email).first()
                if user is None:
                    return Response({
                        'status': 400,
                        'message': 'Something went wrong',
                        'data': 'invalid email',
                    })

                if user.otp != otp:
                    return Response({
                        'status': 400,
                        'message': 'Something went wrong',
                        'data': 'invalid otp',
                    })

                user.is_verified = True
                user.save()

                return Response({
                    'status': 200,
                    'message': 'Account Verified',
                    'data': {},
                })
            return Response({
                'status': 400,
                'message': 'Something went wrong',
                'data': serializer.errors,
            })
        except Exception as e:
            print(e)
            return Response({
                'status': 500,
                'message': 'Internal Server Error',
                'data': str(e),
            })


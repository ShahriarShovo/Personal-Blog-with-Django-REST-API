from rest_framework.decorators import api_view
from django.contrib.auth import login, authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema
from account.serializers import Login_Serializers



def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


@swagger_auto_schema(method='POST', request_body=Login_Serializers)
@api_view(['POST'])
def admin_login(request):
    if request.method=='POST':
        login_admin=authenticate(request, username=request.POST.get('uep'), password=request.POST.get('password'))
        if login_admin is not None:
            token = get_tokens_for_user(login_admin)
            return Response({'message':'you are logged in Successfully','token':token}, status=status.HTTP_200_OK)
        else:
            return Response({'message':'Your Crediential is not Correct'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response({'message':'Something wrong ! Try again'}, status=status.HTTP_400_BAD_REQUEST)



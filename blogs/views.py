from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view,permission_classes,renderer_classes
from .models import Blogs
from blogs.serializers import Blogs_Serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_swagger import renderers
from drf_yasg.utils import swagger_auto_schema
# Create your views here.



@swagger_auto_schema(method='GET')
@api_view(['GET'])
def retreive_post(request):
    get_posts=Blogs.objects.all()
    blogs_serializers=Blogs_Serializers(get_posts, many=True)
    return Response(blogs_serializers.data, status=status.HTTP_200_OK)


@swagger_auto_schema(method='POST', request_body=Blogs_Serializers)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def write_blog(request):
    
    try:
        if request.method=='POST':
            user=request.user
            get_user_data=Blogs(admin=user)
            blogs_Serializers=Blogs_Serializers(get_user_data,data=request.data)
            if blogs_Serializers.is_valid():
                blogs_Serializers.save()
                return Response({'message':'success'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'message':'error'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
             return Response({'message':'Error'}, status=status.HTTP_400_BAD_REQUEST)
    except :
         return Response({'message':'Error'}, status=status.HTTP_400_BAD_REQUEST)




@swagger_auto_schema(method='PUT', request_body=Blogs_Serializers)
@api_view(['GET','PUT'])
@permission_classes([IsAuthenticated])
def edit_posts(request,pk):
    try:
        item=Blogs.objects.get(pk=pk)
        data=Blogs_Serializers(instance=item, data=request.data)
        if data.is_valid():
            print("Not saved")
            data.save()
            return Response(data.data)
        else:
            return Response(data.errors)

    except:
        return Response({'message':'There are something wrong'}, status=status.HTTP_400_BAD_REQUEST)



@swagger_auto_schema(method='DELETE', request_body=Blogs_Serializers)
#@api_view(['GET','DELETE'])
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_post(request,pk):
    
    try:
        # item=Blogs.objects.get(pk=pk)
        # data=Blogs_Serializers(instance=item, data=request.data)
        delete_post=Blogs.objects.get(pk=pk).delete()
        return Response({'message':'Delete Successfully'}, status=status.HTTP_200_OK)

    except:
        return Response({'message':'There are something wrong'}, status=status.HTTP_400_BAD_REQUEST)



        


   



        


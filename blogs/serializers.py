from rest_framework import serializers
from  blogs.models import Blogs


class Blogs_Serializers(serializers.ModelSerializer):
    username=serializers.CharField(source="admin.username", read_only=True)
    class Meta:
        model=Blogs
        fields=['id','admin' , 'username' ,'blog_name','blog_title','blog_image','blog_body']
        #fields='__all__'
        
        def update(self, instance, validated_data):
            instance.blog_image = validated_data.get("blog_image", instance.blog_image)
            if instance.blog_image == None:
                instance.blog_image=instance.blog_image
                instance.save()
                return instance
            else:
                instance.save()
                return instance
            
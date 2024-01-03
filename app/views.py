from django.shortcuts import render
from rest_framework import status, decorators
from rest_framework.response import Response
from .models import ImageModel
from .imgModel import ImageProcess

@decorators.api_view(["POST"])
def image_upload (request) : 
    try :
        image = request.data.get('image',None)

        if image is None :
            return Response({
                'message' : 'please insert image'
            },status=status.HTTP_400_BAD_REQUEST)
        
        img = ImageModel.objects.create(
            image = image,
        )

        img.save()

        current_img_path = img.image.path

        has_sepia = request.data.get('has_sepia',False)
        has_grayscale = request.data.get('has_grayscale',False)
        brightness = request.data.get('brightness',None)
        contrast = request.data.get('contrast',None)
        saturate = request.data.get('saturate',None)


        process = ImageProcess(
            has_grayscale = has_grayscale,
            has_sepia = has_sepia,
            img_path = current_img_path
        )

        if brightness :
            process.brightness(float(brightness))
        
        if contrast :
            process.contrast(float(contrast))
        
        if saturate :
            process.saturate(float(saturate))


        process.save()

        new_iamge_url = process.get_output()
    
        return Response({
            'image' : new_iamge_url
        },status=status.HTTP_200_OK)
    
    except Exception as error :
        return Response({
            'message' : f'an error accured : {error}'
        },status=status.HTTP_400_BAD_REQUEST)
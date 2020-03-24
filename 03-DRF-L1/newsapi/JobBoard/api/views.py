from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from JobBoard.models import JobOffer
from JobBoard.api.serializers import JobOfferSerializer

################## FUNCTION BASED API VIEW ############
@api_view(['GET','POST'])
def Joblist_Create_API_view(request):
    if request.method=='GET':
        jobs=JobOffer.objects.filter(available=True)
        serializers=JobOfferSerializer(jobs,many=True)
        return Response(serializers.data)

    elif request.method=="POST":
        serializers=JobOfferSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def Jobdetail_Create_API_view(request,pk):
    try:
        job=JobOffer.objects.get(pk=pk)
    except JobOffer.DoesNotExist:
        return Response({'error':{
            "code":404,
            "message":"JobOffer not found"
        }},status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializers=JobOfferSerializer(job)
        return Response(serializers.data)
    elif request.method=='PUT':
        serializers=JobOfferSerializer(job,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.eroors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method=="DELETE":
        job.delete()
        return Response(status=status.HTTP_400_BAD_REQUEST)

################## END ##################
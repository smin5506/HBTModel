from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from .models import HBT
import urllib.request
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def mainPage(request):
	return render(request, 'test/setData.html', {})

@csrf_exempt
def setData(request):
    print("test")
    if request.method == 'POST':
        print("POST GOOD")
        myID = request.POST['ID']
        myLocation = request.POST['Location']
        HBT.Head(HBT_ID=myID, Location = myLocation).save()

        myType = request.POST['Type']
        myDataSequence = request.POST['DataSequence']
        HBT.Body(Type=myType, DataSequence=myDataSequence).save()

        myResult = request.POST['Result']
        myAccuracy = request.POST['Accuracy']
        HBT.Tail(Result=myResult, Accuracy=myAccuracy).save()

        myHeart = request.POST['Heart']
        mySkin = request.POST['Skin']
        myMyo = request.POST['Myo']
        myMic = request.POST['Mic']
        HBT.Bodydata(Heart=myHeart, Skin=mySkin, Myo=myMyo, Mic=myMic).save()

    else:
        print("not POST")

    return HttpResponse("good")

def viewData(request):
	headData = serializers.serialize('json', HBT.Head.objects.all())
	bodyData = serializers.serialize('json', HBT.Body.objects.all())
	tailData = serializers.serialize('json', HBT.Tail.objects.all())
	BodydataData = serializers.serialize('json', HBT.Tail.objects.all())
	dataResult = headData + "%" + bodyData + "%" + tailData + "%" + BodydataData
	return HttpResponse(dataResult, content_type='json')

def searchData(request, mType, mySearchData):
    print("searchData")

    if(mType == "ID") :
        data = HBT.Head.objects.filter(HBT_ID=mySearchData)
        data = serializers.serialize('json',data)

    elif(mType == "Time") :
        #y-m-d, y-m-d
        mtime1, mtime2 = mySearchData.split(",")
        data = HBT.Head.objects.filter(Time__range=[mtime1, mtime2])
        data = serializers.serialize('json',data)

    elif(mType == "Location") :
        data = HBT.Head.objects.filter(Location=mySearchData)

    elif(mType == "Type") :
        data = HBT.Body.objects.filter(Type=mySearchData)

    elif(mType == "DataSequence") :
        data = HBT.Body.objects.filter(DataSequence__breed=['heart'])

    elif(mType == "Result") :
        data = HBT.Tail.objects.filter(Result=mySearchData)

    elif(mType == "Accuraccy") :
        data = HBT.Tail.objects.filter(Accuraccy=mySearchData)

    #return HttpResponse(data, content_type='json')
    return HttpResponse(data)





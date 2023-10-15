from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from InfoData.serializers import InfoModalSerializer

# Create your views here.
def addEntry(request):
    res = {
        'error' : 1,
        'msg' : 'Internal server error'
    }
    try:
        if(request.method == "POST"):
            # add faq details
            data = request.POST
            serializer = InfoModalSerializer(data=request.POST)

            if serializer.is_valid():
                serializer.save()
                res['error'] = 0
                res['msg'] = 'Response been saved successfully.'
            else:
                print(serializer.errors)
                res['error'] = 1
                res['msg'] = 'Resonse is not saved.'
        
        else:
            return render(request, 'entry/add_info_form.html', {})
    except Exception as error:
        res['error'] = 1
        res['msg'] = 'Internal server error'

    return JsonResponse(res)
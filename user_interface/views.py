from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def predict(request):
    state = request.POST['State']
    context = {
        "state":state
    }
    return render(request, 'user_interface/prediction_result.html', context)

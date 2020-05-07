from django.shortcuts import render
from django.http import HttpResponse

drop1_dict = [
    "Uttarakhand","Uttarpradesh",
]

drop2_dict = [
    "Chamoli", "Haridwar", "Pauri",
]

drop3_dict = [
    "Ravi", "Kharif", "Zaid"
]



# Create your views here.
def predict(request):
    state_value = request.POST['State']
    selected_state = drop1_dict[int(state_value)]

    district_value = request.POST['District']
    selected_district = drop2_dict[int(district_value)]

    season_value = request.POST['Season']
    selected_season = drop3_dict[int(season_value)]

    context = {
        "state":selected_state,
        "district":selected_district,
        "season":selected_season,
    }
    return render(request, 'user_interface/prediction_result.html', context)

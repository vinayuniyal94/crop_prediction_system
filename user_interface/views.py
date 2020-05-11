from django.shortcuts import render
from django.http import HttpResponse


# 29 indian states list
drop1_dict = ["Uttarakhand","Uttarpradesh",]

# 13 district of uttrakhand list
drop2_dict = ["Chamoli", "Haridwar", "Pauri",]

# season list
drop3_dict = ["Ravi", "Kharif", "Zaid"]



# predict funtion takes the input from the crop prediction html page than saves it to python variable
def predict(request):
    if 'State' in request.POST:
        state_value = request.POST['State']
    else:
        state_value = False
    selected_state = drop1_dict[int(state_value)]

    if 'District' in request.POST:
        district_value = request.POST['District']
    else:
        district_value = False
    selected_district = drop2_dict[int(district_value)]

    if 'Season' in request.POST:
        season_value = request.POST['Season']
    else:
        season_value = False    
    selected_season = drop3_dict[int(season_value)]

    context = {
        "state":selected_state,
        "district":selected_district,
        "season":selected_season,
    }
    return render(request, 'user_interface/prediction_result.html', context)

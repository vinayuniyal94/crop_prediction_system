from django.shortcuts import render
from django.http import HttpResponse

# importing function for checking the pincode entered is valid or not
from user_interface.checkPincode import check



# 29 indian states list
drop1_dict = ["Uttarakhand","Uttarpradesh",]

# season list
drop3_dict = ["Ravi", "Kharif", "Zaid"]


# predict funtion takes the input from the crop prediction html page than saves it to python variable
def predict(request):
    if 'State' in request.POST:
        state_value = request.POST['State']
    else:
        state_value = False
    selected_state = drop1_dict[int(state_value)]

    if 'pin_code' in request.POST:
        district_value = request.POST['pin_code']
    else:
        district_value = False
    selected_pincode = int(district_value)

    if 'Season' in request.POST:
        season_value = request.POST['Season']
    else:
        season_value = False
    selected_season = drop3_dict[int(season_value)]

    if 'area' in request.POST:
        ar = request.POST['area']
    else:
        ar = False

    if 'cropname' in request.POST:
        cr = request.POST['cropname']
    else:
        cr = False


    context = {
        "State_Name":selected_state,
        #"pincode":selected_pincode,
        "Season":selected_season,
        "Area":ar,
        "Crop":cr,
    }

    b = check(selected_pincode, context)
    #print(b["re"])
    context["Result"] = b["re"]
    if b['boo'] == True:
        return render(request, 'user_interface/prediction_result.html', context)
    else:
        return HttpResponse("user_interface/pinNotFound.html")

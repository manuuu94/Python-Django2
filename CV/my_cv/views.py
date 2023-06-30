from django.http import HttpResponse
from django.shortcuts import render
from . import models
# Create your views here.


def my_cv(request):
    personalData = models.Personal.objects.get(pk=1)
    name = personalData
    phone = personalData.phone
    email = personalData.email
    birthDate = personalData.birthDate
    address = personalData.address
    value = "option1"
    languages = models.Languages.objects.all()
    profileDesc = models.Profile.objects.all()
    workXP = models.WorkXP.objects.all()
    education = models.Education.objects.all()
    skills = models.Skills.objects.all()
    skillDetails = models.skillDetails.objects.all()
    dict = {"data":{"Full Name":name,
            "Phone":phone,
            "E-mail":email,
            "Birthdate":birthDate,
            "Address":address},
            "languages":languages,
            "button":value,
            "description":profileDesc[0],
            "skills":{"skill0":skills[0],"skill1":skills[1],"skill2":skills[2]},
            "skillDetails":{"skill1":{"skill":f"{skillDetails[0]}","yrs":skillDetails[0].yearsPractice},
                            "skill2":{"skill":f"{skillDetails[1]}","yrs":skillDetails[1].yearsPractice},
                            "skill3":{"skill":f"{skillDetails[2]}","yrs":skillDetails[2].yearsPractice},
                            "skill4":{"skill":f"{skillDetails[3]}","yrs":skillDetails[3].yearsPractice},
                            "skill5":{"skill":f"{skillDetails[4]}","yrs":skillDetails[4].yearsPractice},
                            "skill6":{"skill":f"{skillDetails[5]}","yrs":skillDetails[5].yearsPractice},
                            "skill7":{"skill":f"{skillDetails[6]}","yrs":skillDetails[6].yearsPractice},
                            "skill8":{"skill":f"{skillDetails[7]}","yrs":skillDetails[7].yearsPractice},
                            "skill9":{"skill":f"{skillDetails[8]}","yrs":skillDetails[8].yearsPractice},
                            "skill10":{"skill":f"{skillDetails[9]}","yrs":skillDetails[9].yearsPractice},
                            "skill11":{"skill":f"{skillDetails[10]}","yrs":skillDetails[10].yearsPractice}},
            "WorkXP":workXP
            }

    print(workXP[3])
    if request.method == 'POST':
        value = request.POST.get('button')
    dict["button"] = value
    return render(request,'my_cv/manucv.html',context = dict)


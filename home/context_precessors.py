from django.core.mail import send_mass_mail
from validate_email import validate_email
from home.form import ClientRezervationForm
from home.models import ClientRezervation, AdminVacantion
from django.contrib import messages

from datetime import datetime, timedelta

def vacantion(date):
        check_vacantion = AdminVacantion.objects.all()
        
        for check in check_vacantion:
            if check.to_date <= date.date() and check.at_date >= date.date() :
                return True
            else:
                return False


def sendrezervation(request): 
    start_work = 9
    end_work = 17
    if request.method == "POST":
        form = ClientRezervationForm(request.POST, request.FILES)
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        date = request.POST.get("date")
        description = request.POST.get("description")
        try:
            image = request.FILES["image"]
        except:
            image = None
        
        # try:
            # email_validation = validate_email(
            # email_address= email,
            # check_format=True,
            # check_blacklist=True,
            # check_dns=True,
            # dns_timeout=10,
            # check_smtp=True,
            # smtp_timeout=10,
            # smtp_skip_tls=False,
            # smtp_tls_context=None,
            # smtp_debug=False)

        email_validation = True


        
        newdate = datetime.strptime(date, '%Y-%m-%dT%H:%M').strftime("%Y-%m-%d")
        newtime = datetime.strptime(date, '%Y-%m-%dT%H:%M').strftime("%H:%M:00")
        verify_date = ClientRezervation.objects.filter(date = newdate)

        print(newdate)
        print(newtime)

        if start_work > datetime.strptime(newtime, "%H:%M:00").hour or end_work < datetime.strptime(newtime, "%H:%M:00").hour:
            messages.warning(request, "In afara orelor de program")
        elif email_validation:
            if vacantion(datetime.strptime(newdate, "%Y-%m-%d")):
                messages.warning(request, "Concediu")
            elif verify_date:
                for v in verify_date:
                    time1 = datetime.strptime(str(v.time),"%H:%M:00")
                    if v.duration:
                        time2 = datetime.strptime(str(v.duration),"%H:%M:00")
                    else:
                        time2 = datetime.strptime("08:00:00","%H:%M:00")
                    time3 = time1 + timedelta(hours = time2.hour, minutes = time2.minute)
                    time4 = datetime.strptime(newtime,"%H:%M:00")

                    if time4 >= time3:
                        if form.is_valid():
                                client = ClientRezervation.objects.create(
                                    name = name,
                                    email = email,
                                    phone = phone,
                                    date = newdate,
                                    time = newtime,
                                    description = description,
                                    image = image
                                )
                                client_msg = ("Sistem", f"Multumesc pentru rezervare. Va voi contacta in cel mai scurt timp pentru confirmare \nDetali rezrevare: \nNume: {name} \nEmail: {email} \nTelefon: {phone}, \nData: {newdate} \nOra: {newtime}", "inktattoo1992@gmail.com", [email])
                                admin_msg = ("Sistem", (f"Aveti un mesaj de la {name}. \nhttp://wazzainktattoo.ro/admin/home/clientrezervation/{client.id}/change/ \nTelefon: {phone}"), "inktattoo1992@gmail.com", ["inktattoo1992@gmail.com"])
                                # send_mass_mail((client_msg, admin_msg),fail_silently=False)
                                # print(client_msg)
                                messages.success(request, "Multumesc pentru rezervare, va voi contacta in cel mai scurt timp")
                                form = ClientRezervationForm
                                
                        else:
                            form = ClientRezervationForm
                            messages.error(request, form.errors)
                    else:
                        messages.warning(request, "Exista o rezervare la aceasta ora, va rugam selectati alta ora sau zi")
            else:

                if form.is_valid():
                        client = ClientRezervation.objects.create(
                            name = name,
                            email = email,
                            phone = phone,
                            date = newdate,
                            time = newtime,
                            description = description,
                            image = image
                        )
                        client_msg = ("Sistem", f"Multumesc pentru rezervare. Va voi contacta in cel mai scurt timp pentru confirmare \nDetali rezrevare: \nNume: {name} \nEmail: {email} \nTelefon: {phone}, \nData: {newdate} \nOra: {newtime}", "inktattoo1992@gmail.com", [email])
                        admin_msg = ("Sistem", (f"Aveti un mesaj de la {name}. \nhttp://wazzainktattoo.ro/admin/home/clientrezervation/{client.id}/change/ \nTelefon: {phone}"), "inktattoo1992@gmail.com", ["inktattoo1992@gmail.com"])
                        # send_mass_mail((client_msg, admin_msg),fail_silently=False)
                        # print(client_msg)
                        messages.success(request, "Multumesc pentru rezervare, va voi contacta in cel mai scurt timp")
                        form = ClientRezervationForm
                        
                else:
                    form = ClientRezervationForm
                    messages.error(request, form.errors)
        else:
            messages.warning(request, "Adresa de email nevalida")
                
        # except BaseException as er:
        #     print(er)
            
    else:
        form = ClientRezervationForm

    return {"form":form}
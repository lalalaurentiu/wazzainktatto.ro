from django_apscheduler.jobstores import DjangoJobStore, register_events
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
from home.models import ClientRezervation
import sys
from django.core.mail import send_mass_mail

def email_announce():
    date =  datetime.now()
    nextday = date + timedelta(days=1)
    clients = ClientRezervation.objects.filter(date = nextday, anounced = True)
    if clients:
        
        for client in clients:
            client_date_rezervation = datetime.strptime(str(client.date), "%Y-%m-%d").strftime("%d-%m-%Y")
            client_msg = ("Sistem", f"Nu uitati ca maine {client_date_rezervation}\n aveti rezervare la ora {client.time}. Pentru orice modificare va rog sa sunati la numarul 0741907328", "inktattoo1992@gmail.com", [client.email])
            admin_msg = ("Sistem", (f"Nu uitati ca pentru maine aveti programat pe {client.name}. \n http://192.168.1.249:35780/admin/home/clientrezervation/{client.id}/change/"), "inktattoo1992@gmail.com", ["inktattoo1992@gmail.com"])
            send_mass_mail((client_msg, admin_msg),fail_silently=False)
            print(client)

def start():
    try:
        scheduler = BackgroundScheduler()
        scheduler.add_jobstore(DjangoJobStore(), "default")
        scheduler.add_job(email_announce, 'interval',name = "server_sends_emails", hours= 24, jobstore='default')
        register_events(scheduler)
        scheduler.start()

        print("Scheduler started...", file=sys.stdout)
    except:
        print("something wrong")

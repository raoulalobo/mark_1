import requests
from celery.decorators import task
from .models import Voyage
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist


@task
def rapport_general( vges , recette, vges_vip , recette_vip, vges_cla , recette_cla  ) :

    message = 'Rapport general :\n Total:{}Vges,{}FCFA\n VIP:{}Vges,{}FCFA\n Cla:{}Vges,{}FCFA '.format( vges , recette, vges_vip , recette_vip, vges_cla , recette_cla   )
    payload = {'action': 'sendmessage', 'username': 'FINEXS', 'password': 'Finexs12345', 'recipient': '237697509899' , 'messagetype':'SMS:TEXT', 'messagedata':message}
    r = requests.get("http://api.vassarl.com:9501/api", params=payload)

    print('retour {}'.format(r))


@task
def rapport_yde( vges_yde, recette_yde, vges_yde_vip, recette_yde_vip ,vges_yde_cla , recette_yde_cla  ) :

    message = 'Rapport Yaounde :\n Yde:{}Vges,{}FCFA\n YdeVIP:{}Vges,{}FCFA\n YdeCla:{}Vges,{}FCFA'.format( vges_yde, recette_yde, vges_yde_vip, recette_yde_vip ,vges_yde_cla , recette_yde_cla  )
    payload = {'action': 'sendmessage', 'username': 'FINEXS', 'password': 'Finexs12345', 'recipient': '237697509899' , 'messagetype':'SMS:TEXT', 'messagedata':message}
    r = requests.get("http://api.vassarl.com:9501/api", params=payload)

    print('retour {}'.format(r))

@task
def rapport_dla(  vges_dla, recette_dla, vges_dla_vip, recette_dla_vip ,vges_dla_cla , recette_dla_cla ) :

    message = 'Rapport Douala :\n Dla:{}Vges,{}FCFA\n DlaVIP:{}Vges,{}FCFA\n DlaCla:{}Vges,{}FCFA'.format( vges_dla, recette_dla, vges_dla_vip, recette_dla_vip ,vges_dla_cla , recette_dla_cla )
    payload = {'action': 'sendmessage', 'username': 'FINEXS', 'password': 'Finexs12345', 'recipient': '237697509899' , 'messagetype':'SMS:TEXT', 'messagedata':message}
    r = requests.get("http://api.vassarl.com:9501/api", params=payload)

    print('retour {}'.format(r))
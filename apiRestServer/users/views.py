# Importar modulos
from django.http import JsonResponse
from django.http import HttpResponse



def loginUser(request):
    user = {
        'id': 1,
        'login': 'lgalicia',
        'toke': 'djhjsduhhjjsd73u43id8u38dh38ru47h8327gf'
    }
    return JsonResponse({'user': user})

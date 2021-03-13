from django.http import HttpResponse

def get_transaction(request, id=None):
    message = f'You entered ID {id}'
    return HttpResponse(message)

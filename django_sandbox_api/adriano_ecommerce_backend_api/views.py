from django.http import JsonResponse

def index(request):
    json_response = {"okay":"okay"}
    return JsonResponse(json_response)
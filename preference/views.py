from django.http import JsonResponse
from .models import Preference
import json

def add_preference(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        name = data.get('name')
        value = data.get('value')

        if username and name and value:
            preference = Preference.objects.create(user__username=username, name=name, value=value)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'error': 'Missing username, name, or value'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
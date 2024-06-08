# # authentication/views.py
# from django.http import JsonResponse
# from django.views.decorators.http import require_GET, require_http_methods
# from authentication.models import CustomUser
# from authentication.serializers import CustomUserSerializer
# from django.core.exceptions import ValidationError

# @require_GET
# def get_user_profile(request, user_id):
#     user = CustomUser.objects.get(pk=user_id)
#     serializer = CustomUserSerializer(user)
#     return JsonResponse(serializer.data)

# @require_http_methods(["PUT"])
# def update_user_profile(request):
#     try:
#         user_id = request.data.get('user_id')  # Assuming request.data for PUT method
#         print(user_id)
#         user = CustomUser.objects.get(pk=user_id)
#         serializer = CustomUserSerializer(user, data=request.data, partial=True)
        
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse({'msg': 'User updated successfully'})
#         else:
#             return JsonResponse(serializer.errors, status=400)
        
#     except CustomUser.DoesNotExist:
#         return JsonResponse({'msg': 'Error: User Not Found!'}, status=400)
#     except ValidationError as e:
#         return JsonResponse({'errors': [{'msg': str(e)}]}, status=400)
   
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_http_methods
from authentication.models import CustomUser
from authentication.serializers import CustomUserSerializer
from django.core.exceptions import ValidationError

@require_GET
def get_user_profile(request, email):
    try:
        user = CustomUser.objects.get(email=email.lower())  # Ensure case-insensitivity
        serializer = CustomUserSerializer(user)
        return JsonResponse(serializer.data)
    except CustomUser.DoesNotExist:
        return JsonResponse({'msg': 'Error: User Not Found!'}, status=400)

@require_http_methods(["PUT"])
def update_user_profile(request):
    try:
        email = request.data.get('email')  # Assuming email in request data
        if not email:
            return JsonResponse({'msg': 'Missing email in request data'}, status=400)

        user = CustomUser.objects.get(email=email.lower())
        serializer = CustomUserSerializer(user, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'msg': 'User updated successfully'})
        else:
            return JsonResponse(serializer.errors, status=400)
        
    except CustomUser.DoesNotExist:
        return JsonResponse({'msg': 'Error: User Not Found!'}, status=400)
    except ValidationError as e:
        return JsonResponse({'errors': [{'msg': str(e)}]}, status=400)

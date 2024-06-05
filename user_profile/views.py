# authentication/views.py
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_http_methods
from authentication.models import CustomUser
from django.core.exceptions import ValidationError
@require_GET
def get_user_profile(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    data = {
        'id': user.pk,
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'phone_number': user.phone_number,
        'address': user.address,
        'gender': user.gender,
        'age': user.age,
        'credit_info': user.credit_info,
        'preference': user.preference,
        'created_at': user.created_at,
        'updated_at': user.updated_at,
    }
    return JsonResponse(data)

@require_http_methods(["PUT"])
def update_user_profile(request):
    try:
        user_id = request.data.get('user_id')  # Assuming request.data for PUT method
        user = get_object_or_404(CustomUser, pk=user_id)
        
        # Assuming you receive updated profile data in the request data
        user.username = request.data.get('user_name', user.username)
        user.email = request.data.get('email', user.email)
        user.phone_number = request.data.get('phonenumber', user.phone_number)
        
        # Validate email format
        if not user.email:
            raise ValidationError("Please enter a valid email")

        # Assuming you have a custom validation method for phonenumber
        if not user.phone_number:
            raise ValidationError("Please enter a valid phone number")

        # Check if the email is allowed to change
        if request.data.get('email') != user.email:
            return JsonResponse({'errors': [{'msg': "Email Is Not Allowed to Change!"}]}, status=400)

        # If password is provided, hash and update
        if request.data.get('password'):
            user.set_password(request.data.get('password'))

        user.save()
        
        return JsonResponse({'msg': 'User updated successfully'})

    except CustomUser.DoesNotExist:
        return JsonResponse({'msg': 'Error: User Not Found!'}, status=400)
    except ValidationError as e:
        return JsonResponse({'errors': [{'msg': str(e)}]}, status=400)
    except Exception as e:
        return JsonResponse({'msg': 'Server Error'}, status=500)  
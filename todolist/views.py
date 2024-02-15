from rest_framework import viewsets
from .serializers import UserSerializers
from .models import User
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import json




class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers

@csrf_exempt
def delete_user_by_id(request, user_id):
    if request.method == 'DELETE':
        user = get_object_or_404(User, id=user_id)
        user.delete()
        return JsonResponse({'success': True, 'message': 'User deleted successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

def get_user_by_id(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        serialized_user = UserSerializers(user)  # Assuming you have a serializer for your User model named UserSerializer
        return JsonResponse({'success': True, 'user': serialized_user.data})
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    
@csrf_exempt
def update_user_by_id(request, user_id):
    if request.method == 'PUT':
        user = get_object_or_404(User, id=user_id)
        data = json.loads(request.body)
        
        # Update the user object based on the data received in the request body
        user.Name = data.get('Name', user.Name)
        user.City = data.get('City', user.City)
        user.Email = data.get('Email', user.Email)
        user.Phone = data.get('Phone', user.Phone)
        user.Post = data.get('Post', user.Post)


        user.save()
        
        return JsonResponse({'success': True, 'message': 'User updated successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
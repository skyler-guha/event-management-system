from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
import json

from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm


@ensure_csrf_cookie
@require_http_methods(['GET'])
def set_csrf_token(request):
    """
    We set the CSRF cookie on the frontend.
    """
    return JsonResponse({'message': 'CSRF cookie set'})


@require_http_methods(['POST'])
def register(request):
    """Register a new user on the database.

    Args:
        request (dict): request info.

    Returns:
        dict: Conformation that the user was registered.
    """
    data = json.loads(request.body.decode('utf-8'))
    form = CreateUserForm(data)
    if form.is_valid():
        form.save()
        return JsonResponse({'success': 'User registered successfully'}, status=201)
    else:
        errors = form.errors.as_json()
        return JsonResponse({'error': errors}, status=400)


@require_http_methods(['POST'])
def login_view(request):
    """Mark the user as logged in on the backend.

    Args:
        request (dict): request info.

    Returns:
        dict: Conformation that the user was logged in.
    """
    try:
        data = json.loads(request.body.decode('utf-8'))
        username = data['username']
        password = data['password']
    except json.JSONDecodeError:
        return JsonResponse(
            {'success': False, 'message': 'Invalid JSON'}, status=400
        )

    user = authenticate(request, username=username, password=password)

    if user:
        login(request, user)
        return JsonResponse({'success': True})
    return JsonResponse(
        {'success': False, 'message': 'Invalid credentials'}, status=401
    )

@require_http_methods(['POST'])
def logout_view(request):
    """logout the user on the backend.

    Args:
        request (dict): request info.

    Returns:
        dict: Conformation that the user was logged out.
    """
    logout(request)
    return JsonResponse({'message': 'Logged out'})


@require_http_methods(['GET'])
def user(request):
    """Get details about the user.

    Args:
        request (dict): request info.

    Returns:
        dict: user details if user is authenticated.
    """
    if request.user.is_authenticated:
        return JsonResponse(
            {'username': request.user.username, 
             'email': request.user.email,
             'role': request.user.role}
        )
    return JsonResponse(
        {'message': 'Not logged in'}, status=401
    )





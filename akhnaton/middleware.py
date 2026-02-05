# akhnatonco/middleware.py
from django.shortcuts import redirect
from django.urls import reverse

class RestrictAdminAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # امنع الوصول للـ /admin/ إلا للمصرح لهم
        if request.path.startswith('/admin/'):
            if not request.user.is_authenticated or not (request.user.username in ['farid', 'reham']):
                return redirect(reverse('notFound'))

        response = self.get_response(request)
        return response
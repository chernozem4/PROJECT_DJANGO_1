from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest
class BillMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            # Check if the user has a related profile
            profile = getattr(request.user, 'employeeprofile', None)
            if profile and not profile.salary:
                # Logic to assign salary based on developer level
                if profile.level == 'junior':
                    profile.salary = 500
                elif profile.level == 'middle':
                    profile.salary = 1000
                elif profile.level == 'senior':
                    profile.salary = 3000
                profile.save()

        return None
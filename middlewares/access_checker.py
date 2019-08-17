# from django.http import HttpResponseRedirect
# from django.shortcuts import render_to_response
# from django.conf import settings
# from django.urls import reverse
#
#
# class AccessUsers:
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         if request.user.is_authenticated:
#             # check if user is operator
#             operator = is_user_operator(request.user)
#             if operator:
#                 if request.user.operator.operator == 1:
#                     if request.path not in settings.OPERATOR1_WHITE_LIST:
#                         return render_to_response("errors.html")
#                 elif request.user.operator.operator == 2:
#                     if request.path not in settings.OPERATOR2_WHITE_LIST:
#                         return render_to_response("errors.html")
#                 elif request.user.operator.operator == 3:
#                     if request.path not in settings.OPERATOR3_WHITE_LIST:
#                         return render_to_response("errors.html")
#                 elif request.user.operator.operator == 4:
#                     if request.path not in settings.OPERATOR4_WHITE_LIST:
#                         return render_to_response("errors.html")
#             superuser = is_user_superuser(request.user)
#             if superuser:
#                 pass
#                 # return HttpResponseRedirect(reverse("root.employee.list"))
#             partner = is_user_partner(request.user)
#             if partner:
#                 pass  # user is partner
#             employee = is_user_employee(request.user)
#             if employee:
#                 pass  # user is employee
#         # else:
#         #     return render_to_response("errors.html")
#         response = self.get_response(request)
#         return response
#
#
# def is_user_operator(user):
#     if hasattr(user, "operator"):
#         return True
#     return False
#
#
# def is_user_superuser(user):
#     if user.is_superuser:
#         return True
#     return False
#
#
# def is_user_partner(user):
#     if hasattr(user, "partner"):
#         return True
#     return False
#
#
# def is_user_employee(user):
#     if hasattr(user, "employee"):
#         return True
#     return False

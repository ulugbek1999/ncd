from django.http import HttpResponse


class OperatorMixin:
	def dispatch(self, request, *args, **kwargs):
		if not hasattr(request.user, 'operator'):
			return HttpResponse("user has no operator")
		return super().dispatch(request, *args, **kwargs)

from django.views.generic import TemplateView
from django.db.models import Count
from .models import APIUsage

class AnalyticsDashboardView(TemplateView):
    template_name = 'analytics/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_requests'] = APIUsage.objects.count()
        context['requests_by_endpoint'] = APIUsage.objects.values('path').annotate(count=Count('id')).order_by('-count')[:10]
        context['requests_by_method'] = APIUsage.objects.values('method').annotate(count=Count('id'))
        context['requests_by_status'] = APIUsage.objects.values('status_code').annotate(count=Count('id'))
        return context

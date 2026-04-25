from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def admin_dashboard(request):
    # ప్రస్తుతానికి డమ్మీ డేటా, తర్వాత దీన్ని డేటాబేస్ నుండి తెద్దాం
    context = {
        'total_leads': 150,
        'pending_tasks': 12,
        'active_projects': 5
    }
    return render(request, 'dashboard/index.html', context)
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from taarifa_config.models import TaarifaConfig

class CheckConfigSet(object):
    def process_request(self, request):
        count = TaarifaConfig.objects.count()
        redirect_url = reverse('taarifa_config:setup')
        login_url = getattr(settings, 'LOGIN_URL', '/accounts/login/')
        logout_url = '/accounts/logout/'
        if not request.path in [redirect_url, login_url, logout_url] and not count and request.user.has_perm('taarifa_config.add_taarifaconfig'):
            return HttpResponseRedirect(redirect_url)

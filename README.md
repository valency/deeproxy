# Deepera Django Proxy System
To install, add the following items to your Django settings:
- `deeproxy` to `INSTALLED_APPS`

To enable access, add the following code to your url patterns:
```
url(r'proxy/', include('deeproxy.urls'))
```

To show docs, add the following code to your urls:
```
from rest_framework.documentation import include_docs_urls
  
urlpatterns = [
    url(r'docs/', include_docs_urls('API Docs'))
]
```

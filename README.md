# Python-CS-Geeks Project
1.Project Start steps
⇒ to create  a virtual environment 
	# python -m venv .venv
⇒ to activate 
	#.venv\Scripts\activate
⇒ pip freeze > requirements.txt  (containing all currently installed packages and their versions)
	#pip freeze > requirements.txt

⇒ to istalll django
	#pip install django
⇒ to create a app 
	#django-admin startproject …name……..
⇒ Create migrations for changes
	#python manage.py makemigrations
	#python manage.py migrate
⇒to create a superuser 
	#python manage.py createsuperuser

2.Configure setting .py
	⇒ media query
	#  MEDIA_URL = '/media/'
     MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

3. Configure static file 
	STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

4. urls.py
	from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #...
    #...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

5. 'DIRS': [os.path.join(BASE_DIR,'templates')],

6  Create app 
	python manage.py startapp tweet

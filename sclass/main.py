#uv init sclass (buat folder baru namanya sclass)
#cd sclass (masuk ke folder = change directory)
#cd .. (utk keluar ke folder lebih luar)
#git branch -M main
#git add . (add semua file python)
#git commit -m "first commit" 
#git remote add origin https://github.com/JenniGwen/sclass.git
#git push -u origin main

#clear (to clear git bash)

#cd sclass/
#cd . (beda sm cd ..)
#uv add django

#DJANGO
#uv run django-admin startproject sclassdev
#uv run django-admin startapp app_landing
#uv run django-admin startapp app_blog
#uv run manage.py runserver

#click linknya di git bash
#delet files in app_landing (intinya hrs ada apps, views and init.py)
#bikin folder baru templates/add_landing dlm add_landing folder (buat file html baru)

#YANG BAKAL KITA PELAJARIN
#1. Create CRUD App
#2. Basic security
#3. Penetration testing
#4. Load test
#5. Deployment (Docker, Kubernetes)
#xss script

#chatgpt pakai kubernetes
#bisa store lbh dari 1000 container (or apps), so chatgpt can be run di seluruh dunia
#chatgpt has kubernetes scaling to 7500 nodes

def main():
    print("Hello from sclass!")


if __name__ == "__main__":
    main()

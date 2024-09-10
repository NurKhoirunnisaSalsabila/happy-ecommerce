**TUGAS 2**

**No.1 Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

Proses Pembuatan Proyek Django dan Inisiasi Proyek Django
1. Membuat direktori baru dengan nama ```happy-skin``` pada dekstop.
2. Membuka folder happy-skin dalam VSCode, kemudian membuka terminal shell (unix) atau git bash.
3. Buat virtual environment dengan menjalankan command berikut:
 
   ```python -m venv env```
5. Mengaktifkan atau menyalakan virtual environment Python baru dengan command:
   
   ```env\Scripts\activate```
7. Mempersiapkan _Dependencies_ dengan cara membuat ```requirements.txt``` pada direktori ```happy-skin``` kemudian menambahkan isi _dependencies_
  ```
   django
   gunicorn
   whitenoise
   psycopg2-binary
   requests
   urllib3
  ```
8. Lanjutkan dengan melakukan instalasi ```requirements``` dengan command berikut:

   ```pip install -r requirements.txt```
9. Membuat Proyek Django dengan nama ```happy_skin``` dengan command berikut:

   ```django-admin startproject happy_skin .```
10. Menambahkan string ```ALLOWED_HOSTS = ["localhost", "127.0.0.1"]``` pada ```ALLOWED_HOSTS``` di
    ```settings.py```
12. Membuat aplikasi ```main``` dengan command:
    ```python manage.py startapp main```
13. Menjalankan server django dengan command berikut:

    ```python manage.py runserver```
14. Menambahkan nama aplikasi ke ```INSTALLED_APPS``` pada file ```settings.py``` di direktori ```happy-skin```
15. Me-_routing_ url pada file ```urls.py``` di direktori ```happy-skin``` sehingga isi file ```urls.py``` sekarang menjadi:
    ```
    from django.contrib import admin
    from django.urls import path, include
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('main.urls')),
    ]
16. Mengubah models.py menjadi:
     ```
    from django.db import models

    class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    ```
17. Melakukan migrasi dengan command:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
18. Membuat direktori templates dan template ``html`` untuk laman ``main``:
    ```
      <h1>{{ app_name }} Happy Skin </h1>
      <h5>Name: </h5>
      <p>{{ name }}<p>
      <h5>NPM: </h5>
      <p>{{ npm }}<p>  
      <h5>Class: </h5>
      <p>{{ class }}<p>
    ```
19. Menambahkan fungsi untuk me-_render_ laman main pada file ``views.py`` di direktori ``main``:
    ```
      from django.shortcuts import render

      def show_main(request):
          context = {
              'app name': 'Happy Ecommerce',
              'name': 'Nur Khoirunnisa Salsabila',
              'npm' : '2306165534',
              'class': 'PBP A'
          }

          return render(request, "main.html", context)
    ```
20. Melakukan _routing_ pada aplikasi ``main`` pada file ``urls.py`` di direktori ``main``:
    ```
    from django.urls import path
    from main.views import show_main
    
    app_name = 'main'
    
    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```
21. Mencoba menjalankan aplikasi pada _localhost_ dengan command:
    ```python manage.py runserver```
22. Membuat repository GitHub baru dengan nama ```happy-skin``` dan visibilitas publik.
23. Menginisiasi direktori lokal ```happy-skin``` sebagai repositori Git
24. Menambahkan berkas ``.gitignore`` dan mengisinya dengan teks berikut:

```
  # Django
  *.log
  *.pot
  *.pyc
  __pycache__
  db.sqlite3
  media
  
  # Backup files
  *.bak
  
  # If you are using PyCharm
  # User-specific stuff
  .idea/**/workspace.xml
  .idea/**/tasks.xml
  .idea/**/usage.statistics.xml
  .idea/**/dictionaries
  .idea/**/shelf
  
  # AWS User-specific
  .idea/**/aws.xml
  
  # Generated files
  .idea/**/contentModel.xml
  .DS_Store
  
  # Sensitive or high-churn files
  .idea/**/dataSources/
  .idea/**/dataSources.ids
  .idea/**/dataSources.local.xml
  .idea/**/sqlDataSources.xml
  .idea/**/dynamic.xml
  .idea/**/uiDesigner.xml
  .idea/**/dbnavigator.xml
  
  # Gradle
  .idea/**/gradle.xml
  .idea/**/libraries
  
  # File-based project format
  *.iws
  
  # IntelliJ
  out/
  
  # JIRA plugin
  atlassian-ide-plugin.xml
  
  # Python
  *.py[cod]
  *$py.class
  
  # Distribution / packaging
  .Python build/
  develop-eggs/
  dist/
  downloads/
  eggs/
  .eggs/
  lib/
  lib64/
  parts/
  sdist/
  var/
  wheels/
  *.egg-info/
  .installed.cfg
  *.egg
  *.manifest
  *.spec
  
  # Installer logs
  pip-log.txt
  pip-delete-this-directory.txt
  
  # Unit test / coverage reports
  htmlcov/
  .tox/
  .coverage
  .coverage.*
  .cache
  .pytest_cache/
  nosetests.xml
  coverage.xml
  *.cover
  .hypothesis/
  
  # Jupyter Notebook
  .ipynb_checkpoints
  
  # pyenv
  .python-version
  
  # celery
  celerybeat-schedule.*
  
  # SageMath parsed files
  *.sage.py
  
  # Environments
  .env
  .venv
  env/
  venv/
  ENV/
  env.bak/
  venv.bak/
  
  # mkdocs documentation
  /site
  
  # mypy
  .mypy_cache/
  
  # Sublime Text
  *.tmlanguage.cache
  *.tmPreferences.cache
  *.stTheme.cache
  *.sublime-workspace
  *.sublime-project
  
  # sftp configuration file
  sftp-config.json
  
  # Package control specific files Package
  Control.last-run
  Control.ca-list
  Control.ca-bundle
  Control.system-ca-bundle
  GitHub.sublime-settings
  
  # Visual Studio Code
  .vscode/*
  !.vscode/settings.json
  !.vscode/tasks.json
  !.vscode/launch.json
  !.vscode/extensions.json
  .history
```
25. Melakukan ``add``, ``commit``, dan ``push`` dari direktori repositori lokal.
26. Mengakses halaman PWS dan membuat proyek baru dengan menekan tombol ```Create New Project```. Kemudian, isi ``Project Name`` dengan ``happyskin``, lalu tekan ``Create New Project`` yang ada di bawahnya.
27. Menambahkan URL _deployment_ PWS pada file ``settings.py`` dan bagian ``ALLOWED_HOSTS`` sehingga menjadi:
    ```ALLOWED_HOSTS = ["localhost", "127.0.0.1", "happyskin.pbp.cs.ui.ac.id"]```
28. Menjalankan 3 perintah ini untuk push ke PWS:
    ```
    git remote add pws http://pbp.cs.ui.ac.id/nur.khoirunnisa/happyskin
    git branch -M master
    git push pws master
    ```

**No. 2 Buatlah bagan yang berisi _request client_ ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara ``urls.py``, ``views.py``, ``models.py``, dan berkas ``html``.**
![Untitled](https://github.com/user-attachments/assets/2ae76eab-89fe-4ce8-9b79-954e93050457)



**No. 3 Jelaskan fungsi git dalam pengembangan perangkat lunak!**

Git adalah alat yang membantu pengembang perangkat lunak mengelola dan melacak perubahan kode secara efisien. Dalam sebuah tim, Git memungkinkan setiap anggota untuk bekerja secara mandiri pada berbagai bagian proyek tanpa saling mengganggu. Dengan sistem ini, setiap perubahan yang dilakukan akan tersimpan dalam catatan yang jelas, sehingga memudahkan untuk kembali ke versi sebelumnya jika diperlukan. Git juga mendukung pengembangan paralel dengan fitur branching, yang memungkinkan pengembangan fitur baru secara terpisah sebelum digabungkan kembali ke proyek utama (merge). Git juga sering digunakan bersama dengan alat CI/CD (_Continuous Integration_/_Continuous Deployment_) untuk mengotomatisasi pengujian dan penyebaran kode. Setiap kali kode di-_commit_, CI/CD dapat otomatis menjalankan tes dan menyebarkan versi terbaru aplikasi ke server.
Kemudian, jika terjadi kesalahan atau _bug_ Git memungkinkan pengembang untuk kembali ke versi sebelumnya dari kode yang diketahui berfungsi dengan baik, sehingga dapat mengurangi risiko kehilangan kode atau waktu ketika menghadapi masalah. Lalu, Git adalah sistem kontrol versi terdistribusi, artinya setiap pengembang memiliki salinan lengkap dari seluruh riwayat proyek. Pada Git, setiap perubahan pada kode disertai dengan pesan _commit_ yang mendokumentasikan apa yang telah dilakukan, sehingga memudahkan untuk melacak sejarah pengembangan proyek dan memahami alasan di balik perubahan tertentu.

**No. 4 Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?**

Menurut saya mengapa _framework_ Django yang dijadikan permulaan pembelajaran pengembangan perangkat lunak adalah karena pertama Django punya banyak fitur _built-in _yang siap pakai ('_batteries included_'), sehingga memungkinkan para pemula untuk langsung fokus pada pengembangan aplikasi tanpa perlu menghabiskan banyak waktu untuk mengatur hal-hal dasar. Kedua, Django dikenal memiliki dokumentasi yang sangat lengkap dan mudah dipahami, sehingga akan sangat membantu pemula yang sedang belajar karena mereka bisa dengan cepat menemukan panduan atau contoh penggunaan fitur-fitur yang ada. Ketiga, Django punya pola arsitektur MVT (_Model-View-Template_) yang membantu pemula memahami konsep dasar dalam pengembangan aplikasi web. Keempat, Django digunakan oleh banyak perusahaan besar dan proyek _open-source_, yang berarti belajar Django memberi pemula pengalaman langsung dengan teknologi yang relevan di industri. Kelima, Django memiliki komunitas yang besar dan aktif, sehingga memudahkan pemula untuk mendapatkan bantuan, menemukan tutorial, atau mengakses berbagai pustaka tambahan yang bisa mempercepat proses belajar.

**No. 5 Mengapa model pada Django disebut sebagai ORM?**
Model pada Django disebut sebagai ORM (_Object-Relational Mapping_) karena Django menggunakan teknik pemetaan objek relasional untuk menghubungkan antara tabel dalam basis data relasional (seperti MySQL, PostgreSQL, SQLite, dll.) dengan objek-objek dalam bahasa pemrograman Python. ORM memungkinkan pengembang untuk bekerja dengan data menggunakan objek Python daripada menulis query SQL secara langsung. Sederhananya, ORM Django hanyalah cara untuk membuat SQL secara _pythonic_ untuk mengambil dan memanipulasi data dari database. Kemudian mendapatkan hasil dengan gaya pemrograman Python yang mudah dipahami. 



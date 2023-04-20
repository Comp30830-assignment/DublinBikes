name: comp30830
channels:
  - defaults
dependencies:
  - anyio=3.5.0
  - argon2-cffi=21.3.0
  - argon2-cffi-bindings=21.2.0
  - attrs=22.1.0
  - babel=2.11.0
  - backcall=0.2.0
  - beautifulsoup4=4.11.1
  - blas=1.0
  - bleach=4.1.0
  - bottleneck=1.3.5
  - brotlipy=0.7.0
  - ca-certificates=2023.01.10
  - certifi=2022.12.7
  - cffi=1.15.1
  - charset-normalizer=2.0.4
  - click=8.0.4
  - colorama=0.4.6
  - cryptography=36.0.0
  - debugpy=1.5.1
  - decorator=5.1.1
  - defusedxml=0.7.1
  - entrypoints=0.4
  - fftw=3.3.9
  - flask=2.2.2
  - flit-core=3.6.0
  - greenlet=2.0.1
  - icc_rt=2022.1.0
  - idna=3.4
  - importlib-metadata=4.11.3
  - importlib_metadata=4.11.3
  - importlib_resources=5.2.0
  - intel-openmp=2021.4.0
  - ipykernel=6.15.2
  - ipython=7.31.1
  - ipython_genutils=0.2.0
  - itsdangerous=2.0.1
  - jedi=0.18.1
  - jinja2=3.1.2
  - joblib=1.1.1
  - json5=0.9.6
  - jsonschema=4.17.3
  - jupyter_client=7.4.9
  - jupyter_core=4.11.2
  - jupyter_server=1.23.4
  - jupyterlab=3.5.3
  - jupyterlab_pygments=0.1.2
  - jupyterlab_server=2.19.0
  - libiconv=1.16
  - libprotobuf=3.6.0
  - libsodium=1.0.18
  - libxml2=2.9.14
  - libxslt=1.1.35
  - lxml=4.9.1
  - markupsafe=2.1.1
  - matplotlib-inline=0.1.6
  - mistune=0.8.4
  - mkl=2021.4.0
  - mkl-service=2.4.0
  - mkl_fft=1.3.1
  - mkl_random=1.2.2
  - mysql-connector-c=6.1.11
  - mysql-connector-python=8.0.18
  - mysqlclient=1.3.14
  - nbclassic=0.5.2
  - nbclient=0.5.13
  - nbconvert=6.5.4
  - nbformat=5.7.0
  - nest-asyncio=1.5.6
  - notebook=6.5.2
  - notebook-shim=0.2.2
  - numexpr=2.8.4
  - numpy=1.21.5
  - numpy-base=1.21.5
  - openssl=1.1.1t
  - packaging=22.0
  - pandas=1.3.5
  - pandocfilters=1.5.0
  - parso=0.8.3
  - pickleshare=0.7.5
  - pip=22.3.1
  - pkgutil-resolve-name=1.3.10
  - prometheus_client=0.14.1
  - prompt-toolkit=3.0.36
  - protobuf=3.6.0
  - psutil=5.9.0
  - pycparser=2.21
  - pygments=2.11.2
  - pymysql=1.0.2
  - pyopenssl=22.0.0
  - pyrsistent=0.18.0
  - pysocks=1.7.1
  - python=3.7.6
  - python-dateutil=2.8.2
  - python-fastjsonschema=2.16.2
  - pytz=2022.7
  - pywin32=305
  - pywinpty=2.0.2
  - pyzmq=23.2.0
  - requests=2.28.1
  - scikit-learn=1.0.2
  - scipy=1.7.3
  - send2trash=1.8.0
  - setuptools=65.6.3
  - simplejson=3.17.6
  - six=1.16.0
  - sniffio=1.2.0
  - soupsieve=2.3.2.post1
  - sqlalchemy=1.4.39
  - sqlite=3.40.1
  - terminado=0.17.1
  - threadpoolctl=2.2.0
  - tinycss2=1.2.1
  - tomli=2.0.1
  - tornado=6.2
  - traitlets=5.7.1
  - typing-extensions=4.4.0
  - typing_extensions=4.4.0
  - urllib3=1.26.14
  - vc=14.2
  - vs2015_runtime=14.27.29016
  - wcwidth=0.2.5
  - webencodings=0.5.1
  - websocket-client=0.58.0
  - werkzeug=2.2.2
  - wheel=0.38.4
  - win_inet_pton=1.1.0
  - wincertstore=0.2
  - winpty=0.4.3
  - zeromq=4.3.4
  - zipp=3.11.0
  - zlib=1.2.13
prefix: D:\Softwares\Anaconda\envs\comp30830

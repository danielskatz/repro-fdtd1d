FROM jupyter/scipy-notebook

USER root

RUN apt-get -qq update && \
    apt-get -qq install \ 
        build-essential \
        curl \
        git \
        python-matplotlib \
        vim && \
    apt-get -qq clean all && \
    apt-get -qq autoclean && \
    apt-get -qq autoremove && \
    rm -rf /var/lib/apt/lists/*

USER $NB_USER
ENV USER $NB_USER
COPY fdtd* /home/jovyan/work/
COPY img /home/jovyan/work/img/

RUN /bin/bash -c 'chmod +w /home/jovyan/work/fdtd1d.c'

CMD ["start-notebook.sh", "--NotebookApp.token=''"]

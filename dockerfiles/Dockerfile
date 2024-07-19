FROM jupyterhub/jupyterhub:main

# USER root
RUN apt-get update && apt-get install -y openjdk-11-jdk python3.11 python3.11-venv python3.11-dev

# Create a symlink to ensure 'python3' points to 'python3.11'
RUN ln -sf /usr/bin/python3.11 /usr/bin/python3 && \
    ln -sf /usr/bin/python3.11 /usr/bin/python

    # USER jovyan
RUN pip install pyspark==3.5.1 hdfs jupyter jupyter_core


## ## ## JUPYTERHUB CONFIGURATION ## ## ##
# Copy the user initialization script into the container
COPY ../user_init.sh /usr/local/bin/user_init.sh
RUN chmod +x /usr/local/bin/user_init.sh
RUN /usr/local/bin/user_init.sh

# Prepare Jupyterhub stuff
RUN pip install jupyterhub mysql-connector-python
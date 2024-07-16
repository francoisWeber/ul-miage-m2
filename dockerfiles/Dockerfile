FROM jupyterhub/jupyterhub:latest

# Copy the user initialization script into the container
COPY user_init.sh /usr/local/bin/user_init.sh
RUN chmod +x /usr/local/bin/user_init.sh
RUN /usr/local/bin/user_init.sh

# install some client specific tools
RUN pip install jupyter requests elasticsearch mysql-connector-python pyvespa pyspark


# Install Java
RUN apt-get update && apt-get install -y openjdk-11-jdk

# Download and install Spark
RUN wget https://downloads.apache.org/spark/spark-3.1.2/spark-3.1.2-bin-hadoop3.2.tgz -O /tmp/spark.tgz && \
    tar -xzf /tmp/spark.tgz -C /opt/ && \
    ln -s /opt/spark-3.1.2-bin-hadoop3.2 /opt/spark

# Set environment variables
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV SPARK_HOME=/opt/spark
ENV PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin

# Copy the user initialization script
COPY user_init.sh /usr/local/bin/user_init.sh
RUN chmod +x /usr/local/bin/user_init.sh

# Run the user initialization script
RUN /usr/local/bin/user_init.sh

# The entrypoint to start JupyterHub
CMD ["jupyterhub"]

FROM ubuntu:latest

COPY hello-cron /etc/cron.d/hello-cron
COPY script.py /usr/src/script.py

RUN apt-get update -y && \
    apt-get install python3 -yqq && \
    apt-get -yqq install python3-pip vim curl&& \
    apt-get -yq install cron && \
    apt-get install python3-dev -yq && \
    pip3 install pymongo && \
    touch /var/log/cron.log && \
    chmod 0644 /etc/cron.d/hello-cron && \
    chmod +x /usr/src/script.py && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN /usr/bin/crontab /etc/cron.d/hello-cron
    

# Run the command on container startup
CMD ["cron", "-f"]

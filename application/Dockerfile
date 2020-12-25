FROM nginx:latest
RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get update -y && \
    apt-get dist-upgrade -y && \
    apt-get install --no-install-recommends -y apache2-utils && \
    sed -i "s#localhost;#localhost;auth_basic \"Restricted Access!\";auth_basic_user_file /etc/nginx/.htpasswd;#g" /etc/nginx/conf.d/default.conf && \
    apt-get install -y curl && \
    sed -i "s#/var/log/nginx/error.log#/var/log/nginx/error_nginx.log#g" /etc/nginx/nginx.conf && \
    sed -i "/access_log/d" /etc/nginx/nginx.conf && \
    sed -i "/log_format/,+2d" /etc/nginx/nginx.conf && \
    sed -i "s#sendfile#log_format json_combined escape=json '{' '\"remote_user\":\"\$remote_user\",' '\"time_local\":\"\$time_local\",' '\"status\": \"\$status\"' '}';access_log  /var/log/nginx/access_nginx.log  json_combined;sendfile#g" /etc/nginx/nginx.conf && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
COPY ./.htpasswd /etc/nginx
COPY ./index.html /usr/share/nginx/html
EXPOSE 80
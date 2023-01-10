# production environment
FROM nginx:alpine

WORKDIR /usr/share/nginx/html
# Copies static resources from builder stage
RUN chown -R nginx:nginx /var/cache/nginx && \
        chown -R nginx:nginx /var/log/nginx && \
        chown -R nginx:nginx /etc/nginx/conf.d
RUN touch /var/run/nginx.pid && \
        chown -R nginx:nginx /var/run/nginx.pid

COPY --chown=nginx:nginx devops/docker/proxy/nginx/nginx.conf /etc/nginx/nginx.conf
USER nginx
EXPOSE 8081
CMD ["nginx", "-g", "daemon off;"]

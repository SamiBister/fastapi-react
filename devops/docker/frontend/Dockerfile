FROM node:alpine as build
ENV NODE_ENV production
ENV DISABLE_ESLINT_PLUGIN true

WORKDIR /app

EXPOSE 3000

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# install and cache app dependencies
COPY frontend/package.json frontend/package-lock.json ./

RUN npm install --production

#RUN npm install --silent && npm install react-scripts@3.3.0 -g --silent

COPY frontend/ ./


RUN npm run build


# production environment
FROM nginx:alpine
#FROM nginxinc/nginx-unprivileged
WORKDIR /usr/share/nginx/html
RUN rm -rf ./*
# Remove default nginx static resources
RUN rm /etc/nginx/conf.d/default.conf
# Copies static resources from builder stage
RUN chown -R nginx:nginx /var/cache/nginx && \
        chown -R nginx:nginx /var/log/nginx && \
        chown -R nginx:nginx /etc/nginx/conf.d
RUN touch /var/run/nginx.pid && \
        chown -R nginx:nginx /var/run/nginx.pid

COPY --chown=nginx:nginx --from=build /app/build /usr/share/nginx/html
COPY --chown=nginx:nginx devops/docker/frontend/nginx/nginx.conf /etc/nginx/conf.d/default.conf
USER nginx

EXPOSE 8080
CMD ["nginx", "-g", "daemon off;"]

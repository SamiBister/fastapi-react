# fastapi-react

## Front-end first time

```bash
sudo su
npx create-react-app frontend
frontend/
npm start
```

## Front end after devcontainer start

```bash
npm install
npm start

```


docker run \
 --rm \
 --volume "$PWD/test-robot":/home/robot/tests \
 --volume "$PWD/results":/home/robot/results \
 robotframework/rfdocker:latest \
 tests
google-chrome-stable  --headless --disable-gpu --no-sandbox --remote-debugging-port=4444 https://jippamaommdom.com

## Kube

Edit the host machine /etc/hosts file
Add 127.0.0.1       host.docker.internal

╭─ ~ ─────────────────────────────────────────────────────────────────── ✔ ─╮
╰─ ping host.docker.internal                                                 ─╯
ping: cannot resolve host.docker.internal: Unknown host
##
# Host Database
#
# localhost is used to configure the loopback interface
# when the system is booting.  Do not change this entry.
##
127.0.0.1       localhost
255.255.255.255 broadcasthost
::1             localhost
127.0.0.1       host.docker.internal
# Added by Docker Desktop
# To allow the same kube context to work on the host and the container:
127.0.0.1 kubernetes.docker.internal
# End of section

k3d cluster create my-multinode-cluster --servers 1 --agents 1 --port 9080:80@loadbalancer --port 9443:443@loadbalancer --api-port 6443 --k3s-arg "--no-deploy=traefik@server:*" --agents-memory=8G

k3d cluster create my-playgound  --api-port 6550 -p "8081:80@loadbalancer" --agents 2
k3d cluster create my-playgound --servers 1 --agents 2 --port 8081:80@loadbalancer --port 8443:443@loadbalancer --api-port 6443


k3d cluster create --api-port 6550 -p "8081:80@loadbalancer" --agents 2

Rationale: You cannot set memory in container.

in ~/.kube/config change the 0.0.0.0 to host.docker.internal

## Deployment



helm upgrade --install myapp-instance ./playgound-proxy

helm create playgound-proxy
helm create playgound-front
helm create playgound-backend

proxy 
change in values.yaml intgress to true

ingress:
  enabled: true
  className: ""
  annotations:

 devops/deploy/kubernetes/proxy/playgound-proxy/templates/ingress.yaml


  rules:
    {{- range .Values.ingress.hosts }}
    - host: {{ .host | quote }}
      http:
        paths:

  rules:
    {{- range .Values.ingress.hosts }}
    - http:
        paths:


Enable ingress

k3d cluster create my-test --api-port 6550 -p "8081:80@loadbalancer" --agents 2
k3d cluster delete my-test
k3d cluster create my-playgound --servers 1 --agents 2 --port 8080:80@loadbalancer --port 8081:8081@loadbalancer --port 8082:8082@loadbalancer --port 8443:443@loadbalancer --api-port 6443
k3d cluster delete my-playgound

k3d cluster create my-test --api-port 6550 -p "8081:80@loadbalancer" --agents 2

host.k3d.internal
kubectl create deployment nginx --image=nginx
kubectl create service clusterip nginx --tcp=80:80
kubectl apply -f ingress.yml

kubectl apply -f ing.yml


helm upgrade --install reverse-proxy ./proxy/playgound-proxy
helm upgrade --install reverse-proxy  ./devops/deploy/kubernetes/proxy/playgound-proxy
helm upgrade --install 

docker build -t localhost:12345/proxy:1.0.5 -f devops/docker/proxy/Dockerfile .
docker build -t showcase/front:1.0.0 -f devops/docker/frontend/Dockerfile .
docker build -t localhshowcase/reverse:1.0.0 -f devops/docker/back/Dockerfile .

k3d registry create myregistry.localhost --port 12345
k3d cluster create my-playgound --servers 1 --agents 2 --port 8080:8080@loadbalancer --port 8081:8081@loadbalancer --port 8082:8082@loadbalancer --port 8443:443@loadbalancer --api-port 6443 --registry-use k3d-myregistry.localhost:12345
k3d cluster delete my-playgound

docker run -d -p 8083:5000 --restart=always --name local-registry registry:2
docker run -dp 8084:5000 --restart=always --name registry registry
docker run -dp 5000:5000 --restart=always --name registry registry

helm registry login -u myuser localhost:8083

helm push mychart-0.1.0.tgz oci://localhost:5000/helm-charts

This will start a registry server at localhost:5000.

Use docker logs -f registry to see the logs and docker rm -f registry to stop.

  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=reverse,app.kubernetes.io/instance=reverse" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT


        location /back {
            proxy_pass         http://docker-back;
            port_in_redirect off;
        }

kubectl run -i --tty busybox --image=busybox --restart=Never -- sh

docker build -t localhost:8083/proxy:1.0.0 -f devops/docker/proxy/Dockerfile .
docker push localhost:8083/proxy:1.0.0
# apiVersion: networking.k8s.io/v1beta1 # for k3s < v1.19
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: nginx
  annotations:
    ingress.kubernetes.io/ssl-redirect: "false"
spec:
  rules:
  - http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: nginx
            port:
              number: 80





vscode ➜ /workspace/devops/deploy/kubernetes (main ✗) $ kubectl get ingress myapp-instance-playgound-proxy -o yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  annotations:
    meta.helm.sh/release-name: myapp-instance
    meta.helm.sh/release-namespace: default
  creationTimestamp: "2022-06-18T21:17:16Z"
  generation: 1
  labels:
    app.kubernetes.io/instance: myapp-instance
    app.kubernetes.io/managed-by: Helm
    app.kubernetes.io/name: playgound-proxy
    app.kubernetes.io/version: 1.16.0
    helm.sh/chart: playgound-proxy-0.1.0
  name: myapp-instance-playgound-proxy
  namespace: default
  resourceVersion: "852"
  uid: 345f455c-9a7f-4486-93eb-b11a5e00fe3b
spec:
  ingressClassName: traefik
  rules:
  - host: localhost
    http:
      paths:
      - backend:
          service:
            name: myapp-instance-playgound-proxy
            port:
              number: 80
        path: /
        pathType: Prefix
status:
  loadBalancer: {}
  

  vscode ➜ /workspace/devops/deploy/kubernetes (main ✗) $ kubectl get ingress myapp-instance-playgound-proxy -o yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  annotations:
    ingress.kubernetes.io/ssl-redirect: "false"
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"networking.k8s.io/v1","kind":"Ingress","metadata":{"annotations":{"ingress.kubernetes.io/ssl-redirect":"false"},"name":"myapp-instance-playgound-proxy","namespace":"default"},"spec":{"rules":[{"http":{"paths":[{"backend":{"service":{"name":"myapp-instance-playgound-proxy","port":{"number":80}}},"path":"/","pathType":"Prefix"}]}}]}}
  creationTimestamp: "2022-06-18T21:22:43Z"
  generation: 1
  name: myapp-instance-playgound-proxy
  namespace: default
  resourceVersion: "867"
  uid: 70bb2cde-dc1d-40a2-8891-b41081f77e7f
spec:
  rules:
  - http:
      paths:
      - backend:
          service:
            name: myapp-instance-playgound-proxy
            port:
              number: 80
        path: /
        pathType: Prefix
status:
  loadBalancer:
    ingress:
    - ip: 192.168.32.3
    - ip: 192.168.32.4
    - ip: 192.168.32.5

  wget -q -S -O - http://loki-graphana:3000

  wget -q -S -O - --header='x-token: fake-super-secret-token'  http://api:8000/items/?token=jessica


  customer2-app-127-0-0-1.nip.io

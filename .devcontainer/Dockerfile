# [Choice] Python version (use -bullseye variants on local arm64/Apple Silicon): 3, 3.10, 3.9, 3.8, 3.7, 3.6, 3-bullseye, 3.10-bullseye, 3.9-bullseye, 3.8-bullseye, 3.7-bullseye, 3.6-bullseye, 3-buster, 3.10-buster, 3.9-buster, 3.8-buster, 3.7-buster, 3.6-buster
ARG VARIANT=3.10-buster
FROM mcr.microsoft.com/vscode/devcontainers/python:${VARIANT}
# [Option] Install zsh
ARG INSTALL_ZSH="true"
# [Option] Upgrade OS packages to their latest versions
ARG UPGRADE_PACKAGES="false"
# [Option] Enable non-root Docker access in container
ARG ENABLE_NONROOT_DOCKER="true"
# [Option] Use the OSS Moby Engine instead of the licensed Docker Engine
ARG USE_MOBY="true"
# [Option] Engine/CLI Version
ARG DOCKER_VERSION="latest"

ARG ISTIO_VERSION=1.13.3

ARG TARGET_ARCH=x86_64

# Enable new "BUILDKIT" mode for Docker CLI
ENV DOCKER_BUILDKIT=1
# [Option] Install Maven
ARG INSTALL_MAVEN="false"
ARG MAVEN_VERSION=""
# [Option] Install Gradle
ARG INSTALL_GRADLE="false"
ARG GRADLE_VERSION=""
ARG TERRAFORM_VERSION=latest
ARG TFLINT_VERSION=latest
ARG TERRAGRUNT_VERSION=latest
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID
ARG NODE_VERSION="none"
ARG VERSION=v4.25.1
ARG BINARY=yq_linux_amd64

COPY library-scripts/*.sh /tmp/library-scripts/


RUN if [ "${INSTALL_MAVEN}" = "true" ]; then su vscode -c "umask 0002 && . /usr/local/sdkman/bin/sdkman-init.sh && sdk install maven \"${MAVEN_VERSION}\""; fi \
    && if [ "${INSTALL_GRADLE}" = "true" ]; then su vscode -c "umask 0002 && . /usr/local/sdkman/bin/sdkman-init.sh && sdk install gradle \"${GRADLE_VERSION}\""; fi \
    && if [ "${NODE_VERSION}" != "none" ]; then su vscode -c "umask 0002 && . /usr/local/share/nvm/nvm.sh && nvm install ${NODE_VERSION} 2>&1"; fi



# [Optional] Uncomment this section to install additional OS packages.
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
        && /bin/bash /tmp/library-scripts/common-debian.sh "${INSTALL_ZSH}" "${USERNAME}" "${USER_UID}" "${USER_GID}" "${UPGRADE_PACKAGES}" "true" "true" \
        && /bin/bash /tmp/library-scripts/docker-debian.sh "${ENABLE_NONROOT_DOCKER}" "/var/run/docker-host.sock" "/var/run/docker.sock" "${USERNAME}" "false" \
        && /bin/bash /tmp/library-scripts/kubectl-helm-debian.sh "latest" "latest" "latest" \
        && mkdir -p /home/${USERNAME}/.minikube \
        && chown ${USERNAME} /home/${USERNAME}/.minikube \
    # Use Docker script from script library to set things up
    && apt-get -y install \
        ansible \
        jq \
        postgresql-client \
    && apt-get -y -q autoremove \
    && rm -rf /var/lib/apt/lists/

RUN curl -s https://raw.githubusercontent.com/k3d-io/k3d/main/install.sh | bash \
    && cd /usr/local/bin ; curl -s https://fluxcd.io/install.sh | sudo bash \
    && curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | sh -s -- -b /usr/local/bin \
    && curl -sSfL https://raw.githubusercontent.com/anchore/grype/main/install.sh | sh -s -- -b /usr/local/bin \
    && wget -qO /usr/local/bin/yq https://github.com/mikefarah/yq/releases/latest/download/yq_linux_amd64 \
    && chmod a+x /usr/local/bin/yq

RUN mkdir -p usr/local/aws-cli ; cd /home/${USERNAME};  wget "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -O  "awscliv2.zip" ; unzip awscliv2.zip ;  ./aws/install -i /usr/local/aws-cli -b /usr/local/bin

RUN bash /tmp/library-scripts/terraform-debian.sh "${TERRAFORM_VERSION}" "${TFLINT_VERSION}" "${TERRAGRUNT_VERSION}" \
    && mkdir -p /home/${USERNAME}/.ssh  \
    && mkdir -p /home/${USERNAME}/.aws \
    && mkdir -p /home/${USERNAME}/.kube \
    && rm -rf /tmp/library-scripts

ARG PROVIDER={all,google,aws,kubernetes}

RUN wget "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz"  -O - | tar xz -C /usr/local/bin \
    && cd /usr/local/bin ; curl -LO https://github.com/GoogleCloudPlatform/terraformer/releases/download/$(curl -s https://api.github.com/repos/GoogleCloudPlatform/terraformer/releases/latest | grep tag_name | cut -d '"' -f 4)/terraformer-${PROVIDER}-linux-amd64 \
    && chmod +x /usr/local/bin/terraformer-all-linux-amd64 \
    && chmod +x /usr/local/bin/terraformer-google-linux-amd64  \
    && chmod +x /usr/local/bin/terraformer-kubernetes-linux-amd64   \
    && chmod +x /usr/local/bin/terraformer-aws-linux-amd64  \
    && cd /usr/local/bin ; curl -L https://github.com/cycloidio/terracognita/releases/latest/download/terracognita-linux-amd64.tar.gz -o terracognita-linux-amd64.tar.gz \
    && tar -xf terracognita-linux-amd64.tar.gz \
    && chmod u+x terracognita-linux-amd64 \
    && chown -R ${USERNAME} /home/${USERNAME}

USER ${USERNAME}

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -  \
   && cd $HOME ; curl -L https://istio.io/downloadIstio | ISTIO_VERSION=${ISTIO_VERSION} TARGET_ARCH=${TARGET_ARCH} sh - \
   && cd $HOME ; curl -s https://raw.githubusercontent.com/armosec/kubescape/master/install.sh | /bin/bash


ENV PATH=$PATH:/home/${USERNAME}/istio-1.13.3/bin:/home/${USERNAME}/.poetry/bin
# [Optional] Uncomment this line to install global node packages.
# RUN su vscode -c "source /usr/local/share/nvm/nvm.sh && npm install -g <your-package-here>" 2>&1
VOLUME [ "/var/lib/docker" ]
VOLUME [ "/home/${USERNAME}/.kube" ]
VOLUME [ "/home/${USERNAME}/.ssh" ]
VOLUME [ "/home/${USERNAME}/.gitconfig" ]
VOLUME [ "/home/${USERNAME}/.aws" ]
ENTRYPOINT [ "/usr/local/share/docker-init.sh" ]
CMD [ "sleep", "infinity" ]

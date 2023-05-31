FROM python:3.11-bullseye

# ------------------------- install required packages ------------------------ #
RUN set -eux \
  && apt-get update \
  && apt-get install -y sudo bash bash-completion git vim \
  && apt-get clean

# ------------------------------ install nodejs ------------------------------ #
RUN set -eux \
  && curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
  && apt-get install -y nodejs

# --------------------------- create non root user --------------------------- #
ARG USERNAME=dev
ARG USER_UID=1001
ARG USER_GID=$USER_UID
RUN groupadd --gid $USER_GID $USERNAME \
  && useradd --uid $USER_UID --gid $USER_GID --groups sudo -m $USERNAME \
  && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
  && chmod 0440 /etc/sudoers.d/$USERNAME \
  && chsh -s /bin/bash $USERNAME
USER $USERNAME

# ---------------------------------- poetry ---------------------------------- #
RUN set -eux \
  && cd $HOME \
  && curl -sSL -o install-poetry.py https://install.python-poetry.org \
  && python3 install-poetry.py \
  && rm install-poetry.py
ENV PATH=/home/dev/.local/bin:$PATH
FROM python:3.11-slim-bullseye

# ------------------------- install required packages ------------------------ #
RUN set -eux \
  && apt-get update \
  && apt-get install -y curl \
  && apt-get clean

# ---------------------------------- poetry ---------------------------------- #
RUN set -eux \
  && cd $HOME \
  && curl -sSL -o install-poetry.py https://install.python-poetry.org \
  && python3 install-poetry.py \
  && rm install-poetry.py
ENV PATH=/home/dev/.local/bin:$PATH
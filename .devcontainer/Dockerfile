FROM python:3.12-alpine

ARG ARG_WORKDIR
ENV WORKDIR=${ARG_WORKDIR}

ENV VIRTUAL_ENV=${WORKDIR}/venv
ENV PATH="${VIRTUAL_ENV}/bin:${PATH}"

RUN adduser -D -s /bin/bash vscode

USER root
RUN apk add --no-cache curl wget bash

USER vscode

WORKDIR ${WORKDIR}

RUN curl -s https://api.github.com/repos/njavilas2015/githooks/releases/latest | \
    grep "browser_download_url" | cut -d '"' -f 4 | wget -i - && \
    chmod +x githooks

COPY . ${WORKDIR}

RUN python3 -m venv ${VIRTUAL_ENV}

RUN chown -R vscode:vscode ${VIRTUAL_ENV}

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

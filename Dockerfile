FROM python:3.9.7

# change shell to bash
SHELL ["/bin/bash", "-c"]

# copy requirements.txt
COPY requirements.txt .

# copy application files
COPY router-config-generator/ /router-config-generator


# Install dependancies for, and s6-overlay
RUN python3 -m venv /router-config-generator/router-config-generator && \
    source /router-config-generator/router-config-generator/bin/activate && \
    apt update && apt install curl -y && \
    mkdir -p /etc/services.d/rcg && \
    # Install s6-overlay
    curl --location -s https://raw.githubusercontent.com/mikenye/deploy-s6-overlay/master/deploy-s6-overlay.sh | sh

# install python dependancies
RUN python3 -m pip install --upgrade pip && \
    pip3 install -r requirements.txt

# copy run file for s6-overlay
COPY ./run /etc/services.d/rcg

# expose port for web app
EXPOSE 5000

# go!
ENTRYPOINT [ "/init" ]
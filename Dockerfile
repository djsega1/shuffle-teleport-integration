FROM frikky/shuffle:app_sdk_ubuntu

# ENV SYSTEM_ARCH=amd64
# ENV TELEPORT_PKG=teleport

ENV TELEPORT_VERSION=12.4.9

COPY src /app
ADD requirements.txt ./
ADD ./install_teleport.sh ./

RUN chmod +x ./install_teleport.sh && \
    ./install_teleport.sh

RUN pip3 install -r ./requirements.txt

WORKDIR /app

CMD python3 app.py

#ENTRYPOINT ["tail", "-f", "/dev/null"]

FROM ubuntu
RUN sudo apt-get updata -y
RUN sudo apt-get install python -y
RUN sudo apt-get install flask -y
COPY . /opt/
ENTRYPOINT [ "python", "app.py" ]
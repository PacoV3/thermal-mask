FROM tensorflow/tensorflow:latest-jupyter

RUN python3 -m pip install imutils
RUN python3 -m pip install sklearn
RUN python3 -m pip install opencv-python

RUN apt-get update
RUN apt-get install libxext6 -y
RUN apt-get install libsm6 -y
RUN apt-get install ffmpeg -y

CMD ["bash", "-c", "source /etc/bash.bashrc && jupyter notebook --notebook-dir=/tf --ip 0.0.0.0 --no-browser --allow-root"]
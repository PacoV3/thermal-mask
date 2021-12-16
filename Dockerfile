FROM tensorflow/tensorflow:latest-jupyter

WORKDIR "/tf/notebooks"

RUN pip install seaborn imutils sklearn opencv-python azure-storage-blob

RUN apt-get update && \
    apt-get install -y libxext6 libsm6 ffmpeg

CMD ["bash", "-c", "source /etc/bash.bashrc && jupyter notebook --ip 0.0.0.0 --no-browser --allow-root"]
# How to run the notebooks

## Build the image based on the Dockerfile

```bash
docker build -t tensorflow-face-mask .
```

## Run the tensorflow-jupyter container

```bash
# For PowerShell
docker run -it --name tf-face-mask -v ${PWD}:/tf/notebooks -p 8888:8888 tensorflow-face-mask

# For Linux:
docker run -it --name tf-face-mask -v $PWD:/tf/notebooks -p 8888:8888 tensorflow-face-mask
```

FROM ubuntu:20.04
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y imagemagick python3
RUN mkdir -p /mnt/files
COPY data/student.txt /mnt/files/student.txt
EXPOSE 8819
CMD ["python3", "-m", "http.server", "--directory", "/mnt/files", "8819"]

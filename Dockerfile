# specify base image. going for python3-8 alpine, which is a minimalist linux distro
# advices are somewhat divided on it but let's just try it out
FROM python:3.8-alpine
WORKDIR /project

# ENV VARS are set in the docker-compose.yml

#RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN echo "pip-install requirements txt done."
RUN echo "copying project files... "
COPY . /project

RUN echo "dockerfile completed. Running entry-point command "
CMD ["flask", "run"]


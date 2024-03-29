
FROM python:3.11


# Copying the project files
WORKDIR /lab
COPY . .


# Installing the project in editable mode
RUN cd /lab && \
    pip install -e . && \
    pip install -r ./requirements/required.txt && \
    pip install -r ./requirements/tests.txt && \
    pip install -r ./requirements/docs.txt && \
    apt-get clean

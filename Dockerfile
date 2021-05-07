FROM python:3.8.8-slim-buster

# Working Directory
WORKDIR $HOME/Flask-Basic

# Copy source code to working directory
COPY . $HOME/Flask-Basic

# Install packages from requirements.txt
# hadolint ignore=DL3013
RUN pip install --no-cache-dir --upgrade pip &&\
    pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "src/app.py" ]
FROM python
COPY . /docker-assignment1
WORKDIR /docker-assignment1
RUN pip install beautifulsoup4
RUN command 
CMD python pythoncode.py
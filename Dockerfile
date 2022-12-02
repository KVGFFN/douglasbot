FROM python

ADD main.py .
ADD helper.py .

RUN pip install requests beautifulsoup4 
CMD ["python","./main.py"]


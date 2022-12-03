FROM python3.11-nodejs19

ADD main.py .
ADD helper.py .
ADD index.js .

RUN pip install requests beautifulsoup4 
RUN npm install
CMD ["node","./index.js"]


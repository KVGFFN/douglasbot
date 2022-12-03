FROM node

ADD main.py .
ADD helper.py .
ADD index.js .

RUN apt-get update || : && apt-get install python -y
RUN pip install requests beautifulsoup4 
RUN npm install
CMD ["node","./index.js"]


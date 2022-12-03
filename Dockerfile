FROM node

ADD main.py .
ADD helper.py .
ADD index.js .

RUN pip install requests beautifulsoup4 
RUN apt-get install -y git-core curl build-essential openssl libssl-dev \
 && git clone https://github.com/nodejs/node.git \
 && cd node \
 && ./configure \
 && make \
 && sudo make install
RUN npm install
CMD ["node","./index.js"]


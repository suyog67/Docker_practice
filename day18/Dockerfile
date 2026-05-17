FROM node:18-alpine
LABEL maintainer="suyog"
WORKDIR /app
COPY package.json . 
RUN npm install 
COPY . .
EXPOSE 3000
CMD ["node", "server.js"]

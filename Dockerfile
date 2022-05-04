FROM node:16.15.0-alpine3.15 as build

RUN apk add --no-cache \
      chromium \
      nss \
      freetype \
      harfbuzz \
      ca-certificates \
      ttf-freefont

RUN mkdir /src
WORKDIR /src

COPY package.json package-lock.json ./
RUN npm ci

COPY . ./
ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true \
    PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium-browser
RUN npm run scully:prod

FROM nginx:1.21.6-alpine

COPY --from=build /src/dist/static /srv/www

CMD ["nginx", "-g", "daemon off;"]

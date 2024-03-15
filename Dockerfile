FROM node:16.15.0-alpine3.15 as build

RUN apk add --no-cache \
      chromium \
      ca-certificates

RUN mkdir /src
WORKDIR /src

COPY package.json package-lock.json ./
RUN npm ci

COPY . ./
ARG ALGOLIA_PD_INDEX \
    ALGOLIA_WRITE_KEY \
    ENVIRONMENT
ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true \
    PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium-browser \
    ALGOLIA_APP_ID=0GWOH3DBQG \
    ALGOLIA_PD_INDEX=${ALGOLIA_PD_INDEX} \
    ALGOLIA_SEARCH_KEY=ea48631f18be2668127d8ae7a2633fe9 \
    ALGOLIA_WRITE_KEY=${ALGOLIA_WRITE_KEY} \
    ENVIRONMENT=${ENVIRONMENT}
RUN npm run scully:prod && scripts/patch_envs.sh

FROM nginx:1.21.6-alpine

ARG SERVICE_PORT=8080
ENV SERVICE_PORT=${SERVICE_PORT}

COPY --from=build /src/dist/static /srv/www
COPY default.conf /etc/nginx/conf.d/
COPY scripts/start.sh ./
RUN chmod +x ./start.sh

EXPOSE ${SERVICE_PORT}

CMD ./start.sh

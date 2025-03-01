FROM node:14-alpine as build-stage
WORKDIR /app
COPY package*.json ./
COPY node_modules ./node_modules
COPY . .
RUN npm run build
RUN npm run dev

FROM nginx:alpine
COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
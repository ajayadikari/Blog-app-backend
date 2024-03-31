echo "in start_container_script"
docker pull ajayadikari/blog-app-backend:latest
docker run -d -p 8000:8000 ajayadikari/blog-app-backend:latest
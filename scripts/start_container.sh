set -e

docker pull ajayadikari/blogapp-backend

docker run -d -p 8000:8000 ajayadikari/blogapp-backend
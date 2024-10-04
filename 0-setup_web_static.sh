#!/usr/bin/env bash
# script that sets up web servers for the deployment of web_static

# Update package lists
sudo apt-get update -y

# Install Nginx if it is not already installed
if ! dpkg -l | grep -q nginx; then
    sudo apt-get -y install nginx
fi

# Allow 'Nginx HTTP' through UFW
sudo ufw allow 'Nginx HTTP'

# Create necessary directories if they do not exist
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

# Create a fake HTML file in /data/web_static/releases/test/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Remove the symbolic link if it exists and recreate it
sudo rm -f /data/web_static/current
sudo ln -s /data/web_static/releases/test /data/web_static/current

# Give ownership of /data/ to the ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve content from /data/web_static/current/
if ! grep -q "location /hbnb_static" /etc/nginx/sites-enabled/default; then
    sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default
fi

# Restart Nginx to apply the changes
sudo service nginx restart

# Ensure the script exits successfully
exit 0

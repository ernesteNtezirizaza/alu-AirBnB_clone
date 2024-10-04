#!/usr/bin/env bash
# script that sets up web servers for the deployment of web_static

# Update package lists
if ! sudo apt-get update -y; then
    echo "Failed to update package lists."
    exit 1
fi

# Install Nginx if it is not already installed
if ! dpkg -l | grep -q nginx; then
    if ! sudo apt-get -y install nginx; then
        echo "Failed to install Nginx."
        exit 1
    fi
fi

# Allow 'Nginx HTTP' through UFW
if ! sudo ufw allow 'Nginx HTTP'; then
    echo "Failed to allow Nginx HTTP through UFW."
    exit 1
fi

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
if ! sudo rm -f /data/web_static/current; then
    echo "Failed to remove existing symbolic link."
    exit 1
fi

if ! sudo ln -s /data/web_static/releases/test /data/web_static/current; then
    echo "Failed to create symbolic link."
    exit 1
fi

# Give ownership of /data/ to the ubuntu user and group recursively
if ! sudo chown -R ubuntu:ubuntu /data/; then
    echo "Failed to change ownership of /data."
    exit 1
fi

# Update Nginx configuration to serve content from /data/web_static/current/
if ! sudo grep -q "location /hbnb_static" /etc/nginx/sites-enabled/default; then
    if ! sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default; then
        echo "Failed to update Nginx configuration."
        exit 1
    fi
fi

# Restart Nginx to apply the changes
if ! sudo service nginx restart; then
    echo "Failed to restart Nginx."
    exit 1
fi

# Ensure the script exits successfully
echo "Setup completed successfully."
exit 0

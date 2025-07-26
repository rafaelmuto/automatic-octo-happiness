# Sophia Project - Deployment Guide

This document provides comprehensive deployment instructions for the Sophia library management system.

## 🎯 Deployment Options

Sophia can be deployed in several environments:

1. **Development Environment** - Local development setup
2. **Production Environment** - Production server deployment
3. **Hardware Deployment** - Single-board computer (Raspberry Pi)
4. **Container Deployment** - Docker-based deployment

## 🚀 Quick Start

### Development Environment

```bash
# Clone the repository
git clone <repository-url>
cd DjangoProject

# Setup development environment
./scripts/setup-dev.sh

# Start development server
python manage.py runserver 8001
```

### Production Environment

```bash
# Setup production environment
make setup
make collectstatic
make migrate

# Start production server
gunicorn sophia.wsgi:application --bind 0.0.0.0:8001
```

## 📋 Prerequisites

### System Requirements

#### Minimum Requirements

- **CPU**: 1 GHz dual-core processor
- **RAM**: 2 GB
- **Storage**: 10 GB free space
- **OS**: Linux (Ubuntu 20.04+, Debian 11+, or similar)

#### Recommended Requirements

- **CPU**: 2 GHz quad-core processor
- **RAM**: 4 GB
- **Storage**: 50 GB free space
- **OS**: Ubuntu 22.04 LTS

### Software Requirements

- **Python**: 3.10 or higher
- **pip**: Python package installer
- **git**: Version control
- **nginx**: Web server (production)
- **SQLite**: Database (default, can be changed to PostgreSQL for production)

## 🔧 Development Deployment

### Local Development Setup

1. **Clone Repository**

   ```bash
   git clone <repository-url>
   cd DjangoProject
   ```

2. **Setup Virtual Environment**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**

   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Database Setup**

   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

6. **Start Development Server**
   ```bash
   python manage.py runserver 8001
   ```

### Using Automation Scripts

```bash
# Complete setup
./scripts/setup-dev.sh

# Start development
make dev
```

## 🏭 Production Deployment

### Traditional Server Deployment

#### 1. Server Preparation

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install required packages
sudo apt install python3 python3-pip python3-venv nginx postgresql postgresql-contrib -y

# Create application user
sudo useradd -m -s /bin/bash sophia
sudo usermod -aG sudo sophia
```

#### 2. Application Setup

```bash
# Switch to application user
sudo su - sophia

# Clone repository
git clone <repository-url> /home/sophia/sophia-app
cd /home/sophia/sophia-app

# Setup virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install gunicorn psycopg2-binary
```

#### 3. Database Configuration

```bash
# For SQLite (default) - no additional setup needed
# The database file will be created automatically

# For PostgreSQL (optional)
sudo -u postgres createdb sophia_db
sudo -u postgres createuser sophia_user
sudo -u postgres psql -c "ALTER USER sophia_user PASSWORD 'your_password';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE sophia_db TO sophia_user;"
```

#### 4. Environment Configuration

```bash
# Create production environment file
cat > .env << EOF
DEBUG=False
SECRET_KEY=your-secret-key-here
# For SQLite (default)
DATABASE_URL=sqlite:///db.sqlite3
# For PostgreSQL (optional)
# DATABASE_URL=postgresql://sophia_user:your_password@localhost/sophia_db
ALLOWED_HOSTS=your-domain.com,www.your-domain.com
STATIC_ROOT=/home/sophia/sophia-app/staticfiles
EOF
```

#### 5. Application Configuration

```bash
# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic --noinput
```

#### 6. Gunicorn Configuration

```bash
# Create Gunicorn configuration
cat > gunicorn.conf.py << EOF
bind = "127.0.0.1:8001"
workers = 3
worker_class = "sync"
worker_connections = 1000
max_requests = 1000
max_requests_jitter = 50
timeout = 30
keepalive = 2
EOF
```

#### 7. Systemd Service

```bash
# Create systemd service file
sudo tee /etc/systemd/system/sophia.service << EOF
[Unit]
Description=Sophia Library Management System
After=network.target

[Service]
Type=notify
User=sophia
Group=sophia
WorkingDirectory=/home/sophia/sophia-app
Environment=PATH=/home/sophia/sophia-app/.venv/bin
ExecStart=/home/sophia/sophia-app/.venv/bin/gunicorn --config gunicorn.conf.py sophia.wsgi:application
ExecReload=/bin/kill -s HUP \$MAINPID
KillMode=mixed
TimeoutStopSec=5
PrivateTmp=true

[Install]
WantedBy=multi-user.target
EOF

# Enable and start service
sudo systemctl enable sophia
sudo systemctl start sophia
```

#### 8. Nginx Configuration

```bash
# Create Nginx configuration
sudo tee /etc/nginx/sites-available/sophia << EOF
server {
    listen 80;
    server_name your-domain.com www.your-domain.com;

    location = /favicon.ico { access_log off; log_not_found off; }

    location /static/ {
        root /home/sophia/sophia-app;
    }

    location /media/ {
        root /home/sophia/sophia-app;
    }

    location / {
        include proxy_params;
        proxy_pass http://127.0.0.1:8001;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
    }
}
EOF

# Enable site
sudo ln -s /etc/nginx/sites-available/sophia /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

#### 9. SSL Configuration (Optional)

```bash
# Install Certbot
sudo apt install certbot python3-certbot-nginx -y

# Obtain SSL certificate
sudo certbot --nginx -d your-domain.com -d www.your-domain.com

# Auto-renewal
sudo crontab -e
# Add: 0 12 * * * /usr/bin/certbot renew --quiet
```

## 🐳 Docker Deployment

### Using Docker Compose

The project already includes Docker configuration with `docker-compose.yaml` and `Dockerfile`.

#### 1. Docker Configuration

```bash
# Build and run with Docker Compose
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Using Makefile commands
make docker-build
make docker-run
make docker-stop
```

#### 2. Production Docker Compose

```yaml
# docker-compose.prod.yml
version: '3.8'

services:
  web:
    build: .
    restart: always
    environment:
      - DEBUG=False
      - DATABASE_URL=postgresql://sophia_user:password@db:5432/sophia_db
    depends_on:
      - db
    volumes:
      - static_volume:/app/staticfiles
      - media_volume:/app/media

  db:
    image: postgres:13
    restart: always
    environment:
      - POSTGRES_DB=sophia_db
      - POSTGRES_USER=sophia_user
      - POSTGRES_PASSWORD=password
    volumes:
      - postgres_data:/var/lib/postgresql/data

  nginx:
    image: nginx:alpine
    restart: always
    ports:
      - '80:80'
      - '443:443'
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - static_volume:/app/staticfiles
      - media_volume:/app/media
    depends_on:
      - web

volumes:
  postgres_data:
  static_volume:
  media_volume:
```

#### 3. Production Deployment

```bash
# Deploy production stack
docker-compose -f docker-compose.prod.yml up -d

# Run migrations
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate

# Create superuser
docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser

# Collect static files
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --noinput
```

## 🍓 Hardware Deployment (Raspberry Pi)

### Raspberry Pi Setup

#### 1. System Preparation

```bash
# Update Raspberry Pi OS
sudo apt update && sudo apt upgrade -y

# Install required packages
sudo apt install python3 python3-pip python3-venv nginx sqlite3 git -y

# Enable SSH (if not already enabled)
sudo raspi-config
# Navigate to: Interface Options > SSH > Enable
```

#### 2. Application Installation

```bash
# Clone repository
git clone <repository-url> /home/pi/sophia-app
cd /home/pi/sophia-app

# Setup virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install gunicorn
```

#### 3. Configuration

```bash
# Create environment file
cat > .env << EOF
DEBUG=False
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=raspberrypi.local,192.168.1.100
STATIC_ROOT=/home/pi/sophia-app/staticfiles
EOF

# Run setup
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic --noinput
```

#### 4. Service Configuration

```bash
# Create systemd service
sudo tee /etc/systemd/system/sophia.service << EOF
[Unit]
Description=Sophia Library Management System
After=network.target

[Service]
Type=notify
User=pi
Group=pi
WorkingDirectory=/home/pi/sophia-app
Environment=PATH=/home/pi/sophia-app/.venv/bin
ExecStart=/home/pi/sophia-app/.venv/bin/gunicorn --bind 0.0.0.0:8001 sophia.wsgi:application
ExecReload=/bin/kill -s HUP \$MAINPID
KillMode=mixed
TimeoutStopSec=5
PrivateTmp=true

[Install]
WantedBy=multi-user.target
EOF

# Enable and start service
sudo systemctl enable sophia
sudo systemctl start sophia
```

#### 5. Nginx Configuration

```bash
# Create Nginx configuration
sudo tee /etc/nginx/sites-available/sophia << EOF
server {
    listen 80;
    server_name raspberrypi.local;

    location /static/ {
        alias /home/pi/sophia-app/staticfiles/;
    }

    location / {
        proxy_pass http://127.0.0.1:8001;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
    }
}
EOF

# Enable site
sudo ln -s /etc/nginx/sites-available/sophia /etc/nginx/sites-enabled/
sudo rm /etc/nginx/sites-enabled/default
sudo nginx -t
sudo systemctl restart nginx
```

## 🔒 Security Configuration

### Environment Variables

```bash
# Production environment variables
DEBUG=False
SECRET_KEY=your-very-secure-secret-key
ALLOWED_HOSTS=your-domain.com,www.your-domain.com
DATABASE_URL=postgresql://user:password@localhost/dbname

# Security settings
CSRF_COOKIE_SECURE=True
SESSION_COOKIE_SECURE=True
SECURE_BROWSER_XSS_FILTER=True
SECURE_CONTENT_TYPE_NOSNIFF=True
X_FRAME_OPTIONS=DENY
```

### Firewall Configuration

```bash
# Configure UFW firewall
sudo ufw allow ssh
sudo ufw allow 'Nginx Full'
sudo ufw enable
```

### Database Security

```bash
# PostgreSQL security
sudo -u postgres psql -c "ALTER USER sophia_user PASSWORD 'strong_password';"
sudo -u postgres psql -c "REVOKE ALL ON ALL TABLES IN SCHEMA public FROM PUBLIC;"
```

## 📊 Monitoring and Logging

### Application Monitoring

```bash
# View application logs
sudo journalctl -u sophia -f

# View Nginx logs
sudo tail -f /var/log/nginx/access.log
sudo tail -f /var/log/nginx/error.log

# Monitor system resources
htop
df -h
free -h
```

### Health Checks

```bash
# Application health check
curl -f http://localhost:8001/health/

# Database connection test
python manage.py dbshell

# Static files check
ls -la staticfiles/
```

## 🔄 Backup and Recovery

### Database Backup

```bash
# SQLite backup (default)
cp db.sqlite3 db.sqlite3.backup.$(date +%Y%m%d_%H%M%S)

# PostgreSQL backup (if using PostgreSQL)
pg_dump sophia_db > sophia_backup_$(date +%Y%m%d_%H%M%S).sql
```

# Automated backup script

cat > backup.sh << 'EOF'
#!/bin/bash
BACKUP*DIR="/home/sophia/backups"
DATE=$(date +%Y%m%d*%H%M%S)
mkdir -p $BACKUP_DIR

# Database backup (SQLite)

cp db.sqlite3 $BACKUP_DIR/sophia_db_$DATE.sqlite3

# Application backup

tar -czf $BACKUP_DIR/sophia_app_$DATE.tar.gz /home/sophia/sophia-app

# Clean old backups (keep last 7 days)

find $BACKUP_DIR -name "_.sqlite3" -mtime +7 -delete
find $BACKUP_DIR -name "_.tar.gz" -mtime +7 -delete
EOF

chmod +x backup.sh

````

### Recovery Procedures

```bash
# Database recovery (SQLite)
cp sophia_backup_20240725_120000.sqlite3 db.sqlite3

# Application recovery
tar -xzf sophia_app_20240725_120000.tar.gz -C /home/sophia/
````

## 🚨 Troubleshooting

### Common Issues

#### 1. Permission Errors

```bash
# Fix file permissions
sudo chown -R sophia:sophia /home/sophia/sophia-app
sudo chmod -R 755 /home/sophia/sophia-app
```

#### 2. Database Connection Issues

```bash
# Check database status
sudo systemctl status postgresql

# Test database connection
python manage.py dbshell
```

#### 3. Static Files Not Loading

```bash
# Recollect static files
python manage.py collectstatic --noinput

# Check Nginx configuration
sudo nginx -t
sudo systemctl restart nginx
```

#### 4. Service Not Starting

```bash
# Check service status
sudo systemctl status sophia

# View service logs
sudo journalctl -u sophia -n 50
```

### Performance Optimization

```bash
# Database optimization
python manage.py dbshell
# Run: VACUUM; ANALYZE;

# Clear cache
python manage.py clearcache

# Optimize static files
python manage.py collectstatic --noinput --clear
```

## 📝 Deployment Checklist

### Pre-Deployment

- [ ] Code review completed
- [ ] Tests passing
- [ ] Environment variables configured
- [ ] Database migrations ready
- [ ] Static files collected
- [ ] Security settings configured

### Deployment

- [ ] Application deployed
- [ ] Database migrated
- [ ] Static files served
- [ ] Service started
- [ ] Health checks passing
- [ ] SSL certificate installed (if applicable)

### Post-Deployment

- [ ] Application accessible
- [ ] API endpoints working
- [ ] Admin interface accessible
- [ ] Monitoring configured
- [ ] Backup procedures tested
- [ ] Documentation updated

---

**Last Updated**: July 25, 2024
**Version**: 1.0

```

```

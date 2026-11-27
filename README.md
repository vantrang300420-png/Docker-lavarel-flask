# Laravel 13 + Flask + MySQL chạy bằng Docker

Dự án môn <Mã Nguồn Mở> – Chủ đề 10: Tìm hiểu và sử dụng Docker.
Một lệnh khởi động đồng thời web Laravel 13, web Flask và cơ sở dữ liệu MySQL.

## Công nghệ

- Laravel 13 (PHP >= 8.3) chạy qua PHP-FPM
- Nginx (web server)
- MySQL 8
- Python Flask
- Docker và Docker Compose

## Yêu cầu trước khi chạy
- Docker Desktop (Windows) tải tại https://www.docker.com
- Git
## Cấu trúc thư mục
```text
Docker-lavarel-flask/
├── .docker/
│   ├── nginx.conf          # Cấu hình web server Nginx
│   └── php.Dockerfile      # Cấu hình cài đặt PHP
├── flask-app/              # Ứng dụng Flask và Dockerfile của nó
├── docker-compose.yml      # Điều phối các container
├── src/                    # Mã nguồn Laravel 13
├── .gitignore
└── README.md                     # File hướng dẫn này
```
## Hướng dẫn cài đặt
### Bước 1: Tải mã nguồn
```bash
git clone https://github.com/vantrang300420-png/Docker-lavarel-flask.git
cd Docker-lavarel-flask
```
### Bước 2: Build và khởi động hệ thống
```bash
docker compose up -d --build
docker compose ps
```
Tất cả service phải ở trạng thái `running`. Lần đầu build có thể mất vài phút.
### Bước 3: Khởi tạo Laravel (chỉ làm lần đầu)
Vào container PHP:

```bash
docker compose exec app bash
```

Chạy lần lượt các lệnh sau bên trong container:

```bash
composer install
cp .env.example .env
```

Mở file `.env` và sửa phần cơ sở dữ liệu cho khớp `docker-compose.yml`:

```env
DB_CONNECTION=mysql
DB_HOST=db
DB_PORT=3306
DB_DATABASE=laravel_db
DB_USERNAME=laravel_user
DB_PASSWORD=secret_password
```

Tiếp tục chạy:

```bash
php artisan key:generate
chmod -R 775 storage bootstrap/cache
php artisan migrate
chown -R www-data:www-data storage bootstrap/cache
chmod -R 777 storage bootstrap/cache
exit
```
### Bước 4: Kiểm tra kết quả

| Ứng dụng | Địa chỉ |
| --- | --- |
| Laravel | http://localhost |
| Flask | http://localhost:5000 |

## Các lệnh thường dùng

| Việc cần làm | Lệnh |
| --- | --- |
| Xem container đang chạy | `docker compose ps` |
| Xem log | `docker compose logs -f <tên-service>` |
| Vào container PHP | `docker compose exec app bash` |
| Chạy lại sau khi sửa Dockerfile | `docker compose up -d --build` |

## Tắt hệ thống khi làm xong

```bash
docker compose down
```

Lệnh này xóa container nhưng giữ dữ liệu MySQL nhờ Volume. Muốn xóa cả dữ liệu: `docker compose down -v`.


Thành viên nhóm
Tính (Leader): cấu hình Docker gốc, làm slide
Trân: tích hợp Flask, docker-compose
My: lý thuyết, kiểm thử, README
Khoa: sơ đồ, demo, thuyết trình
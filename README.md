# how-to-kill-virus-kdevtmpfsi
how to kill virus kdevtmpfsi


## Bước 1: Xóa tất cả các thư mục có tên bắt đầu là kdevtmpfsi và kinsing
```
find / -iname kdevtmpfsi* -exec rm -fv {} \;
find / -iname kinsing* -exec rm -fv {} \;
```

## Bước 2: Tạo 2 file cùng tên với con virus cùi bắp
```
touch /tmp/kdevtmpfsi
echo "kdevtmpfsi is fine now" > /tmp/kdevtmpfsi
touch /var/tmp/kinsing
echo "kinsing is fine now" > /var/tmp/kinsing
touch /tmp/kinsing
echo "kinsing is fine now" > /tmp/kinsing
```

## Bước 3: Cấp quyền chỉ cho đọc 2 file đó
```
chattr +i /tmp/kdevtmpfsi
chattr +i /var/tmp/kinsing
chattr +i /tmp/kinsing
```


Vọc xem chi tiết con đó làm gì
```
systemctl status idProcess
```
## Bước 4: Ngăn con virus quay trở lại
Con virus này rất khôn, nó cài auto curl để tự cài lại, vì thế, mình mở crontab (trình quản lý cron job mặc định của linux) , mở ra và xóa hết cron của con virus đi.

+ Mở crontab của ubuntu và xóa cái cái curl của nó đi
```
sudo su -c "crontab -e" www-data -s /bin/bash
```
+ Mở crontab của centos và xóa cái cái curl của nó đi
 ```
 # Liệt kê tất cả các crontab của tất cả các user
for user in $(cut -f1 -d: /etc/passwd); do echo $user; crontab -u $user -l; done
 
 # Liệt kê tất cả các crontab của user apache
crontab -u apache -l
 # Chỉnh sửa crontab của user apache
crontab -u apache -e
 ```

Nếu nó vẫn quay lại thì thử hard core hơn đó là không cho phép www-data ghi vào crontab
```
touch /var/spool/cron/crontabs/www-data;
chmod 0 /var/spool/cron/crontabs/www-data;
```
## Bước 5: reboot

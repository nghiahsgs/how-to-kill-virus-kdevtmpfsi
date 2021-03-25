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
```

## Bước 3: Cấp quyền chỉ cho đọc 2 file đó
```
chattr +i /tmp/kdevtmpfsi
chattr +i /var/tmp/kinsing
```

# Virtual Environment - Môi trường ảo

Môi trường ảo hiểu nôm na nó sẽ cho phép bạn nghịch ngợm lung tung, hay test thử các packages, thư viện mới của Python mà không ảnh hưởng tới những packages đã được cài ở môi trường global. Nói chung nó giống như việc bạn tạo ra một tờ giấy trắng khác rồi vẽ phác thảo mẫu lên thay vì vẽ thẳng vào tờ giấy chính vậy á =)) 

Để coi những packages đã được cài ở môi trường global thì chỉ cần thao tác như sau (đảm bảo bạn đã cài anaconda ở bài 01): [**Bật cmd -> conda list**]. Nó ra một list dài các packages như vầy là đúng ròi á. Kể từ giờ mình sẽ gọi môi trường chính là **Global**, môi trường ảo là **Local** cho dễ nha

![image](https://user-images.githubusercontent.com/43443323/88449554-06914a00-ce72-11ea-992c-f3abc7dd4416.png)

## Cài đặt Virtual Environment

Ở trên bọn mình đã biết tại sao phải dùng môi trường ảo với môi trường Global là gì rồi nên bây giờ sẽ tiếp đến phần tạo và thao tác trên môi trường ảo.  

Mình sẽ không sử dụng packages **virtualenv** hay **pip** để tạo môi trường ảo, mà mình sẽ sử dụng thẳng luôn **conda** để tạo, lí do: <https://docs.conda.io/projects/conda/en/latest/commands.html#conda-vs-pip-vs-virtualenv-commands>

___

**Bước 1:** Sử dụng lệnh sau để tạo môi trường **demoenv** có thể thay bằng bất cứ tên nào mà bạn thích

```
$ conda create --name demoenv
```
Gõ y để xác nhận tạo môi trường và kết quả đây

![image](https://user-images.githubusercontent.com/43443323/88449820-4e18d580-ce74-11ea-9432-67fff80c5a61.png)


**Bước 2:** Sử dụng lệnh như nó hướng dẫn

```
$ conda activate demoenv
```
Nó thay đổi chỗ này chữ **(base)** thành **(demoenv)** là thành công rồi á  

![image](https://user-images.githubusercontent.com/43443323/88449881-d26b5880-ce74-11ea-93f1-db305a6c6377.png)

**Bước 3:** Kiểm tra thử trong môi trường ảo này có packages nào đã được cài hay không?

```
$ conda list
```

Kết quả ra vầy là đúng nha, bởi vì như nãy mình đã nói, môi trường ảo là tờ giấy trắng mới, có phải môi trường global đâu mà nó có sẵn mấy cái packages như cũ =))  

![image](https://user-images.githubusercontent.com/43443323/88449941-3b52d080-ce75-11ea-9172-cfb7ed138b3c.png)

**Bước 4:** Giờ thì cài những gói cần thiết vào rồi thử thôi, ví dụ như numpy nè, matplotlib nè =))

**Bước 5:** Sau khi đã sử dụng đủ thứ, chúng ta cần câu lệnh để deactive cái môi trường ảo này đi  
```
$ conda deactivate
```
Vậy là xong rồi, còn muốn xóa cả môi trường ảo ra khỏi máy tính thì tham khảo những lệnh ở dưới nha =))

## Những lệnh thường sử dụng

Mọi câu lệnh này mn có thể search on google hoặc ở link này <https://docs.conda.io/projects/conda/en/latest/glossary.html#>

```
# Hiển thị tất cả môi trường đang có trong máy với base là môi trường global
còn lại đều là các môi trường ảo
$ conda info --envs 

# Show ra tất cả những packages hiện có trong môi trường
$ conda list

# Install packages mới vào conda ví dụ như numpy, pandas,...
$ conda install ten_packages

# Update một packages nào đó lên bản mới nhất
$ conda update ten_packages
```

```
# Tạo môi trường ảo
$ conda create --name ten_moitruong_ao

# Kích hoạt môi trường ảo
$ conda activate

# Tắt môi trường ảo
$ conda deactivate

# Xóa môi trường ảo, phải đảm bảo đã tắt môi trường ảo rồi
$ conda remove --name ten_moi_truong_ao --all
```
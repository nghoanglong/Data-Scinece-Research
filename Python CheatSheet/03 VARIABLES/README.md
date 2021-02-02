# VARIABLES - Biến trong Python

Biến là một trong những khái niệm quan trọng trong lập trình, không chỉ riêng Python mà còn ở những ngôn ngữ lập trình khác.

Hình dung biến như một chiếc hộp, đồ vật bên trong chiếc hộp được gọi là giá trị.

Lập trình đơn giản là công việc tạo ra những thứ gọi là biến và đơn thuần thao tác với chúng.

## Define

```
Default: ten_bien = gia_tri

Ví dụ:

a = 5
variable = 6
day_la_bien = "day la gia tri"

a = a + 1 # biến a có giá trị = 5, ta thực hiện cộng thêm 1 vào, vậy a = 6

x = x + 1 # như vầy là sai vì x chưa được khởi tạo và gán giá trị mà đã thực 
hiện x + 1
```
Bên trái dấu bằng ta gọi là biến, một biến như ta biết nó là một chiếc hộp, mà hộp thì phải có giá trị, vậy giá trị ở trên là **5, 6, "day la gia tri"**. Việc làm như trên trong lập trình gọi là khởi tạo biến và gán giá trị cho biến.

## Kiểu dữ liệu

Như ta đã biết ở trên về việc khởi tạo biến và gán giá trị cho biến, vậy giá trị ta gán cho biến gồm những kiểu nào?

Value (giá trị) | Data Type (kiểu dữ liệu)
------------ | -------------
0, 1, 2,..., n | **int** - kiểu dữ liệu số nguyên
0.4, 0.3, 1.4,... | **float** - kiểu dữ liệu số thực
3 + 1j, 5 + 6j,... | **complex** - kiểu dữ liệu số phức
"day la mot chuoi" | **string** - kiểu dữ liệu dạng chuỗi
[1, 2, 3, 4]	   | **list hay array** - kiểu dữ liệu mảng
{1, 2, 3, 4}	   | **set** - kiểu dữ liệu set
(1, 3, 4, 5)       | **tuple** - kiểu dữ liệu tuple
{key: value}	   | **dictionary** - kiểu dữ liệu dictionary hay map
None 			   | **None hay Null** - kiểu dữ liệu None hay có thể hiểu là rỗng

Đây là những kiểu dữ liệu khác nhau trong Python, nếu có thiếu sót mn có thể tự bổ sung. Mình phải nói về kiểu dữ liệu này bởi vì trong C++ hay một số ngôn ngữ khác thì biến nó không tự hiểu giá trị đó mang kiểu dữ liệu gì như là Python, ví dụ C++:
```
//C++ cú pháp để khai báo và khởi tạo một biến
int a = 5
string text = "day la kieu chuoi"

//Python cú pháp để khai báo và khởi tạo một biến
a = 5
text = "day la kieu chuoi"
```
Như mn đã thấy, với C++, trước khi khởi tạo một biến ta phải định kiểu dữ liệu cho nó trước rồi mới được gán giá trị tương thích. May mắn thay, Python dành cho những người lười, mọi thứ đã được làm sẵn, vậy thui.

Mình sẽ có chuỗi bài riêng để giải thích về từng kiểu dữ liệu, có lẽ là sau bài về biến này. Tạm thời mn chưa cần hiểu vội, chỉ cần biết gán một giá trị nào mà nằm ngoài các kiểu dữ liệu ở trên thì chương trình sẽ báo lỗi, hiểu sơ sơ vậy đc rồi.

**Lưu ý:** Ta có một cách để lấy được kiểu dữ liệu của biến trong Python bằng từ khóa **type** như sau:

```python
a = "kieu du lieu chuoi"
print(type(a)) // <string type>
```

## Quy tắc đặt tên biến

Dĩ nhiên ta không thể muốn đặt tên biến là gì cũng được, nó có một số quy tắc riêng để đỡ trùng với những thứ khác, giống như nãy mình ví dụ, một biến coi như một cái hộp, chẳng lẽ giờ lại đặt tên cái hộp là cái nhà?. Trong lập trình cũng vậy, có một số cái nhà có sẵn, nếu bây giờ đặt trùng tên thì nó sẽ sai lè ra.

+ Không đặt tên biến bắt đầu bằng số | Ex: 4Years = 4, nhưng có thể đặt là Years4 = 4
+ Không sử dụng những ký tự ngu ngốc như $ % ^ &..., nói chung đừng bgio đặt tên biến bằng mấy cái kí tự này hoặc đặt tên biến có xuất hiện mấy cái kí tự như trên thì cũng nên bỏ luôn, ngoại trừ kí tự **_**
+ Không sử dụng dấu khi đặt tên biến | Ex: người_yêu = "khong co"
+ Không đặt tên biến trùng với những thứ có sẵn trong python (cái nhà) | Ex: print = "in ra", hàm print() là hàm để in ra, nó đã có sẵn trong python, đặt tên vầy là sai
+ Google Search thêm về những hàm có sẵn để tránh đặt trùng

Đây là một số quy tắc đặt tên biến, khi code gặp lỗi nhiều sẽ thành quen, mn không cần nhớ mấy cái quy tắc này nhiều, chỉ cần nhớ những thứ quan trọng thôi, đến khi gặp lỗi nhiều sẽ chừa và không đặt tên biến một cách ngu ngốc nữa.

# COMMENT CODE

Ở trên ta đã nói sương sương về biến là gì, cách khai báo và khởi tạo giá trị, bây giờ ta tiếp đến phần comment code.

Comment code cũng chỉ là cách note lại những chú thích cần thiết chứ không có gì cao siêu. 

Dev thường có nhiều công việc phải làm, nên việc comment lại ý nghĩa của một đoạn code nào đó trong hàng trăm ngàn dòng code là một điều nên làm, vừa dễ hiểu lại tránh bị quên.

## Define

```
# Cách comment lại code trong Python ta sẽ bắt đầu bằng dấu #, ví dụ như sau;

#khởi tạo biến a và gán giá trị là một chuỗi
#đây là dòng comment, nó sẽ không được thực thi khi chạy chương trình
#nó chỉ dùng để note lại thôi, dòng được thực thi là dòng khởi gán
#và dòng print(), cho nên muốn dòng nào không thực thi, ta chỉ cần đặt nó là
#một dòng comment là được

a = "mot cai gi do"
print(a)
```
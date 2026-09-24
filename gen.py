import subprocess
import sys

try:
    import docx
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'python-docx'])
    import docx

doc = docx.Document()
doc.add_heading('Lời giải Bài tập Python', 0)

content = """
Chương 1: TỔNG QUAN VỀ NGÔN NGỮ LẬP TRÌNH PYTHON
1. Chương trình dịch: Dịch mã nguồn sang ngôn ngữ máy. Vai trò: Giúp máy tính có thể hiểu và thực thi chương trình.
2. Biên dịch: Dịch toàn bộ mã nguồn một lần thành tệp thực thi. Thông dịch: Dịch và thực thi từng dòng lệnh một (Python là ngôn ngữ thông dịch).
3. Bậc cao: Cú pháp gần gũi với ngôn ngữ tự nhiên. Thông dịch: Chạy trực tiếp qua trình thông dịch (Interpreter) mà không cần biên dịch trước.
4. IDE: PyCharm, VS Code, Spyder, IDLE, Jupyter Notebook.
5. Ứng dụng: Phát triển Web (Django/Flask), Trí tuệ nhân tạo (AI/ML), Phân tích dữ liệu (Pandas), Tự động hóa (Scripting).
6. Phương thức thực thi: Chế độ tương tác (Interactive Mode) và Chế độ kịch bản (Script Mode).
7. Gọi là Python Script, phần mở rộng mặc định là .py.
8. PyPI: Python Package Index, là kho lưu trữ các gói phần mềm của bên thứ 3 dành cho Python.
9. Pip: Trình quản lý gói của Python, dùng để cài đặt và quản lý các thư viện/gói từ PyPI.
10. NumPy: Thư viện tính toán khoa học, hỗ trợ mảng đa chiều (ndarray) và các phép toán đại số tuyến tính.
11. Mô-đun: Là một tệp .py chứa các mã Python. Gói (Package): Là thư mục chứa nhiều mô-đun và tệp __init__.py.
12. Lệnh cài đặt phần mềm IDLE (IDE mặc định của Python) trên hệ điều hành Linux (Ubuntu/Debian) bằng quyền quản trị.
13. Lệnh dùng pip để cài đặt IDE Spyder.
14. Lệnh: python --version hoặc python -V trong terminal/command prompt.
15. Cú pháp: import [tên_mô_đun]. Ví dụ: import math.
16. Cần import mô-đun math. Cú pháp: from math import sqrt, pow, exp.
17. Cần sử dụng mô-đun random. Cú pháp: import random.
18. Mô-đun os: Tương tác với hệ điều hành như tạo, xóa thư mục, lấy đường dẫn, thực thi lệnh hệ thống.
19. Mô-đun datetime hoặc time. Ví dụ: import datetime; print(datetime.datetime.now()).
20. Giấy phép PSF (Python Software Foundation License), là giấy phép mã nguồn mở cho phép sử dụng, sửa đổi và phân phối tự do.

Chương 2: LẬP TRÌNH CĂN BẢN
1. Kết quả: Orange. Vì Python cho phép gán một giá trị cho nhiều biến cùng một lúc.
2. Dùng hàm type(). Ví dụ: type(x) sẽ trả về kiểu dữ liệu của x.
3. Dùng hàm input(). Ví dụ: name = input('Nhập tên: '). Giá trị nhập vào luôn là chuỗi (str).
4. Kết quả báo lỗi TypeError vì chuỗi định dạng % có 2 biến %s nhưng tuple truyền vào bị thiếu hoặc biến v chưa được định nghĩa.
5. Kết quả: I want to pay 49.95 dollars for 3 pieces of item 567. Phương thức format() truyền giá trị vào các vị trí {} tương ứng với chỉ số.
6. Kết quả: ['Apple', ' Banana', ' Cherry']. Hàm split(',') cắt chuỗi s thành danh sách các chuỗi con dựa trên dấu phẩy.
7. Kết quả: Wellcome to Viet Nam ! (Biến w có %s được thay thế bằng chuỗi v).
8. print('I want {} pieces of item {} for {} dollars.'.format(3, 567, 49.95))
9. Dùng lệnh: print('Hello World'). Hàm print dùng để xuất dữ liệu ra màn hình.
10. Hợp lệ: bắt đầu bằng chữ cái hoặc dấu gạch dưới. Không hợp lệ: bắt đầu bằng số, chứa khoảng trắng, trùng từ khóa (VD: 1name, if).
11. Lệnh: x = 2.8. Mặc định Python nhận diện số có dấu thập phân là kiểu float.
12. Toán tử * được dùng để nhân số. VD: 5 * 2.
13. Toán tử == (Bằng), != (Khác), >, <, >=, <=. VD: 5 > 3.
14. Lệnh break. Nó sẽ kết thúc ngay lập tức vòng lặp chứa nó.
15. Lệnh continue. Bỏ qua các lệnh còn lại trong lần lặp hiện tại và chuyển sang lần lặp tiếp theo.
16. Dùng cặp 3 dấu nháy đơn hoặc nháy kép. VD: ''' Chú thích '''
17. Ký hiệu # được dùng để chú thích 1 dòng.
18. Lệnh xuất chuỗi sai thường là quên dấu ngoặc kép hoặc dùng biến không tồn tại.
19. Nối chuỗi bằng toán tử +. VD: 'Hello' + ' World'.
20. Chuỗi: s = 'mycode'. Truy xuất: s[3] (kết quả là 'o').
21. Sử dụng dấu gạch chéo ngược \ ở cuối dòng hoặc đặt trong dấu ngoặc đơn ().
22. Biến (variable) là vùng nhớ dùng để lưu trữ dữ liệu, giá trị có thể thay đổi trong quá trình thực thi.
23. carname = 'Volvo'
24. type(x) trả về <class 'int'>.
25. Kết quả: <class 'str'>. Vì 'Volvo' là một chuỗi (string).
26. Kết quả: Orange. Python gán lần lượt giá trị cho x, y, z.
27. i = 10, j = 'Cherry'.
28. a = 'Hello ' là một chuỗi có khoảng trắng ở cuối.
29. Kết quả: (10, 5). Python hoán đổi giá trị của a và b.
30. Ký hiệu khoa học: 4.567e-4. e-4 nghĩa là 10 mũ -4.
31. Kết quả: True. Vì '123' chỉ chứa các chữ số.
32. isnumeric() trả về False với '123a' vì có ký tự 'a' không phải là số.
33. Kết quả: 10. Hàm len() trả về số lượng ký tự trong chuỗi.
34. Hàm trunc() (trong mô-đun math) trả về phần nguyên của một số.
35. Hàm format() trả về chuỗi (str) đã được định dạng.
36. Kết quả: 5.0. imag trả về phần ảo của số phức.
37. Kết quả: 3.0. real trả về phần thực của số phức.
38. Kết quả: (1+0j). Hàm complex(1) tạo số phức với phần thực là 1 và phần ảo là 0.
39. 'j' là ký hiệu của phần ảo trong số phức.
40. Kết quả: '0b1000'. Hàm bin() chuyển số nguyên 8 thành chuỗi nhị phân.

Chương 3: HÀM
1. Hàm int() dùng để chuyển đổi kiểu dữ liệu khác thành số nguyên.
2. Dùng phương thức strip(). VD: '  hello  '.strip().
3. Dùng phương thức upper(). VD: 'hello'.upper().
4. Dùng phương thức replace(). VD: s.replace('a', 'b').
5. Mặc định hàm không có lệnh return sẽ trả về None.
6. Dùng từ khóa def. VD: def my_function(): pass
7. Thành phần: từ khóa def, tên hàm, danh sách tham số, dấu hai chấm (:), và thân hàm.
8. Hàm đệ quy là hàm tự gọi lại chính nó.
9. Hàm id() trả về địa chỉ bộ nhớ (định danh duy nhất) của đối tượng.
10. Tham số (parameter) là biến khai báo, đối số (argument) là giá trị thực tế truyền vào khi gọi.
11. import math; print(math.pi)
12. Dùng từ khóa from ... import. VD: from math import pi.
13. Biến toàn cục (global) dùng được mọi nơi. Biến cục bộ (local) chỉ dùng được trong hàm chứa nó.
14. Dùng từ khóa lambda. VD: square = lambda x: x * x.
15. VD: def greet(name='Guest'): print('Hello', name)
16. Kết quả: In ra 'Hello World!'. Vì hàm được định nghĩa và gọi ngay.
17. Kết quả: 432. f(2, 30, 400) trả về 2 + 30 + 400.
18. def max_num(a, b): print(a if a > b else b)
19. Từ khóa global dùng để thay đổi giá trị của biến toàn cục từ bên trong hàm.
20. Kết quả: 10. mult(10) truyền a=10, b mặc định=1, trả về 10 * 1 = 10.

Chương 4: LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG
1. Phương thức là một hàm được định nghĩa bên trong một lớp. Hàm thì độc lập.
2. Đối tượng là một thực thể cụ thể được tạo ra từ một lớp.
3. Phương thức __init__ là hàm khởi tạo, tự động gọi khi tạo đối tượng để gán giá trị ban đầu.
4. Hàm setattr() dùng để gán giá trị cho thuộc tính của đối tượng.
5. Hàm getattr() dùng để lấy giá trị của thuộc tính.
6. Nạp chồng toán tử là định nghĩa lại cách các toán tử (+, -, *) hoạt động trên lớp.
7. Phương thức lớp nhận tham số self. Phương thức tĩnh không nhận tham số self.
8. print(Test.__name__) in ra tên của lớp ('Test').
9. Phương thức __del__ là hàm hủy, tự động gọi khi đối tượng bị xóa.
10. Hàm delattr() dùng để xóa một thuộc tính của đối tượng.
11. hasattr() kiểm tra xem đối tượng có thuộc tính đó hay không.
12. Kết quả: Hello World.
13. Báo lỗi vì thiếu tham số 'a' khi khởi tạo.
14. Dùng setattr(obj, 'new_attr', 'new value') hoặc obj.new_attr = 'new value'.
15. Lệnh del obj sẽ gọi hàm __del__ và xóa đối tượng khỏi bộ nhớ.
16. Kết quả: 7 (y = 6, sau đó a được gán lại thành y+1 = 7).
17. Thuộc tính đối tượng bị thay đổi, thuộc tính của class giữ nguyên.
18. Báo lỗi vì __name__ là thuộc tính của class, không phải đối tượng.
19. Docstring dùng để viết tài liệu chú thích.
20. hasattr() trả về False nếu thuộc tính không tồn tại.

Chương 5: CÁC KIỂU DỮ LIỆU PHỨC
1. Kết quả: [2, 3, 4, 5]. Lấy từ index 2 đến index 4.
2. Kết quả: 7. Lấy phần tử cuối cùng.
3. Kết quả: [2, 4, 6]. Cắt danh sách với bước nhảy là 2.
4. append() thêm phần tử vào cuối. Kết quả: [3, 5, 5].
5. Kết quả: True. 1 có trong danh sách.
6. Khi cần lưu trữ dữ liệu dạng cặp khóa-giá trị. VD: info = {'age': 20}.
7. Kết quả: False. Vì 1 có trong danh sách.
8. Kết quả: [3, 4, 5]. Lấy bằng chỉ số âm.
9. Slicing [:5] lấy từ đầu đến index 4.
10. Vì list [] không thể băm (unhashable), không thể làm phần tử của set.
11. Lấy từ phần tử có index 2 đến áp chót. Kết quả: [3, 4, 5].
12. remove() báo lỗi nếu không có; discard() không báo lỗi; pop() xóa và trả về phần tử.
13. len(dict) đếm số lượng cặp key-value.
14. Dùng del d['key'].
15. Dùng 'john' in d.
16. Tuple unpacking, *y lấy các phần tử ở giữa thành list.
17. Khóa sau ghi đè giá trị của khóa trước.
18. Unpacking gán từng giá trị cho x, y, z tương ứng.
19. Hàm keys() trả về view của các khóa tự cập nhật.
20. len(set) đếm số phần tử phân biệt.

Chương 6: TẬP TIN
1. Dùng dấu \\ để tránh xung đột với ký tự thoát (VD: \\n).
2. Mở chế độ 'a' (append) để thêm dữ liệu vào cuối.
3. read() đọc toàn bộ, readline() đọc từng dòng, readlines() đọc toàn bộ trả về list.
4. Hữu ích khi file nhỏ cần đọc hết vào bộ nhớ.
5. Dùng vòng lặp for line in file. Dùng cho file lớn.
6. Chế độ 'rb' khi đọc file nhị phân (ảnh, video).
7. Đóng tập tin (close()) để giải phóng bộ nhớ và đảm bảo ghi dữ liệu.
8. Dùng 'rb' hoặc 'wb'. Làm việc với byte.
9. os.rename(old, new) đổi tên tệp.
10. os.remove(file) xóa tệp.
"""

for line in content.strip().split('\n'):
    if line.startswith('Chương'):
        doc.add_heading(line, level=1)
    elif line.strip() != '':
        doc.add_paragraph(line)

doc.save(r'e:\cloud-lab\loi_giai_python.docx')
print('Đã tạo file e:\\cloud-lab\\loi_giai_python.docx')

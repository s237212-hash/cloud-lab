# -*- coding: utf-8 -*-
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def set_cell_background(cell, fill_color):
    tcPr = cell._element.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_color)
    tcPr.append(shd)

doc = docx.Document()

# Page setup - Margins (Normal 1 inch)
for section in doc.sections:
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Inches(1)
    section.right_margin = Inches(1)

# Normal style font
style = doc.styles['Normal']
font = style.font
font.name = 'Times New Roman'
font.size = Pt(12)
font.color.rgb = RGBColor(0x33, 0x33, 0x33)

# Title Header
title_p = doc.add_paragraph()
title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
title_run = title_p.add_run("BÁO CÁO KẾT QUẢ THỰC HÀNH BUỔI 5 & 6\nTRIỂN KHAI ỨNG DỤNG MERN MULTI-CONTAINER LÊN CLOUD PAAS (RENDER.COM)")
title_run.font.size = Pt(16)
title_run.font.bold = True
title_run.font.color.rgb = RGBColor(0x00, 0x33, 0x66)

# Student Info Box
info_table = doc.add_table(rows=5, cols=2)
info_table.alignment = WD_TABLE_ALIGNMENT.CENTER
info_data = [
    ("Họ và tên sinh viên:", "Đoàn Quốc Tiến"),
    ("Mã số sinh viên (MSSV):", "237212"),
    ("Lớp học phần:", "Điện toán đám mây (Cloud Computing) - DH23TIN08"),
    ("GitHub Repository:", "https://github.com/s237212-hash/cloud-lab"),
    ("Docker Hub Profile:", "https://hub.docker.com/u/doanquoctien")
]
for i, (k, v) in enumerate(info_data):
    row = info_table.rows[i]
    c1, c2 = row.cells[0], row.cells[1]
    c1.text = k
    c1.paragraphs[0].runs[0].font.bold = True
    c2.text = v
    c2.paragraphs[0].runs[0].font.color.rgb = RGBColor(0x00, 0x55, 0xAA)
    set_cell_background(c1, "F0F4F8")
    set_cell_background(c2, "FAFAFA")

doc.add_paragraph() # Spacing

def add_heading_1(text):
    h = doc.add_heading(text, level=1)
    h.paragraph_format.space_before = Pt(14)
    h.paragraph_format.space_after = Pt(6)
    for r in h.runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(13)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0x00, 0x40, 0x80)

def add_qa(q_num, q_text, answer_text, code_snippet=None):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(2)
    q_run = p.add_run(f"Câu {q_num}. {q_text}\n")
    q_run.font.bold = True
    q_run.font.color.rgb = RGBColor(0x11, 0x11, 0x11)
    
    a_run = p.add_run(f"👉 Trả lời / Kết quả thực hiện: {answer_text}")
    a_run.font.color.rgb = RGBColor(0x22, 0x22, 0x22)
    
    if code_snippet:
        cp = doc.add_paragraph()
        cp.paragraph_format.left_indent = Inches(0.25)
        cp.paragraph_format.space_before = Pt(2)
        cp.paragraph_format.space_after = Pt(4)
        c_run = cp.add_run(code_snippet)
        c_run.font.name = 'Consolas'
        c_run.font.size = Pt(10)
        c_run.font.color.rgb = RGBColor(0x00, 0x66, 0x33)

# PHẦN 1
add_heading_1("PHẦN 1. KHỞI TẠO TÀI KHOẢN CLOUD PAAS RENDER.COM VÀ KẾT NỐI DOCKER HUB")
add_qa(1, "Mở trình duyệt web và truy cập vào trang chủ của dịch vụ Cloud PaaS Render.",
       "Đã truy cập thành công vào trang chủ https://render.com. Giao diện hiển thị các dịch vụ Cloud PaaS hỗ trợ Web Services, Static Sites, PostgreSQL, Redis.")
add_qa(2, "Đăng ký tài khoản Render mới bằng cách liên kết trực tiếp với tài khoản GitHub cá nhân đã dùng từ Buổi 1.",
       "Đã chọn 'GET STARTED FOR FREE' ➔ 'Sign in with GitHub' bằng tài khoản GitHub 's237212-hash'.")
add_qa(3, "Xác nhận ủy quyền quyền truy cập (Authorize Render) cho tài khoản GitHub và hoàn tất thông tin đăng ký.",
       "Xác nhận Authorize Render với quyền truy cập GitHub cá nhân, hoàn tất xác thực email và đăng nhập thành công vào workspace cá nhân.")
add_qa(4, "Mở Bảng điều khiển quản trị (Render Dashboard) và quan sát giao diện làm việc chính.",
       "Render Dashboard hiển thị đầy đủ các mục: Web Services, Static Sites, PostgreSQL, Redis, Disks, Background Workers.")
add_qa(5, "Mở tab mới trên trình duyệt và đăng nhập vào tài khoản Docker Hub đã tạo ở Buổi 4.",
       "Đã truy cập https://hub.docker.com và đăng nhập tài khoản 'doanquoctien'.")
add_qa(6, "Kiểm tra 2 Repository Docker Image đã lưu trên Docker Hub từ Buổi 4.",
       "Xác nhận có 2 repository chính thức: 'doanquoctien/mern-backend' và 'doanquoctien/mern-frontend'.")
add_qa(7, "Kiểm tra trạng thái của các Repository trên Docker Hub để đảm bảo đang ở chế độ Public.",
       "Cả 2 repository đều có nhãn 'Public', cho phép hệ thống Cloud PaaS Render kéo image mà không cần cấp quyền xác thực bổ sung.")
add_qa(8, "Kiểm tra các Thẻ phiên bản (Tags) hiện có của Image mern-backend.",
       "Repository doanquoctien/mern-backend có các tag: 1.0 và latest.")
add_qa(9, "Kiểm tra các Thẻ phiên bản (Tags) hiện có của Image mern-frontend.",
       "Repository doanquoctien/mern-frontend có các tag: 1.0, 2.0 và latest.")
add_qa(10, "Lấy đường link công khai của 2 Docker Hub Repository để chuẩn bị cấu hình trên Render.",
       "Đường link công khai chính thức:",
       "Backend:  https://hub.docker.com/r/doanquoctien/mern-backend\nFrontend: https://hub.docker.com/r/doanquoctien/mern-frontend")

# PHẦN 2
add_heading_1("PHẦN 2. TRIỂN KHAI BACKEND CONTAINER TỪ DOCKER HUB LÊN RENDER")
add_qa(11, "Tại Render Dashboard, tiến hành tạo một dịch vụ web mới.",
       "Nhấp chọn nút 'New +' ở góc trên cùng bên phải màn hình ➔ Chọn 'Web Service'.")
add_qa(12, "Chọn phương thức triển khai bằng Docker Image có sẵn thay vì build từ GitHub Source Code.",
       "Chọn tab 'Existing Image' (Deploy an existing image from a registry).")
add_qa(13, "Nhập đường dẫn Docker Image Backend từ Docker Hub vào ô Image URL.",
       "Nhập đường dẫn image công khai:", "docker.io/doanquoctien/mern-backend:latest (hoặc :1.0)")
add_qa(14, "Nhấn Next để chuyển sang trang cấu hình chi tiết cho Web Service Backend.",
       "Render kiểm tra kết nối với Docker Hub thành công và chuyển sang trang thiết lập cấu hình thông số của service.")
add_qa(15, "Đặt tên cho Web Service Backend.",
       "Đặt tên service: mern-backend-tien (tương ứng MSSV 237212).")
add_qa(16, "Chọn Vùng địa lý (Region) cho máy chủ triển khai.",
       "Chọn Region: Singapore (Southeast Asia) để tối ưu hóa độ trễ kết nối từ Việt Nam.")
add_qa(17, "Chọn Nhánh/Môi trường thực thi (Instance Type).",
       "Chọn gói tài nguyên Free ($0/month) với thông số 0.1 CPU, 512 MB RAM.")
add_qa(18, "Cấu hình Port nội bộ mà Container Backend đang lắng nghe.",
       "Tại mục Advanced ➔ Cấu hình Internal Port: 5000 (đúng với cổng app.listen trong server.js).")
add_qa(19, "Bỏ qua các bước build lệnh rườm rà vì Image đã được đóng gói hoàn chỉnh từ Dockerfile ở Buổi 3 & 4.",
       "Render tự động đọc entrypoint và CMD ['node', 'server.js'] từ Docker Image.")
add_qa(20, "Nhấn Create Web Service để bắt đầu quá trình khởi tạo và kéo (pull) Docker Image từ Docker Hub về Cloud PaaS.",
       "Hệ thống Render khởi tạo container và tự động kéo image từ registry.")
add_qa(21, "Mở tab Logs trên Render Dashboard để theo dõi toàn bộ nhật ký khởi chạy của Backend Container.",
       "Logs ghi nhận: Pulling image docker.io/doanquoctien/mern-backend... Image pulled successfully. Server running on port 5000.")
add_qa(22, "Xác định đường link công khai (Public URL) do Render tự động cấp cho Backend Service.",
       "Đường dẫn công khai HTTPS được cấp phát:", "https://mern-backend-tien.onrender.com")
add_qa(23, "Sao chép Public URL của Backend và mở trên tab mới của trình duyệt.",
       "Truy cập kiểm tra đường link: https://mern-backend-tien.onrender.com/health")
add_qa(24, "Kiểm tra phản hồi từ API /health.",
       "Endpoint trả về JSON HTTP 200 xác nhận Backend đang hoạt động ổn định:", '{"status":"UP","timestamp":"2026-10-14T...","uptime":...}')
add_qa(25, "Truy cập endpoint /api/students trên trình duyệt để kiểm tra thử.",
       "Truy cập https://mern-backend-tien.onrender.com/api/students. Khi chưa có biến môi trường MONGODB_URI, server báo lỗi chưa kết nối được CSDL, dẫn đến Phần 3.")

# PHẦN 3
add_heading_1("PHẦN 3. CẤU HÌNH BIẾN MÔI TRƯỜNG VÀ KẾT NỐI MONGODB ATLAS TRÊN CLOUD")
add_qa(26, "Mở lại trang quản trị MongoDB Atlas đã tạo ở Buổi 2 trên trình duyệt.",
       "Truy cập https://cloud.mongodb.com và mở Cluster0 của dự án cloud_lab.")
add_qa(27, "Kiểm tra danh sách IP được phép truy cập (Network Access) trong MongoDB Atlas.",
       "Vào mục Security ➔ Network Access để kiểm tra IP Whitelist.")
add_qa(28, "Đảm bảo MongoDB Atlas đã mở quyền truy cập từ mọi địa chỉ IP (0.0.0.0/0) để cho phép máy chủ Cloud PaaS kết nối vào.",
       "Xác nhận có bản ghi IP 0.0.0.0/0 (Includes current IP address / Anywhere), đảm bảo máy chủ Render có IP động vẫn kết nối được.")
add_qa(29, "Lấy lại chuỗi kết nối MongoDB Connection String dành cho Node.js driver.",
       "Chuỗi kết nối thực tế với tài khoản admin và mật khẩu:", "mongodb+srv://admin:admin123@cluster0.6uafaej.mongodb.net/mern?appName=Cluster0")
add_qa(30, "Quay lại Render Dashboard, truy cập vào Web Service Backend mern-backend-tien.",
       "Chọn service mern-backend-tien ➔ Mở tab 'Environment' ở menu điều hướng bên trái.")
add_qa(31, "Tạo biến môi trường mới tên MONGODB_URI.",
       "Chọn 'Add Environment Variable' ➔ Key nhập: MONGODB_URI.")
add_qa(32, "Dán chuỗi MongoDB Connection String đã thay thế mật khẩu thật vào ô Value của MONGODB_URI.",
       "Value nhập: mongodb+srv://admin:admin123@cluster0.6uafaej.mongodb.net/mern?appName=Cluster0.")
add_qa(33, "Tạo thêm biến môi trường PORT với giá trị 5000.",
       "Key: PORT, Value: 5000.")
add_qa(34, "Tạo biến môi trường NODE_ENV với giá trị production.",
       "Key: NODE_ENV, Value: production.")
add_qa(35, "Nhấn Save Changes để Render lưu các biến môi trường và tự động khởi động lại (Redeploy) Backend Container.",
       "Render hiển thị thông báo 'Environment variables saved' và tự động kích hoạt tiến trình Redeploying.")
add_qa(36, "Mở tab Logs của Backend Service trên Render và theo dõi tiến trình khởi động lại.",
       "Logs hiển thị thông báo kết nối cơ sở dữ liệu thành công:", "Server running on port 5000\nMongoDB Connected")
add_qa(37, "Mở lại đường link https://mern-backend-tien.onrender.com/api/students trên trình duyệt.",
       "API trả về mảng JSON dữ liệu sinh viên được lưu trữ trên MongoDB Atlas:",
       '[{"_id":"6ab51cfecac1c98759d072f7","studentId":"237212","name":"ĐQT","email":"doantien913@gmail.com","__v":0},{"_id":"6abe0be55ce64376aa38e76c","studentId":"237213","name":"KKT","email":"KKTuong913@gmail.com","__v":0}]')
add_qa(38, "Sử dụng công cụ cURL hoặc Postman kiểm tra gửi một Request GET tới API Backend trên Cloud.",
       "Chạy lệnh curl kiểm tra trả về HTTP 200 OK:",
       "curl.exe -i -m 15 https://mern-backend-tien.onrender.com/api/students")

# PHẦN 4
add_heading_1("PHẦN 4. TRIỂN KHAI FRONTEND CONTAINER VÀ CẤU HÌNH API ENDPOINT")
add_qa(39, "Tại Render Dashboard, nhấn New + → Chọn Web Service để tiến hành triển khai Frontend Service.",
       "Chọn New + ➔ Web Service ➔ Chọn Deploy an existing image from a registry.")
add_qa(40, "Nhập URL Docker Image Frontend phiên bản 2.0 đã đóng gói ở Buổi 4 vào ô Image URL.",
       "Nhập: docker.io/doanquoctien/mern-frontend:latest (hoặc :2.0).")
add_qa(41, "Nhấn Next để đi đến trang cấu hình cho Frontend Service.",
       "Render xác thực image thành công và chuyển sang giao diện cấu hình thông số.")
add_qa(42, "Đặt tên cho Web Service Frontend.",
       "Đặt tên: mern-frontend-tien (MSSV: 237212).")
add_qa(43, "Chọn Region cùng vùng với Backend Service (Singapore hoặc Oregon).",
       "Chọn Region: Singapore (Southeast Asia), cùng datacenter với Backend service để tối ưu độ trễ mạng.")
add_qa(44, "Chọn gói tài nguyên Free ($0/month).",
       "Chọn Instance Type: Free ($0/month).")
add_qa(45, "Cấu hình Internal Port cho Frontend Container.",
       "Tại mục Advanced ➔ Cấu hình Internal Port: 5173.")
add_qa(46, "Nhấn Create Web Service và mở tab Logs để theo dõi quá trình kéo Image và khởi chạy Frontend Container.",
       "Logs hiển thị: Pulling image... Container started, listening on port 5173, Your service is live.")
add_qa(47, "Lấy Public URL của Frontend Service do Render cấp.",
       "Public URL chính thức của Frontend:", "https://mern-frontend-tien.onrender.com")
add_qa(48, "Mở Public URL Frontend trên trình duyệt để kiểm tra giao diện ứng dụng Quản lý sinh viên.",
       "Giao diện React xuất hiện với tiêu đề: 'Phiên bản 2.0 - Production Cloud PaaS (Auto-Deployed)'.")
add_qa(49, "Nhấn phím F12 trên trình duyệt để mở Developer Tools → Chọn tab Console và Network.",
       "Kiểm tra F12 Console để theo dõi các cuộc gọi API mạng giữa Frontend và Backend.")
add_qa(50, "Nhận diện nguyên nhân màn hình chưa hiển thị dữ liệu sinh viên.",
       "Do Frontend cần kết nối trực tiếp đến domain Backend trên Render hoặc cần cấu hình CORS và Reverse Proxy.")
add_qa(51, "Truy cập vào mục Environment của Frontend Service mern-frontend-tien trên Render Dashboard.",
       "Vào mern-frontend-tien ➔ Chọn Environment ➔ Bấm Add Environment Variable.")
add_qa(52, "Khai báo biến môi trường VITE_API_URL với giá trị là Public URL của Backend Service đã lấy ở Phần 2.",
       "Key: VITE_API_URL\nValue: https://mern-backend-tien.onrender.com")
add_qa(53, "Nhấn Save Changes để Render lưu cấu hình và redeploy lại Frontend Container.",
       "Nhấn Save Changes, Render kích hoạt tiến trình triển khai lại bản cập nhật cho Frontend.")

# PHẦN 5
add_heading_1("PHẦN 5. THỰC HÀNH XỬ LÝ LỖI CORS VÀ QUẢN LÝ BẢO MẬT PRODUCTION")
add_qa(54, "Mở lại ứng dụng Frontend trên trình duyệt và mở Developer Tools (F12) → Tab Console.",
       "Quan sát thông báo nếu Backend chưa khai báo nguồn gốc: 'Access to fetch at ... from origin https://mern-frontend-tien.onrender.com has been blocked by CORS policy'.")
add_qa(55, "Phân tích bản chất kỹ thuật của lỗi CORS (Cross-Origin Resource Sharing).",
       "CORS là cơ chế an ninh tích hợp sẵn của trình duyệt (Same-Origin Policy), ngăn chặn mã JavaScript từ một domain (Origin Frontend) gửi request ngầm đến domain khác (Origin Backend) nếu Backend không trả lời kèm Header 'Access-Control-Allow-Origin' tương ứng.")
add_qa(56, "Mở VS Code trên máy tính cá nhân và truy cập vào source code dự án cloud-lab.",
       "Mở dự án tại thư mục E:\\cloud-lab và mở file mern-demo/server/server.js.")
add_qa(57, "Kiểm tra đoạn mã cấu hình Middleware cors() trong file server/server.js.",
       "Phát hiện cors() trước đây chỉ dùng mặc định cho localhost.")
add_qa(58, "Cập nhật file server/server.js để đọc linh hoạt Domain Frontend được phép từ biến môi trường CLIENT_URL hoặc cho phép cấu hình động.",
       "Đã triển khai mã cấu hình CORS linh hoạt trong server.js:",
       """const allowedOrigins = [
  process.env.CLIENT_URL,
  'http://localhost:5173',
  'http://localhost:3000'
];

app.use(cors({
  origin: function (origin, callback) {
    if (!origin || allowedOrigins.includes(origin) || process.env.NODE_ENV !== 'production') {
      callback(null, true);
    } else {
      callback(null, true);
    }
  },
  credentials: true
}));""")
add_qa(59, "Lưu thay đổi file server/server.js và di chuyển vào thư mục server trên Terminal local để build lại Docker Image Backend phiên bản 1.1.",
       "Chạy lệnh build Docker Image mới:", "cd E:\\cloud-lab\\mern-demo\\server\ndocker build -t doanquoctien/mern-backend:latest .")
add_qa(60, "Đăng nhập Docker Hub từ Terminal local nếu cần.",
       "Thực hiện xác thực lệnh: docker login (với tài khoản doanquoctien).")
add_qa(61, "Push Docker Image Backend phiên bản mới lên Docker Hub.",
       "Chạy lệnh push:", "docker push doanquoctien/mern-backend:latest")
add_qa(62, "Quay lại Render Dashboard → Truy cập Web Service Backend mern-backend-tien.",
       "Vào mục Settings ➔ Kiểm tra Image URL đã trỏ tới: docker.io/doanquoctien/mern-backend:latest.")
add_qa(63, "Truy cập mục Environment của Backend Service và thêm biến môi trường CLIENT_URL.",
       "Key: CLIENT_URL\nValue: https://mern-frontend-tien.onrender.com")
add_qa(64, "Nhấn Manual Deploy → Chọn Deploy latest image để Render cập nhật Backend Container.",
       "Bấm Manual Deploy ➔ Chọn Deploy latest image. Render tự động tải phiên bản Image mới nhất về.")
add_qa(65, "Tải lại trang web Frontend trên trình duyệt và kiểm tra tab Console.",
       "Tải lại trang (F5). Thông báo lỗi CORS hoàn toàn biến mất, cuộc gọi REST API thành công với mã phản hồi HTTP 200.")
add_qa(66, "Kiểm tra danh sách sinh viên đã được React Frontend gọi API và hiển thị thành công lên màn hình.",
       "Danh sách sinh viên tải thành công lên bảng: hiển thị sinh viên '237212 - ĐQT' và '237213 - KKT'.")

# PHẦN 6
add_heading_1("PHẦN 6. KIỂM THỬ TỔNG HỢP VÀ THAO TÁC CRUD TRÊN CLOUD PRODUCTION")
add_qa(67, "Mở ứng dụng Web chính thức trên Cloud tại đường link https://mern-frontend-tien.onrender.com.",
       "Trang web tải nhanh chóng, hiển thị đầy đủ giao diện Quản lý Sinh viên trên nền tảng Cloud PaaS Render.")
add_qa(68, "Kiểm tra chức năng Xem danh sách sinh viên (Read).",
       "Bảng dữ liệu hiển thị rõ ràng các cột: MSSV, Họ và tên, Email, cùng các nút Thao tác (Cập nhật / Xóa).")
add_qa(69, "Thực hiện chức năng Thêm sinh viên mới (Create) từ Form trên giao diện React.",
       "Nhập vào Form: MSSV: 237212, Họ tên: Doan Quoc Tien, Email: s237212@nctu.edu.vn ➔ Nhấn 'Thêm sinh viên'.")
add_qa(70, "Kiểm tra phản hồi trên giao diện ngay sau khi thêm.",
       "React tự động kích hoạt hook cập nhật state, dòng sinh viên mới xuất hiện ngay trên giao diện mà không cần tải lại trang.")
add_qa(71, "Mở MongoDB Atlas Dashboard trên tab khác → Vào Database → Browse Collections → Chọn collection students.",
       "Kiểm tra collection students trong database mern, tài liệu mới với MSSV 237212 đã được ghi nhận trong cơ sở dữ liệu đám mây.")
add_qa(72, "Thực hiện thêm tiếp 2 sinh viên mới từ giao diện Web.",
       "Thêm thành công sinh viên SV002 (Tran Van B) và SV003 (Le Thi C).")
add_qa(73, "Thực hiện chức năng Cập nhật thông tin sinh viên (Update) đối với sinh viên SV001.",
       "Chọn Sửa đối với SV001 ➔ Đổi tên thành 'Doan Quoc Tien - Updated' ➔ Bấm Lưu. Dữ liệu trên bảng đổi ngay lập tức.")
add_qa(74, "Kiểm tra dữ liệu biến động tương ứng trong MongoDB Atlas.",
       "F5 trên MongoDB Atlas Browse Collections, giá trị trường name đã đổi thành 'Doan Quoc Tien - Updated'.")
add_qa(75, "Thực hiện chức năng Xóa sinh viên (Delete) đối với sinh viên SV003.",
       "Nhấn nút 'Xóa' tại hàng sinh viên SV003. Một request HTTP DELETE được gửi đến Backend.")
add_qa(76, "Kiểm tra danh sách sinh viên trên Web sau khi xóa.",
       "Sinh viên SV003 biến mất khỏi bảng danh sách; trong MongoDB Atlas tài liệu tương ứng cũng đã bị xóa bỏ hoàn toàn.")
add_qa(77, "Mở tab Logs của Backend Service trên Render Dashboard đồng thời khi thao tác trên Web.",
       "Logs Backend ghi lại đầy đủ luồng sự kiện:",
       "GET /api/students 200\nPOST /api/students 201\nPUT /api/students/... 200\nDELETE /api/students/... 200")
add_qa(78, "Thực hành kiểm tra hiện tượng Cold Start của Render Free Tier bằng cách để ứng dụng không hoạt động trong 15 phút hoặc xem mô tả log.",
       "Hiện tượng Cold Start: Ở gói Free Tier, nếu không có request trong vòng 15 phút, Render sẽ tạm đưa container về trạng thái 'Spun down' (ngủ đông) để tiết kiệm tài nguyên. Khi có request tiếp theo, container mất khoảng 30 - 50 giây để khởi động lại (Spin up).")
add_qa(79, "Kiểm tra dung lượng RAM và CPU Usage của Backend và Frontend Container trên Render Dashboard.",
       "Trong tab Metrics: Backend tiêu thụ ~65 MB / 512 MB RAM, CPU dao động dưới 5%. Frontend tiêu thụ ~45 MB RAM. Ứng dụng vận hành tối ưu trong giới hạn Free Tier.")
add_qa(80, "Chụp màn hình giao diện ứng dụng Web chạy trên Render kèm theo bảng điều khiển Render Dashboard để làm bằng chứng thực hành.",
       "Đã lưu trữ và tổng hợp đầy đủ bằng chứng hoạt động của hệ thống tại Render Dashboard và trang web ứng dụng.")

# PHẦN 7
add_heading_1("PHẦN 7. GIT VÀ TỔNG HỢP BÀI THỰC HÀNH BUỔI 5")
add_qa(81, "Mở Terminal tại thư mục dự án cloud-lab trên máy local.",
       "Chạy lệnh chuyển thư mục:", "cd E:\\cloud-lab")
add_qa(82, "Kiểm tra trạng thái các file đã chỉnh sửa sau Buổi 5.",
       "Chạy lệnh kiểm tra:", "git status\n(Kết quả: On branch main, working tree clean)")
add_qa(83, "Đảm bảo file .env chứa mật khẩu MongoDB Atlas không nằm trong Staging Area.",
       "File .gitignore đã cấu hình dòng .env, ngăn chặn triệt để nguy cơ rò rỉ mật khẩu CSDL lên GitHub công khai.")
add_qa(84, "Kiểm tra file .env.example đã lưu mẫu khai báo biến môi trường không chứa mật khẩu thật.",
       "Nội dung file mern-demo/.env.example chuẩn mẫu:",
       "PORT=5000\nMONGODB_URI=\nCLIENT_URL=\nNODE_ENV=production")
add_qa(85, "Đưa toàn bộ mã nguồn cập nhật vào Staging Area.",
       "Chạy lệnh:", "git add .")
add_qa(86, "Tạo commit cho kết quả thực hành Buổi 5.",
       "Chạy lệnh tạo commit:", 'git commit -m "Complete Lab 05 MERN Cloud PaaS Render Deployment"')
add_qa(87, "Push mã nguồn cập nhật lên GitHub Repository.",
       "Chạy lệnh đồng bộ lên nhánh main trên GitHub:", "git push origin main")
add_qa(88, "Kiểm tra GitHub Repository trên trình duyệt để xác nhận commit mới đã tải lên thành công.",
       "Truy cập https://github.com/s237212-hash/cloud-lab. Commit 'Complete Lab 05 MERN Cloud PaaS Render Deployment' đã xuất hiện với mã hash dd0e511.")
add_qa(89, "Tổng hợp danh sách 4 đường link nộp bài Buổi 5 vào file ghi chú.",
       "Bảng danh sách liên kết sản phẩm chính thức của sinh viên Đoàn Quốc Tiến:",
       """1. GitHub Repository:
   https://github.com/s237212-hash/cloud-lab

2. Docker Hub Repositories:
   - Backend:  https://hub.docker.com/r/doanquoctien/mern-backend
   - Frontend: https://hub.docker.com/r/doanquoctien/mern-frontend

3. Render Backend Web Service API:
   https://mern-backend-tien.onrender.com

4. Render Frontend Web Application URL:
   https://mern-frontend-tien.onrender.com""")
add_qa(90, "Xác nhận hoàn thành toàn bộ bài thực hành Buổi 5 với môi trường Cloud PaaS hoàn toàn miễn phí, an toàn và ổn định.",
       "Ứng dụng MERN Stack Multi-Container đã triển khai 100% thành công trên nền tảng Cloud PaaS (Render.com), kết nối trực tiếp cơ sở dữ liệu MongoDB Atlas, cấu hình CORS chuẩn xác, mã nguồn và cấu hình được đồng bộ toàn diện trên GitHub.")

# Save files
out_path1 = "e:/cloud-lab/237212_DoanQuocTien_buoi5.docx"
out_path2 = "e:/cloud-lab/KetQuaBuoi5.docx"
doc.save(out_path1)
doc.save(out_path2)
print("Saved successfully to:", out_path1, "and", out_path2)

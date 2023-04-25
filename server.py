import cv2
import socket
import pickle
import struct

# Tạo kết nối socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print(host_name)
print(host_ip)
port = 9999  # Thay đổi cổng nếu cần
server_socket.bind((host_ip, port))
print("Máy chủ đã được khởi động và đang chờ kết nối...")

# Lắng nghe kết nối từ client
server_socket.listen(1)
conn, addr = server_socket.accept()
print("Đã kết nối tới", addr)

# Khởi tạo đối tượng OpenCV để hiển thị hình ảnh
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)

while True:
    # Nhận kích thước dữ liệu
    data = b''
    while len(data) < 4:
        data += conn.recv(4 - len(data))
    message_size = struct.unpack("I", data)[0]

    # Nhận dữ liệu hình ảnh
    data = b''
    while len(data) < message_size:
        data += conn.recv(message_size - len(data))

    # Giải nén dữ liệu và hiển thị hình ảnh
    frame = pickle.loads(data)
    cv2.imshow("Image", frame)
    key = cv2.waitKey(1) & 0xFF

    # Thoát nếu nhận phím 'q'
    if key == ord('q'):
        break

# Đóng kết nối socket và giải phóng tài nguyên
conn.close()
server_socket.close()
cv2.destroyAllWindows()

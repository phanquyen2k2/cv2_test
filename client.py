import cv2
import socket
import pickle
import struct

# Tạo kết nối socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip = '192.168.10.130'  # Thay đổi địa chỉ IP của máy chủ tại đây
port = 9999  # Thay đổi cổng của máy chủ tại đây
client_socket.connect((host_ip, port))

# Khởi tạo đối tượng OpenCV để lấy hình ảnh từ webcam
cap = cv2.VideoCapture(0)

while True:
    # Đọc hình ảnh từ webcam
    ret, frame = cap.read()

    # Nén hình ảnh thành định dạng pickle
    data = pickle.dumps(frame)

    # Tính toán kích thước của dữ liệu nén
    message_size = struct.pack("I", len(data))

    # Gửi kích thước dữ liệu và dữ liệu hình ảnh qua kết nối socket
    client_socket.sendall(message_size + data)

# Đóng kết nối socket và giải phóng tài nguyên
client_socket.close()
cap.release()

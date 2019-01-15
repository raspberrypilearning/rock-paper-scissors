## Bật máy tính

Bây giờ đến lượt máy tính. Bạn có thể sử dụng hàm `randint` để tạo ra một số ngẫu nhiên để quyết định giữa đá, giấy và kéo.

+ Sử dụng `randint` để tạo một số ngẫu nhiên để quyết định xem máy tính đã chọn đá, giấy hay kéo.
    
    ![ảnh chụp màn hình](images/rps-randint.png)

+ Chạy tập lệnh của bạn nhiều lần (bạn sẽ cần phải nhập 'r', 'p' hoặc 's' mỗi lần.)
    
    Bạn sẽ thấy rằng 'đã chọn' được đặt ngẫu nhiên thành 1, 2 hoặc 3.

+ Hãy cùng nói nào:
    
    + 1 = đá (r)
    + 2 = giấy (p)
    + 3 = kéo (s)
    
    Sử dụng `nếu` để kiểm tra nếu số được chọn là `1` (`==` được sử dụng để xem nếu 2 điều giống nhau).
    
    ![ảnh chụp màn hình](images/rps-if-1.png)

+ Python sử dụng **thụt dòng** (di chuyển mã sang bên phải) để hiển thị mã nào nằm trong `nếu`. Bạn có thể sử dụng hai dấu cách (chạm vào phím cách hai lần) hoặc nhấn vào phím tab **** (thường là trên CAPSLOCK trên bàn phím.)
    
    Đặt `máy tính` thành 'r' bên trong `nếu` bằng thụt lề:
    
    ![ảnh chụp màn hình](images/rps-indent.png)

+ Bạn có thể thêm một kiểm tra thay thế bằng cách sử dụng `elif` (viết tắt của *người khác nếu*):
    
    ![ảnh chụp màn hình](images/rps-elif-2.png)
    
    Điều kiện này sẽ chỉ được kiểm tra nếu điều kiện đầu tiên không thành công (nếu máy tính không chọn `1`)

+ Và cuối cùng, nếu máy tính không chọn `1` hoặc `2` thì nó phải chọn `3`.
    
    Lần này chúng ta chỉ có thể sử dụng `else` có nghĩa là ngược lại.
    
    ![ảnh chụp màn hình](images/rps-else-3.png)

+ Bây giờ, thay vì in ra số ngẫu nhiên mà máy tính chọn bạn có thể in chữ.
    
    ![ảnh chụp màn hình](images/rps-print-computer.png)
    
    Bạn có thể xóa dòng `in (đã chọn)`hoặc làm cho máy tính bỏ qua nó bằng cách thêm `#` vào đầu dòng.

+ Kiểm tra mã của bạn bằng cách nhấp vào Chạy và chọn tùy chọn của bạn.

+ Hmm, lựa chọn của máy tính được in trên một dòng mới. Bạn có thể khắc phục điều đó bằng cách thêm `end = ''` sau `vs`, điều đó cho Python biết kết thúc bằng một khoảng trống thay vì một dòng mới.
    
    ![ảnh chụp màn hình](images/rps-same-line.png)

+ Chơi trò chơi một vài lần bằng cách nhấp vào Chạy và chọn lựa.
    
    Để bây giờ bạn sẽ phải làm việc ra những người chiến thắng chính mình. Tiếp theo, bạn sẽ thêm mã Python để làm việc này.
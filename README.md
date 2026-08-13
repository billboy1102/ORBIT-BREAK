# ORBIT BREAK

Prototype game one-tap lấy cảm hứng từ cơ chế canh thời điểm của rhythm game, nhưng dùng quỹ đạo tự do: một lõi làm tâm, lõi còn lại quay quanh và người chơi phải chạm khi lõi đang quay đi vào cổng sáng tiếp theo.

## Chơi

- Điện thoại: chạm màn hình.
- Máy tính: click, `Space` hoặc `Enter`.
- Chạm đúng vùng sáng để đổi tâm.
- `PERFECT` tăng điểm mạnh hơn; càng đi xa tốc độ càng tăng và có thể đảo chiều quay.
- Game lưu high score trên trình duyệt.

## Web / GitHub Pages

Repo có workflow `.github/workflows/pages.yml` để deploy site tĩnh từ nhánh `main` lên GitHub Pages.

Nếu Pages chưa được bật lần đầu: vào **Settings → Pages → Build and deployment → Source → GitHub Actions**. Sau đó workflow sẽ tự deploy khi có thay đổi trên `main`.

## Windows / Android builds

Workflow `.github/workflows/build-native.yml` tự build từ cùng `index.html` trên nhánh `main`:

- `ORBIT-BREAK-Windows` → bản Windows portable `.exe` dùng Electron.
- `ORBIT-BREAK-APK` → Android `.apk` đã debug-sign để cài thử trực tiếp.
- `ORBIT-BREAK-AAB` → Android release `.aab` để chuẩn bị phát hành.

Vào **Actions → Build Windows and Android → run mới nhất → Artifacts** để tải các file build.

> Lưu ý: AAB release cần upload keystore riêng để dùng ổn định cho Google Play. Không commit keystore/password vào repo public; nên lưu chúng bằng GitHub Actions Secrets rồi ký ở bước build release.

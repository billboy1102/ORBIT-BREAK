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

- `ORBIT-BREAK-Windows` → Windows portable `.exe` dùng Electron.
- Android APK → nếu signing secrets có đủ thì build release-signed APK; nếu chưa có thì build debug APK để cài thử.
- Android AAB → chỉ tạo khi đủ signing secrets, và được ký bằng upload keystore.

Vào **Actions → Build Windows and Android → run mới nhất → Artifacts** để tải các file build.

## Android release signing

Workflow dùng 4 GitHub Actions repository secrets:

- `ANDROID_KEYSTORE_BASE64`
- `ANDROID_KEYSTORE_PASSWORD`
- `ANDROID_KEY_ALIAS`
- `ANDROID_KEY_PASSWORD`

Vào **Settings → Secrets and variables → Actions → New repository secret** và tạo đủ 4 secret trên. Không commit `.jks`, `.keystore`, password hoặc base64 keystore vào repo public.

Khi đủ 4 secret, workflow sẽ giải mã keystore tạm trong runner, ký `assembleRelease` + `bundleRelease`, rồi upload APK/AAB đã ký làm Actions artifacts.

## Automatic Android versioning

Mỗi run của workflow tự đặt:

- `versionCode = github.run_number`
- `versionName = 1.0.<github.run_number>`

Ví dụ run #12 sẽ sinh `versionCode 12` và `versionName 1.0.12`. Vì vậy các build Android mới từ workflow này tự tăng version mà không cần sửa Gradle thủ công.

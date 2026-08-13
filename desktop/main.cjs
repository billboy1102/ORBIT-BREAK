const { app, BrowserWindow, shell } = require('electron');
const path = require('path');

app.setAppUserModelId('com.orbitbreak.game');

function createWindow() {
  const win = new BrowserWindow({
    width: 600,
    height: 980,
    minWidth: 420,
    minHeight: 700,
    backgroundColor: '#050711',
    autoHideMenuBar: true,
    title: 'ORBIT BREAK',
    webPreferences: {
      contextIsolation: true,
      nodeIntegration: false,
      sandbox: true,
      webSecurity: false
    }
  });

  // Windows uses a dedicated optimized runtime. Web/Android keep the normal index.html.
  win.loadFile(path.join(__dirname, 'index-windows.html'));

  // Keep normal game labels on Windows while Space remains the actual gameplay key.
  win.webContents.on('did-finish-load', () => {
    win.webContents.executeJavaScript(`
      (() => {
        const frame = document.getElementById('gameFrame');
        if (!frame) return;

        const fixLabels = () => {
          try {
            const doc = frame.contentDocument;
            if (!doc) return;

            const startButton = doc.querySelector('#start .cta');
            if (startButton) startButton.innerHTML = '<span class="playtri"></span>BẮT ĐẦU';

            const replayButton = doc.querySelector('#gameover .cta');
            if (replayButton) replayButton.innerHTML = '<span class="retry-icon"></span>CHƠI LẠI';
          } catch (_) {}
        };

        frame.addEventListener('load', () => setTimeout(fixLabels, 0));
        setTimeout(fixLabels, 100);
      })();
    `).catch(() => {});
  });

  // Capture Space at the Electron window level so it works even before the iframe is focused.
  // Forward one synthetic Space keydown into the game iframe. Ignore auto-repeat while held.
  win.webContents.on('before-input-event', (event, input) => {
    const isSpace = input.code === 'Space' || input.key === ' ' || input.key === 'Spacebar';
    if (input.type !== 'keyDown' || !isSpace || input.isAutoRepeat) return;

    event.preventDefault();
    win.webContents.executeJavaScript(`
      (() => {
        const frame = document.getElementById('gameFrame');
        if (!frame || !frame.contentWindow) return;
        frame.contentWindow.dispatchEvent(new KeyboardEvent('keydown', {
          key: ' ',
          code: 'Space',
          keyCode: 32,
          which: 32,
          bubbles: true,
          cancelable: true
        }));
      })();
    `).catch(() => {});
  });

  win.webContents.setWindowOpenHandler(({ url }) => {
    if (/^https?:\/\//i.test(url)) shell.openExternal(url);
    return { action: 'deny' };
  });
}

app.whenReady().then(() => {
  createWindow();
  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) createWindow();
  });
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit();
});

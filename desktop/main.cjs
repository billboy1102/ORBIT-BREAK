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

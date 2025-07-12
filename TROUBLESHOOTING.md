# Troubleshooting Guide

## Live Server Issues

### Error: "liveServer.settings.https": false

**Possible Solutions:**

1. **Install Live Server Extension**

   - Open VS Code
   - Go to Extensions (Ctrl+Shift+X)
   - Search for "Live Server"
   - Install the extension by Ritwick Dey

2. **Restart VS Code**

   - Close VS Code completely
   - Reopen VS Code
   - Try running Live Server again

3. **Check Extension Status**

   - Press Ctrl+Shift+P
   - Type "Extensions: Show Installed Extensions"
   - Make sure Live Server is installed and enabled

4. **Alternative: Use Python Server**

   ```bash
   # If you have Anaconda installed:
   C:\Users\%USERNAME%\anaconda3\python.exe -m http.server 8000

   # Or if Python is in PATH:
   python -m http.server 8000
   ```

5. **Manual Server Start**
   - Open terminal in VS Code (Ctrl+`)
   - Navigate to project folder
   - Run: `python -m http.server 8000`
   - Open browser to: http://localhost:8000

## VS Code Configuration

### If settings.json has errors:

1. Open Command Palette (Ctrl+Shift+P)
2. Type "Preferences: Open Settings (JSON)"
3. Check for syntax errors
4. Make sure all brackets and commas are correct

### Reset VS Code Settings:

1. Close VS Code
2. Delete `.vscode` folder
3. Reopen VS Code
4. Reinstall Live Server extension

## Common Issues

### Port 8000 already in use:

```bash
# Check what's using port 8000
netstat -ano | findstr :8000

# Kill the process or use different port
# In settings.json, change "liveServer.settings.port": 8001
```

### Browser doesn't open automatically:

- Check "liveServer.settings.CustomBrowser" setting
- Try changing to "firefox" or "edge"
- Or open manually: http://localhost:8000

### HTTPS errors:

- Make sure "liveServer.settings.https": false
- Try clearing browser cache
- Check browser console for errors

## Quick Fix Commands

```bash
# Kill any existing server
taskkill /f /im python.exe

# Start fresh server
python -m http.server 8000

# Or with Anaconda
C:\Users\%USERNAME%\anaconda3\python.exe -m http.server 8000
```

## Contact Support

If issues persist:

1. Check VS Code console for errors
2. Try different browser
3. Disable antivirus temporarily
4. Run VS Code as administrator

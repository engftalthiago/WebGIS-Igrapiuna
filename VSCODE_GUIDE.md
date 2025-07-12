# 🚀 Guia VS Code para WebGIS

## 📋 Configuração Rápida

### **1. Abrir o Projeto no VS Code**

1. **Abra o VS Code**
2. **File → Open Folder** (ou Ctrl+K, Ctrl+O)
3. **Selecione a pasta `modulo1`**
4. **Clique em "Select Folder"**

### **2. Instalar Extensões Recomendadas**

O VS Code mostrará uma notificação para instalar extensões recomendadas. Clique em **"Install All"** ou instale manualmente:

- **Live Server** (ritwickdey.LiveServer) - **ESSENCIAL**
- **Prettier** (esbenp.prettier-vscode) - Formatação de código
- **Auto Rename Tag** (formulahendry.auto-rename-tag) - HTML
- **Path Intellisense** (christian-kohler.path-intellisense) - Autocomplete

### **3. Executar o WebGIS**

#### **Opção A: Live Server (Recomendado)**

1. **Clique com botão direito** no arquivo `index.html`
2. **Selecione "Open with Live Server"**
3. **O navegador abrirá automaticamente** em `http://localhost:8000`

#### **Opção B: Atalho Rápido**

1. **Pressione `Ctrl+Shift+P`** para abrir a paleta de comandos
2. **Digite "Live Server: Open with Live Server"**
3. **Pressione Enter**

#### **Opção C: Terminal Integrado**

1. **Pressione `Ctrl+``** para abrir o terminal
2. **Execute:**
   ```bash
   python start_webgis.py
   ```

## 🛠️ Recursos do VS Code para WebGIS

### **🔍 Navegação Inteligente**

- **Ctrl+P**: Buscar arquivos rapidamente
- **Ctrl+Shift+F**: Buscar em todo o projeto
- **F12**: Ir para definição
- **Alt+F12**: Ver definição

### **📝 Edição Avançada**

- **Ctrl+D**: Selecionar próxima ocorrência
- **Alt+Click**: Múltiplos cursores
- **Ctrl+Shift+K**: Deletar linha
- **Alt+↑/↓**: Mover linha

### **🎨 Formatação Automática**

- **Shift+Alt+F**: Formatar documento
- **Ctrl+S**: Salvar (formata automaticamente)
- **Auto-save**: Salva automaticamente a cada segundo

### **🐛 Debug Integrado**

1. **Pressione F5** para iniciar debug
2. **Selecione "Launch WebGIS"**
3. **Use breakpoints** no JavaScript
4. **Inspecione variáveis** no painel de debug

## 📁 Estrutura do Projeto no VS Code

```
modulo1/
├── 📄 index.html              # Interface principal
├── 📄 start_webgis.py         # Script Python
├── 📄 README.md               # Documentação
├── 📄 VSCODE_GUIDE.md         # Este arquivo
├── 📁 .vscode/                # Configurações do VS Code
│   ├── settings.json          # Configurações do projeto
│   ├── launch.json            # Configurações de debug
│   └── extensions.json        # Extensões recomendadas
└── 📁 data/
    └── 📁 igrapiuna/
        ├── 📄 IGRAPIUNA.geojson
        ├── 📄 AREA_IMOVEL.geojson
        ├── 📄 VEGETACAO_NATIVA.geojson
        ├── 📄 RESERVA_LEGAL.geojson
        ├── 📄 HIDROGRAFIA.geojson
        ├── 📄 AREA_CONSOLIDADA.geojson
        └── 📄 APP.geojson
```

## ⚡ Atalhos Úteis

### **Navegação**
- `Ctrl+G`: Ir para linha
- `Ctrl+P`: Buscar arquivo
- `Ctrl+Shift+P`: Paleta de comandos
- `Ctrl+B`: Toggle sidebar

### **Edição**
- `Ctrl+X/C/V`: Cortar/Copiar/Colar
- `Ctrl+Z`: Desfazer
- `Ctrl+Shift+Z`: Refazer
- `Ctrl+A`: Selecionar tudo

### **Multi-cursor**
- `Alt+Click`: Adicionar cursor
- `Ctrl+Alt+↑/↓`: Adicionar cursor acima/abaixo
- `Ctrl+D`: Selecionar próxima ocorrência

### **Debug**
- `F5`: Iniciar debug
- `F9`: Toggle breakpoint
- `F10`: Step over
- `F11`: Step into
- `Shift+F11`: Step out

## 🔧 Personalizações

### **Tema Escuro (Recomendado)**
1. **Ctrl+Shift+P**
2. **Digite "Preferences: Color Theme"**
3. **Selecione "Dark+" ou "One Dark Pro"**

### **Fonte Programação**
1. **Ctrl+Shift+P**
2. **Digite "Preferences: Font Family"**
3. **Configure: `'Fira Code', 'Consolas', 'Courier New', monospace`**

### **Ligatures (Para Fira Code)**
1. **Ctrl+Shift+P**
2. **Digite "Preferences: Font Ligatures"**
3. **Selecione "Enabled"**

## 🚀 Workflow Recomendado

### **1. Desenvolvimento**
1. **Abra o projeto** no VS Code
2. **Inicie o Live Server** (botão direito em index.html)
3. **Edite o código** - as mudanças aparecem automaticamente
4. **Use o debug** para testar funcionalidades

### **2. Debugging**
1. **Abra o DevTools** no navegador (F12)
2. **Configure breakpoints** no VS Code
3. **Use o console** para logs
4. **Inspecione elementos** no DOM

### **3. Versionamento**
1. **Instale a extensão Git** (já vem por padrão)
2. **Use o Source Control** (Ctrl+Shift+G)
3. **Commit suas mudanças** regularmente

## 🎯 Vantagens do VS Code

✅ **Live Server**: Recarrega automaticamente
✅ **IntelliSense**: Autocomplete inteligente
✅ **Debug Integrado**: Breakpoints no JavaScript
✅ **Extensões**: Muitas ferramentas úteis
✅ **Terminal Integrado**: Execute comandos sem sair
✅ **Git Integrado**: Controle de versão
✅ **Multi-language**: Suporte a HTML, CSS, JS, Python

## 🆘 Solução de Problemas

### **Live Server não funciona:**
- Verifique se a extensão está instalada
- Tente reiniciar o VS Code
- Use o terminal integrado com Python

### **Debug não conecta:**
- Verifique se o Chrome está aberto
- Use "Attach to Chrome" em vez de "Launch"

### **Extensões não aparecem:**
- Reinicie o VS Code
- Verifique se há atualizações pendentes

O VS Code é uma excelente escolha para desenvolvimento web! 🚀 
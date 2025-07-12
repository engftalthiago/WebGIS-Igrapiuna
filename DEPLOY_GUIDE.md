# 🚀 Guia de Deploy - GitHub Pages

## 📋 Passos para Publicar o WebGIS

### **1. Preparar o Repositório**

✅ **Arquivos já criados:**
- ✅ `index.html` - Interface principal
- ✅ `.github/workflows/deploy.yml` - Configuração do GitHub Actions
- ✅ `README.md` - Documentação atualizada
- ✅ `LICENSE` - Licença MIT
- ✅ `.gitignore` - Arquivos ignorados

### **2. Fazer Upload para o GitHub**

#### **Opção A: Via Git (Recomendado)**

1. **Inicialize o Git** (se ainda não fez):
   ```bash
   git init
   git add .
   git commit -m "Initial commit: WebGIS Igrapiuna"
   ```

2. **Conecte ao repositório remoto:**
   ```bash
   git remote add origin https://github.com/engftalthiago/WebGIS-Igrapiuna.git
   git branch -M main
   git push -u origin main
   ```

#### **Opção B: Upload Manual**

1. **Acesse:** https://github.com/engftalthiago/WebGIS-Igrapiuna
2. **Clique em "Add file" → "Upload files"**
3. **Arraste todos os arquivos** para o repositório
4. **Commit as mudanças**

### **3. Configurar GitHub Pages**

1. **Vá para Settings** do repositório
2. **Clique em "Pages"** no menu lateral
3. **Configure:**
   - **Source**: Deploy from a branch
   - **Branch**: `gh-pages`
   - **Folder**: `/ (root)`
4. **Clique em "Save"**

### **4. Verificar o Deploy**

1. **Aguarde alguns minutos** para o GitHub Actions processar
2. **Acesse:** https://engftalthiago.github.io/WebGIS-Igrapiuna/
3. **Verifique se tudo está funcionando**

## 🔧 Configurações Importantes

### **GitHub Actions (Automático)**

O arquivo `.github/workflows/deploy.yml` já está configurado para:
- ✅ **Deploy automático** quando você fizer push
- ✅ **Branch `gh-pages`** criada automaticamente
- ✅ **Atualização em tempo real** do site

### **Estrutura de Arquivos**

```
WebGIS-Igrapiuna/
├── index.html              # 🎯 Arquivo principal
├── data/                   # 📊 Dados GeoJSON
│   └── igrapiuna/
├── .github/workflows/      # ⚙️ Configuração do deploy
├── .vscode/               # 🔧 Configurações do VS Code
├── README.md              # 📖 Documentação
├── LICENSE                # 📄 Licença
└── .gitignore            # 🚫 Arquivos ignorados
```

## 🌐 URLs Importantes

- **🌍 WebGIS Online:** https://engftalthiago.github.io/WebGIS-Igrapiuna/
- **📊 Repositório:** https://github.com/engftalthiago/WebGIS-Igrapiuna
- **⚙️ Actions:** https://github.com/engftalthiago/WebGIS-Igrapiuna/actions

## 🚀 Como Atualizar

### **Para fazer mudanças:**

1. **Edite os arquivos** localmente
2. **Commit as mudanças:**
   ```bash
   git add .
   git commit -m "Atualização: [descrição da mudança]"
   git push origin main
   ```
3. **O GitHub Actions** fará o deploy automaticamente
4. **Aguarde 2-3 minutos** para a atualização

### **Para verificar o status:**

1. **Vá para:** https://github.com/engftalthiago/WebGIS-Igrapiuna/actions
2. **Verifique se o workflow** "Deploy to GitHub Pages" foi executado
3. **Clique no workflow** para ver os detalhes

## 🎯 Funcionalidades do WebGIS Online

✅ **3 Mapas de Fundo:**
- OpenStreetMap
- Satélite (Esri World Imagery)
- CartoDB Voyager

✅ **7 Camadas de Dados:**
- Limite Municipal (transparente)
- Área do Imóvel
- Vegetação Nativa (verde escuro)
- Reserva Legal
- Hidrografia
- Área Consolidada
- APP

✅ **Funcionalidades Avançadas:**
- Tabela de atributos completa
- Zoom automático para Igrapiuna
- Ordem de sobreposição controlada
- Status de carregamento
- Design responsivo

## 🆘 Solução de Problemas

### **Se o site não aparecer:**
1. **Verifique o Actions** - veja se houve erro no deploy
2. **Aguarde mais tempo** - pode demorar até 5 minutos
3. **Verifique a branch** - deve ser `gh-pages`

### **Se as camadas não carregarem:**
1. **Verifique o console** do navegador (F12)
2. **Confirme se os arquivos GeoJSON** estão no repositório
3. **Teste localmente** primeiro

### **Se o GitHub Actions falhar:**
1. **Vá para Actions** no repositório
2. **Clique no workflow** que falhou
3. **Verifique os logs** para identificar o erro

## 📞 Suporte

Se precisar de ajuda:
- **Issues:** https://github.com/engftalthiago/WebGIS-Igrapiuna/issues
- **Email:** [seu-email@exemplo.com]

---

🎉 **Parabéns! Seu WebGIS estará online em:** https://engftalthiago.github.io/WebGIS-Igrapiuna/ 
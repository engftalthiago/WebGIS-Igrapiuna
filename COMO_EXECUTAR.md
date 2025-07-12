# 🚀 Como Executar o WebGIS com Anaconda

## 📋 Opções Disponíveis

### **Opção 1: Jupyter Notebook (Recomendado)**

1. **Abra o Anaconda Navigator**
2. **Clique em "Launch" no Jupyter Notebook**
3. **Navegue até a pasta do projeto** (modulo1)
4. **Abra o arquivo `webgis_server.ipynb`**
5. **Execute todas as células** (Shift + Enter)
6. **O navegador abrirá automaticamente** com o WebGIS

### **Opção 2: Script Python Direto**

1. **Abra o Anaconda Navigator**
2. **Clique em "Launch" no Jupyter Notebook**
3. **Navegue até a pasta do projeto**
4. **Abra um novo notebook** e cole este código:

```python
# Executar o script diretamente
exec(open('start_webgis.py').read())
```

### **Opção 3: Terminal do Anaconda**

1. **Abra o Anaconda Navigator**
2. **Clique em "Launch" no Anaconda Prompt**
3. **Navegue até a pasta do projeto:**
   ```bash
   cd "C:\Users\CFRI03\OneDrive\Thiago_Martins\Pessoal\Cursos\F2W\modulo1"
   ```
4. **Execute o script:**
   ```bash
   python start_webgis.py
   ```

### **Opção 4: Abrir Diretamente (Mais Simples)**

1. **Abra o Windows Explorer**
2. **Navegue até a pasta do projeto**
3. **Clique duas vezes no arquivo `index.html`**
4. **O navegador abrirá com o WebGIS**

⚠️ **Nota:** Esta opção pode ter limitações de CORS, mas funciona para testes rápidos.

## 🔧 Solução de Problemas

### **Se o Jupyter não abrir:**
- Verifique se o Anaconda está instalado corretamente
- Tente reiniciar o Anaconda Navigator

### **Se a porta 8000 estiver ocupada:**
- Abra o notebook `webgis_server.ipynb`
- Mude a linha `PORT = 8000` para `PORT = 8080`
- Execute novamente

### **Se os dados não carregarem:**
- Verifique se os arquivos GeoJSON estão na pasta `data/igrapiuna/`
- Abra o console do navegador (F12) para ver erros

### **Se o navegador não abrir automaticamente:**
- Acesse manualmente: http://localhost:8000
- Ou tente: http://127.0.0.1:8000

## 📁 Estrutura de Arquivos

```
modulo1/
├── index.html              # Interface principal
├── start_webgis.py         # Script Python
├── webgis_server.ipynb     # Notebook Jupyter
├── COMO_EXECUTAR.md        # Este arquivo
├── README.md               # Documentação completa
└── data/
    └── igrapiuna/
        ├── IGRAPIUNA.geojson
        ├── AREA_IMOVEL.geojson
        ├── VEGETACAO_NATIVA.geojson
        ├── RESERVA_LEGAL.geojson
        ├── HIDROGRAFIA.geojson
        ├── AREA_CONSOLIDADA.geojson
        └── APP.geojson
```

## 🎯 Funcionalidades do WebGIS

✅ **3 Mapas de Fundo Funcionais:**
- OpenStreetMap
- Satélite (Esri World Imagery)
- CartoDB Voyager

✅ **7 Camadas de Dados:**
- Limite Municipal
- Área do Imóvel
- Vegetação Nativa
- Reserva Legal
- Hidrografia
- Área Consolidada
- APP

✅ **Interface Moderna:**
- Design responsivo
- Controles intuitivos
- Pop-ups informativos
- Coordenadas em tempo real

## 🚀 Recomendação

**Use a Opção 1 (Jupyter Notebook)** - é a mais confiável e oferece melhor controle! 
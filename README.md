# WebGIS Igrapiuna

Sistema de Informação Geográfica Web para o município de Igrapiuna, Bahia.

## 🌍 Sobre o Projeto

Este WebGIS foi desenvolvido para visualizar e analisar dados geográficos do município de Igrapiuna, incluindo limites municipais, áreas de propriedades, vegetação nativa, reserva legal, áreas consolidadas, APPs e hidrografia.

## 🚀 Acesso Público

**URL do WebGIS:** https://engftalthiago.github.io/WebGIS-Igrapiuna/

## ✨ Funcionalidades

### 🗺️ Mapas Base
- **OpenStreetMap**: Mapa topográfico padrão
- **Satélite (Esri)**: Imagens de satélite de alta resolução
- **CartoDB Voyager**: Mapa estilizado moderno

### 📊 Camadas Disponíveis
1. **Limite Municipal** - Fronteiras do município de Igrapiuna
2. **Área do Imóvel** - Delimitação de propriedades rurais
3. **Vegetação Nativa** - Cobertura vegetal nativa
4. **Reserva Legal** - Áreas de proteção legal
5. **Área Consolidada** - Áreas de uso consolidado
6. **APP** - Áreas de Preservação Permanente
7. **Hidrografia** - Rios, córregos e corpos d'água

### 🎛️ Controles Interativos
- **Sidebar Colapsável**: Controles de camadas e mapas base
- **Pop-ups Informativos**: Detalhes completos dos atributos
- **Coordenadas em Tempo Real**: Posição do cursor
- **Legenda Visual**: Cores e símbolos das camadas
- **Zoom Automático**: Ajuste automático ao carregar camadas

## 🛠️ Tecnologias Utilizadas

- **Leaflet.js**: Biblioteca de mapas interativos
- **HTML5/CSS3**: Interface responsiva
- **JavaScript ES6+**: Funcionalidades dinâmicas
- **GeoJSON**: Formato de dados geográficos
- **GitHub Pages**: Hospedagem gratuita

## 📁 Estrutura do Projeto

```
WebGIS-Igrapiuna/
├── index.html              # Arquivo principal do WebGIS
├── data/
│   └── igrapiuna/
│       ├── IGRAPIUNA.geojson          # Limite municipal
│       ├── AREA_IMOVEL.geojson        # Área do imóvel
│       ├── VEGETACAO_NATIVA.geojson   # Vegetação nativa
│       ├── RESERVA_LEGAL.geojson      # Reserva legal
│       ├── AREA_CONSOLIDADA.geojson   # Área consolidada
│       ├── APP.geojson                # Áreas de preservação
│       └── HIDROGRAFIA.geojson        # Hidrografia
├── .github/
│   └── workflows/
│       └── deploy.yml                 # GitHub Actions
├── README.md                          # Este arquivo
├── LICENSE                            # Licença MIT
└── .gitignore                        # Arquivos ignorados
```

## 🎨 Características Visuais

### Paleta de Cores
- **Limite Municipal**: Transparente com borda cinza
- **Área do Imóvel**: Marrom (#8B4513)
- **Vegetação Nativa**: Verde escuro (#228B22)
- **Reserva Legal**: Verde claro (#32CD32)
- **Área Consolidada**: Dourado (#FFD700)
- **APP**: Azul (#4169E1)
- **Hidrografia**: Azul claro (#00BFFF)

### Interface
- Design responsivo para desktop e mobile
- Sidebar com controles intuitivos
- Pop-ups com tabelas de atributos
- Legenda visual integrada
- Painel de informações em tempo real

## 🔧 Como Executar Localmente

### Opção 1: Servidor Python
```bash
# Python 3
python -m http.server 8000

# Python 2
python -m SimpleHTTPServer 8000
```

### Opção 2: Servidor Node.js
```bash
# Instalar serve globalmente
npm install -g serve

# Executar servidor
serve -p 8000
```

### Opção 3: Live Server (VS Code)
1. Instale a extensão "Live Server"
2. Clique com botão direito no `index.html`
3. Selecione "Open with Live Server"

## 📱 Responsividade

O WebGIS é totalmente responsivo e funciona em:
- ✅ Desktop (Windows, macOS, Linux)
- ✅ Tablet (iOS, Android)
- ✅ Smartphone (iOS, Android)

## 🔄 Atualizações Automáticas

O projeto utiliza GitHub Actions para deploy automático:
- Push para `main` branch
- Build automático
- Deploy para GitHub Pages
- URL atualizada automaticamente

## 📊 Dados Geográficos

### Fonte dos Dados
- Dados oficiais do município de Igrapiuna
- Formato GeoJSON otimizado
- Coordenadas em WGS84 (EPSG:4326)

### Estrutura dos Dados
Cada camada contém:
- Geometria (polígonos, linhas, pontos)
- Atributos descritivos
- Metadados de origem

## 🤝 Contribuições

Para contribuir com o projeto:

1. Faça um fork do repositório
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👨‍💻 Autor

**Thiago Martins**
- GitHub: [@engftalthiago](https://github.com/engftalthiago)
- Email: [seu-email@exemplo.com]

## 🙏 Agradecimentos

- Prefeitura Municipal de Igrapiuna
- Comunidade Leaflet.js
- GitHub Pages pela hospedagem gratuita

## 📞 Suporte

Para dúvidas ou sugestões:
- Abra uma [Issue](https://github.com/engftalthiago/WebGIS-Igrapiuna/issues)
- Entre em contato via email
- Consulte a documentação do Leaflet.js

---

**Última atualização:** Janeiro 2025
**Versão:** 1.0.0 
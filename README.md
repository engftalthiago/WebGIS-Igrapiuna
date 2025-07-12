# 🌍 WebGIS Igrapiuna

Um sistema de informação geográfica web desenvolvido com Leaflet para visualização de dados geoespaciais do município de Igrapiuna.

## 🌐 **Acesso Online**

**🌍 WebGIS Público:** [https://engftalthiago.github.io/WebGIS-Igrapiuna/](https://engftalthiago.github.io/WebGIS-Igrapiuna/)

## 🚀 Funcionalidades

### Mapas de Fundo
- **OpenStreetMap**: Mapa base padrão com informações de ruas e localidades
- **Satélite**: Imagens de satélite de alta resolução
- **CartoDB Voyager**: Mapa detalhado com informações de transporte, POIs e relevo

### Camadas de Dados
- **Limite Municipal**: Contorno do município de Igrapiuna (transparente com contorno cinza)
- **Área do Imóvel**: Delimitação das propriedades rurais
- **Vegetação Nativa**: Cobertura vegetal nativa (verde escuro)
- **Reserva Legal**: Áreas de reserva legal das propriedades
- **Hidrografia**: Rios, córregos e corpos d'água
- **Área Consolidada**: Áreas já consolidadas
- **APP**: Áreas de Preservação Permanente

## 🛠️ Como Usar

1. **Acesse o WebGIS online** no link acima
2. **Selecione o mapa de fundo** desejado no painel lateral esquerdo
3. **Ative/desative as camadas** marcando/desmarcando as caixas de seleção
4. **Clique nos elementos** do mapa para ver informações detalhadas
5. **Use o mouse** para navegar (zoom, pan) no mapa

## 📁 Estrutura de Arquivos

```
WebGIS-Igrapiuna/
├── index.html              # Interface principal do WebGIS
├── README.md               # Este arquivo
├── .github/
│   └── workflows/
│       └── deploy.yml      # Configuração do GitHub Actions
├── .vscode/                # Configurações do VS Code
│   ├── settings.json
│   ├── launch.json
│   └── extensions.json
├── data/
│   └── igrapiuna/
│       ├── IGRAPIUNA.geojson
│       ├── AREA_IMOVEL.geojson
│       ├── VEGETACAO_NATIVA.geojson
│       ├── RESERVA_LEGAL.geojson
│       ├── HIDROGRAFIA.geojson
│       ├── AREA_CONSOLIDADA.geojson
│       └── APP.geojson
└── modulo1.qgz
```

## 🎨 Características da Interface

- **Design responsivo**: Funciona em desktop e dispositivos móveis
- **Interface intuitiva**: Controles organizados e fáceis de usar
- **Legenda visual**: Cores distintas para cada tipo de camada
- **Informações em tempo real**: Coordenadas atualizadas conforme o mouse
- **Pop-ups informativos**: Detalhes dos elementos ao clicar
- **Tabela de atributos completa**: Informações detalhadas em formato tabular
- **Zoom automático**: Ajuste automático para os dados de Igrapiuna

## 🔧 Tecnologias Utilizadas

- **Leaflet 1.9.4**: Biblioteca JavaScript para mapas interativos
- **HTML5/CSS3**: Estrutura e estilização
- **JavaScript ES6+**: Lógica de funcionamento
- **GeoJSON**: Formato de dados geoespaciais
- **GitHub Pages**: Hospedagem gratuita

## 📊 Fontes dos Mapas de Fundo

- **OpenStreetMap**: © OpenStreetMap contributors
- **Satélite**: © Esri — Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP
- **CartoDB Voyager**: © CARTO

## 🌐 Requisitos

- Navegador web moderno (Chrome, Firefox, Safari, Edge)
- Conexão com internet (para carregar os mapas de fundo)

## 🚀 Como Executar Localmente

### Opção 1: Abrir Diretamente
1. **Clone o repositório:**
   ```bash
   git clone https://github.com/engftalthiago/WebGIS-Igrapiuna.git
   cd WebGIS-Igrapiuna
   ```
2. **Abra o arquivo `index.html`** no navegador

### Opção 2: Servidor Local
```bash
# Python 3
python -m http.server 8000

# Python 2
python -m SimpleHTTPServer 8000

# Node.js
npx http-server

# PHP
php -S localhost:8000
```

Depois acesse: `http://localhost:8000`

## 📝 Notas

- Os mapas de fundo são carregados de serviços externos
- Os dados GeoJSON são carregados localmente
- O sistema é responsivo e funciona em diferentes tamanhos de tela
- Todas as camadas são interativas com pop-ups informativos
- A ordem de sobreposição das camadas é controlada automaticamente

## 🔍 Funcionalidades Avançadas

- **Zoom automático**: O mapa se ajusta automaticamente aos dados
- **Controle de escala**: Barra de escala no canto inferior esquerdo
- **Navegação intuitiva**: Zoom com scroll, pan com arrastar
- **Performance otimizada**: Carregamento assíncrono das camadas
- **Status de carregamento**: Indicador visual do progresso
- **Cálculo de área/comprimento**: Informações geométricas nos pop-ups

## 🤝 Contribuição

Para contribuir com o projeto:

1. **Fork o repositório**
2. **Crie uma branch** para sua feature (`git checkout -b feature/AmazingFeature`)
3. **Commit suas mudanças** (`git commit -m 'Add some AmazingFeature'`)
4. **Push para a branch** (`git push origin feature/AmazingFeature`)
5. **Abra um Pull Request**

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👨‍💻 Autor

**Thiago Martins** - [GitHub](https://github.com/engftalthiago)

---

⭐ **Se este projeto foi útil para você, considere dar uma estrela no repositório!** 
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WebGIS Igrapiuna - Servidor Local
Script para iniciar o servidor HTTP local do WebGIS
"""

import http.server
import socketserver
import webbrowser
import os
import sys
from pathlib import Path

def main():
    # Configurações
    PORT = 8000
    DIRECTORY = Path.cwd()
    
    print("🌍 WebGIS Igrapiuna - Servidor Local")
    print("=" * 50)
    
    # Verificar se o arquivo index.html existe
    if not Path('index.html').exists():
        print("❌ ERRO: Arquivo index.html não encontrado!")
        print("💡 Certifique-se de estar no diretório correto.")
        return
    
    print(f"✅ index.html encontrado")
    print(f"📁 Diretório: {DIRECTORY}")
    print(f"🌐 Porta: {PORT}")
    
    # Mudar para o diretório do projeto
    os.chdir(DIRECTORY)
    
    # Configurar o handler HTTP com CORS
    class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
        def end_headers(self):
            # Adicionar headers CORS
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            super().end_headers()
    
    try:
        # Iniciar o servidor
        with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
            print(f"\n🚀 Servidor iniciado com sucesso!")
            print(f"🌐 URL: http://localhost:{PORT}")
            print(f"📱 Para parar: Ctrl+C")
            print("-" * 50)
            
            # Abrir o navegador automaticamente
            try:
                webbrowser.open(f"http://localhost:{PORT}")
                print("✅ Navegador aberto automaticamente")
            except:
                print("⚠️  Navegador não abriu automaticamente")
                print("💡 Acesse manualmente: http://localhost:8000")
            
            print("\n🎯 WebGIS carregado! Use os controles na sidebar.")
            print("🗺️  Mapas de fundo: OpenStreetMap, Satélite, Topográfico")
            print("📊 Camadas: Limite Municipal, Área do Imóvel, Vegetação, etc.")
            
            # Manter o servidor rodando
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n🛑 Servidor parado pelo usuário.")
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"❌ ERRO: Porta {PORT} já está em uso!")
            print("💡 Tente:")
            print(f"   - Parar outros processos na porta {PORT}")
            print(f"   - Ou mude a porta no código para 8080")
        else:
            print(f"❌ ERRO: {e}")
    except Exception as e:
        print(f"❌ ERRO inesperado: {e}")

if __name__ == "__main__":
    main() 
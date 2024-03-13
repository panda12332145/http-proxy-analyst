import requests
import os

def download_proxies(api_url, output_file):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        with open(output_file, 'w') as file:
            file.write(response.text)
        print(f"Lista de proxies baixada e salva em {output_file}")
    except requests.RequestException as e:
        print(f"Erro ao baixar a lista de proxies: {e}")

def verificar_proxy(proxy):
    try:
        response = requests.get("https://www.example.com", proxies={"http": proxy, "https": proxy}, timeout=5)
        response.raise_for_status()
        return "Funcionando"
    except requests.RequestException as e:
        return f"Falha ({type(e).__name__}: {str(e)})"

def salvar_proxys_funcionando(arquivo_saida, proxys_funcionando):
    with open(arquivo_saida, 'w') as file:
        file.write("\n".join(proxys_funcionando))
    print(f"Proxys funcionando foram salvos em {arquivo_saida}")

def testar_proxies(arquivo_proxies, arquivo_saida):
    with open(arquivo_proxies, 'r') as file:
        proxies = file.readlines()

    proxys_funcionando = []
    for proxy in proxies:
        proxy = proxy.strip()
        resultado = f"Proxy: {proxy} - Status: {verificar_proxy(proxy)}"
        print(resultado)
        if "Funcionando" in resultado:
            proxys_funcionando.append(f"Proxy: {proxy} - Status: Funcionando")

    if proxys_funcionando:
        salvar_proxys_funcionando(arquivo_saida, proxys_funcionando)

if __name__ == "__main__":
    api_url = "https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&protocol=all&timeout=15000&proxy_format=ipport&format=text"
    arquivo_proxies_temp = "proxies_temp.txt"
    arquivo_saida = input("Digite o nome do arquivo de saída para as proxies funcionando: ")

    download_proxies(api_url, arquivo_proxies_temp)
    testar_proxies(arquivo_proxies_temp, arquivo_saida)
    os.remove(arquivo_proxies_temp)

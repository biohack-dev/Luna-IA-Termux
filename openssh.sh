#!/data/data/com.termux/files/usr/bin/bash

# Verifica se o Termux está na versão 0.79 ou superior
TERMUX_VERSION=$(termux-info | grep "termux-packages" | awk '{print $2}')
if [[ "$TERMUX_VERSION" < "0.79" ]]; then
    echo "[!] Versão do Termux inferior a 0.79. Atualize com 'pkg upgrade'."
    exit 1
fi

# Atualiza os pacotes e instala o OpenSSH
echo "[*] Atualizando pacotes e instalando OpenSSH..."
pkg update -y && pkg upgrade -y
pkg install -y openssh

# Configura a senha do usuário do Termux
echo "[*] Configurando senha do usuário do Termux..."
passwd

# Configura o servidor SSH
echo "[*] Configurando o servidor SSH..."
sshd_config="/data/data/com.termux/files/usr/etc/ssh/sshd_config"
if [ -f "$sshd_config" ]; then
    # Habilita autenticação por senha (opcional, mas útil para acesso rápido)
    sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/g' "$sshd_config"
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin no/g' "$sshd_config"
    sed -i 's/#AllowAgentForwarding yes/AllowAgentForwarding yes/g' "$sshd_config"
else
    echo "[!] Arquivo de configuração do SSH não encontrado: $sshd_config"
    exit 1
fi

# Inicia o servidor SSH
echo "[*] Iniciando o servidor SSH..."
sshd

# Obtém o IP e a porta (padrão: 8022)
IP=$(ifconfig | grep "inet" | grep -v "127.0.0.1" | awk '{print $2}' | head -n 1)
PORT=8022

echo -e "\n[+] OpenSSH configurado com sucesso!"
echo -e "[+] Conecte-se usando:"
echo -e "    ssh $(whoami)@$IP -p $PORT"
echo -e "\n[!] Certifique-se de que o Termux está acessível na rede (WiFi/4G)."

exit 0

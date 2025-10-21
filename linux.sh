#!/data/data/com.termux/files/usr/bin/bash
# Instalar Ubuntu 20.04 (32-bit armhf) no Termux Legacy (Android 6)

set -e

echo "=== Atualizando pacotes do Termux ==="
#apt update --allow-insecure-repositories
#apt upgrade -y --allow-unauthenticated

echo "=== Instalando dependências ==="
#apt install proot wget tar -y --allow-unauthenticated

echo "=== Baixando rootfs do Ubuntu 20.04 (armhf 32-bit) ==="
cd $HOME
UBUNTU_TAR="ubuntu.tar.gz"
wget https://partner-images.canonical.com/core/bionic/current/ubuntu-bionic-core-cloudimg-armhf-root.tar.gz -O ubuntu.tar.gz

echo "=== Criando diretório do Ubuntu ==="
mkdir -p $HOME/ubuntu-fs
cd $HOME/ubuntu-fs

echo "=== Extraindo rootfs... Isso pode demorar ==="
proot --link2symlink tar -xzf $HOME/ubuntu.tar.gz --exclude='dev' --exclude='proc' --exclude='sys'

echo "=== Criando script de inicialização start-ubuntu.sh ==="
cat > $HOME/start-ubuntu.sh <<'EOF'
#!/data/data/com.termux/files/usr/bin/bash
cd ~/ubuntu-fs
unset LD_PRELOAD
exec proot \
  --link2symlink \
  -0 \
  -r ~/ubuntu-fs \
  -b /dev \
  -b /proc \
  -b /sys \
  -b /sdcard \
  -b /data/data/com.termux/files/home \
  /usr/bin/env -i \
  HOME=/root \
  PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
  TERM=$TERM \
  LANG=C.UTF-8 \
  /bin/bash --login
EOF

chmod +x $HOME/start-ubuntu.sh

echo "=== Limpeza ==="
rm $HOME/ubuntu.tar.gz

echo "=== Instalação concluída! ==="
echo "Agora rode: ./start-ubuntu.sh"

#!/bin/bash
echo "Configurando sources.list no Termux (forçando modo inseguro)..."

cat > $PREFIX/etc/apt/sources.list <<EOF
deb [allow-insecure=yes] http://192.168.43.56/termux-packages stable main
deb [allow-insecure=yes] http://192.168.43.56/termux-root-packages-21 root stable
deb [allow-insecure=yes] http://192.168.43.56/unstable-packages-21 unstable main
deb [allow-insecure=yes] http://192.168.43.56/science-packages-21 science stable
EOF

echo "Configurando APT para nunca exigir GPG..."
mkdir -p $PREFIX/etc/apt/apt.conf.d
cat > $PREFIX/etc/apt/apt.conf.d/99nogpgcheck <<EOF
APT::Get::AllowUnauthenticated "true";
Acquire::AllowInsecureRepositories "true";
Acquire::AllowDowngradeToInsecureRepositories "true";
EOF

echo "Ignorando SSL no wget/curl..."
echo "check_certificate = off" >> $HOME/.wgetrc
echo "insecure" >> $HOME/.curlrc

echo "Atualizando pacotes (sem checagem de assinatura)..."
apt update --allow-insecure-repositories
apt upgrade -y --allow-unauthenticated

#!/bin/bash

# Создаем временную директорию для сбора данных
TEMP_DIR=$(mktemp -d)
RESULTS_DIR="$TEMP_DIR/results"
mkdir -p "$RESULTS_DIR"

echo "Начинаем сбор данных..."

# Этап 1: Копирование результатов
echo "Этап 1/9: Копирование ~/results..."
if [ -d "$HOME/results" ]; then
    cp -r "$HOME/results/"* "$RESULTS_DIR/" 2>/dev/null
fi

# Этап 2: Копирование /etc/hosts
echo "Этап 2/9: Копирование /etc/hosts..."
cp /etc/hosts "$TEMP_DIR/hosts.txt"

# Этап 3: Копирование файлов sudoers.d
echo "Этап 3/9: Копирование файлов sudoers.d..."
if [ -f /etc/sudoers.d/test2 ]; then
    sudo cp /etc/sudoers.d/test2 "$TEMP_DIR/"
fi
if [ -f /etc/sudoers.d/test_users ]; then
    sudo cp /etc/sudoers.d/test_users "$TEMP_DIR/"
fi

# Этап 4: Проверка пользователей
echo "Этап 4/9: Проверка пользователей..."
{
    echo "=== Проверка пользователя test ==="
    echo "Ожидаемый пароль: P@ssw0rd1"
    echo "P@ssw0rd1" | su test -c "echo 'Успешный вход'" 2>/dev/null && echo "✅ Пароль верный" || echo "❌ Пароль неверный"
    echo ""
    echo "Группы безопасности:"
    groups test 2>/dev/null || echo "Пользователь test не найден"
    echo ""
    echo "=== Проверка пользователя test2 ==="
    echo "Ожидаемый пароль: P@ssw0rd"
    echo "P@ssw0rd" | su test2 -c "echo 'Успешный вход'" 2>/dev/null && echo "✅ Пароль верный" || echo "❌ Пароль неверный"
    echo ""
    echo "Группы безопасности:"
    groups test2 2>/dev/null || echo "Пользователь test2 не найден"
} > "$TEMP_DIR/users.txt"

# Этап 5: Создание whoami.txt
echo "Этап 5/9: Сбор информации о сервисах..."
{
    echo "=== Статус whoami.service ==="
    sudo systemctl status whoami.service 2>/dev/null || echo "Сервис whoami.service не найден"
    echo ""
    echo "=== Статус whoami.timer ==="
    sudo systemctl status whoami.timer 2>/dev/null || echo "Таймер whoami.timer не найден"
} > "$TEMP_DIR/whoami.txt"

# Этап 6: Копирование SSH конфигураций и проверка ключей
echo "Этап 6/9: Копирование SSH конфигураций и проверка ключей..."
if [ -f /etc/ssh/ssh_config ]; then
    cp /etc/ssh/ssh_config "$TEMP_DIR/ssh_config.txt"
fi
if [ -f "$HOME/.ssh/config" ]; then
    cp "$HOME/.ssh/config" "$TEMP_DIR/config.txt"
fi

# Проверка наличия SSH-ключей (записываем в keygen.txt)
{
    echo "=== Проверка наличия SSH-ключей ==="
    PUB_KEY=$(find "$HOME/.ssh" -maxdepth 1 -name "*.pub" 2>/dev/null | head -n 1)
    if [ -n "$PUB_KEY" ]; then
        echo "✅ Найден публичный ключ: $PUB_KEY"
        PRIV_KEY="${PUB_KEY%.pub}"
        if [ -f "$PRIV_KEY" ]; then
            echo "✅ Приватный ключ найден: $PRIV_KEY"
        else
            echo "❌ Приватный ключ не найден для $PUB_KEY"
        fi
    else
        echo "❌ Публичный ключ не найден в ~/.ssh/"
    fi
} > "$TEMP_DIR/keygen.txt"

# Этап 7: Сбор информации с srv01
echo "Этап 7/9: Сбор информации с srv01..."
{
    echo "=== Проверка подключения к srv01 ==="
    ssh -o ConnectTimeout=5 -o StrictHostKeyChecking=no srv01 "echo '✅ Подключение ОК'" 2>/dev/null && echo "✅ Успешное подключение (ключ + порт 2222)" || echo "❌ Ошибка подключения к srv01"
    echo ""
    echo "=== Проверка наличия authorized_keys на srv01 ==="
    ssh -o ConnectTimeout=5 -o StrictHostKeyChecking=no -p 2222 srv01 "test -f /home/administrator/.ssh/authorized_keys && echo '✅ authorized_keys найден' || echo '❌ authorized_keys не найден'" 2>/dev/null || echo "❌ Не удалось проверить ключи на srv01"
    echo ""
    echo "=== Статус UFW на srv01 ==="
    ssh -o ConnectTimeout=5 -o StrictHostKeyChecking=no srv01 "sudo ufw status" 2>/dev/null || echo "Не удалось получить статус UFW на srv01"
} > "$TEMP_DIR/ssh_srv01.txt"

# Этап 8: Сбор информации с srv02
echo "Этап 8/9: Сбор информации с srv02..."
{
    echo "=== Проверка подключения к srv02 ==="
    ssh -o ConnectTimeout=5 -o StrictHostKeyChecking=no srv02 "echo '✅ Подключение ОК'" 2>/dev/null && echo "✅ Успешное подключение (ключ + root)" || echo "❌ Ошибка подключения к srv02"
    echo ""
    echo "=== Проверка наличия authorized_keys на srv02 ==="
    ssh -o ConnectTimeout=5 -o StrictHostKeyChecking=no srv02 "test -f /root/.ssh/authorized_keys && echo '✅ authorized_keys найден' || echo '❌ authorized_keys не найден'" 2>/dev/null || echo "❌ Не удалось проверить ключи на srv02"
    echo ""
    echo "=== Статус UFW на srv02 ==="
    ssh -o ConnectTimeout=5 -o StrictHostKeyChecking=no srv02 "sudo ufw status" 2>/dev/null || echo "Не удалось получить статус UFW на srv02"
} > "$TEMP_DIR/ssh_srv02.txt"

# Этап 9: Проверка запрета administrator на srv02
echo "Этап 9/9: Проверка запрета administrator на srv02..."
{
    echo "=== Проверка запрета для administrator ==="
    ssh -o ConnectTimeout=5 -o StrictHostKeyChecking=no -l administrator srv02 "exit" 2>/dev/null && echo "❌ ОШИБКА: Подключение administrator РАЗРЕШЕНО (должно быть запрещено)" || echo "✅ Подключение administrator ЗАПРЕЩЕНО (корректно)"
} > "$TEMP_DIR/ssh_srv02_administrator.txt"

# Этап 10: Создание архива
echo "Этап 10/10: Создание архива results.zip..."
cd "$TEMP_DIR" || exit 1
zip -r "$HOME/results.zip" . >/dev/null 2>&1

# Очистка
cd "$HOME" || exit 1
rm -rf "$TEMP_DIR"

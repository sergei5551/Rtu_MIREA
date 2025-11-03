
## Python

**Установка:**
```bash
# Ubuntu/Debian
sudo apt install python3 python3-pip

# Windows (через сайт python.org)
```

**Запуск:**
```bash
python3 файл.py
```

**С аргументами:**
```bash
python3 файл.py аргумент1 аргумент2
```

**Установка библиотек:**
```bash
pip3 install имя_библиотеки
```

---

## C

**Установка компилятора:**
```bash
# Ubuntu/Debian
sudo apt install gcc

# Windows: MinGW или MSYS2
```

**Компиляция и запуск:**
```bash
gcc файл.c -o программа
./программа
```

**С флагами компиляции:**
```bash
gcc -Wall -g файл.c -o программа
./программа
```

---

## C++

**Установка компилятора:**
```bash
# Ubuntu/Debian
sudo apt install g++

# Windows: MinGW или MSYS2
```

**Компиляция и запуск:**
```bash
g++ файл.cpp -o программа
./программа
```

**С C++11/14/17 стандартом:**
```bash
g++ -std=c++17 файл.cpp -o программа
./программа
```

---

## Java

**Установка:**
```bash
# Ubuntu/Debian
sudo apt install default-jdk

# Windows: с oracle.com/java
```

**Компиляция и запуск:**
```bash
javac Файл.java
java Файл
```

**Если есть пакеты:**
```bash
javac com/папка/Файл.java
java com.папка.Файл
```

**С аргументами командной строки:**
```bash
java Файл аргумент1 аргумент2
```

---

## Kotlin

**Установка:**
```bash
# Ubuntu/Debian
sudo apt install kotlin

# Или через SDKMAN:
curl -s "https://get.sdkman.io" | bash
sdk install kotlin
```

**Компиляция и запуск:**
```bash
kotlinc файл.kt -include-runtime -d программа.jar
java -jar программа.jar
```

**Быстрый запуск (как скрипт):**
```bash
kotlinc -script файл.kts
```

**С аргументами:**
```bash
java -jar программа.jar аргумент1 аргумент2
```

---

## Пример для каждого языка:

**Python:**
```bash
echo 'print("Hello Python!")' > test.py
python3 test.py
```

**C:**
```bash
echo '#include <stdio.h>\nint main() { printf("Hello C!\\n"); return 0; }' > test.c
gcc test.c -o test && ./test
```

**C++:**
```bash
echo '#include <iostream>\nint main() { std::cout << "Hello C++!\\n"; return 0; }' > test.cpp
g++ test.cpp -o test && ./test
```

**Java:**
```bash
echo 'public class Test { public static void main(String[] args) { System.out.println("Hello Java!"); } }' > Test.java
javac Test.java && java Test
```

**Kotlin:**
```bash
echo 'fun main() { println("Hello Kotlin!") }' > test.kt
kotlinc main.kt -include-runtime -d word.jar && java -jar work.jar
```

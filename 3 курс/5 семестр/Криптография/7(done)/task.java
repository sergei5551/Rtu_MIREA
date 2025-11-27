import java.io.*;
import java.util.Scanner;
import java.math.BigInteger;
import java.util.Random;

public class task {
  private static BigInteger savedP;
  private static BigInteger savedG;
  private static BigInteger savedX0;

  public static void main(String[] args) {
    try {
      int choice = -1;
      psp psp1 = new psp();
      Scanner scanner = new Scanner(System.in);

      while (choice != 0) {
        System.out.println("""
            Выберите действие:
            1) Зашифровать файл
            2) Расшифровать файл
            0) Выход
            """.trim());
        System.out.print("Ввод: ");
        choice = scanner.nextInt();
        scanner.nextLine();

        switch (choice) {
          case 1 -> encryptFile(psp1, scanner);
          case 2 -> decryptFile(psp1, scanner);
          default -> choice = 0;
        }
      }
      scanner.close();

    } catch (Exception e) {
      System.out.println("Ошибка: " + e.getMessage());
    }
  }

  public static void encryptFile(psp psp1, Scanner scanner) {
    try {
      System.out.print("Введите текст для шифрования: ");
      String text = scanner.nextLine();
      char[] line = text.toCharArray();

      String gammaStr = psp1.geretatePsp(line.length * 8);
      char[] gamma = gammaStr.toCharArray();

      savedP = psp1.getP();
      savedG = psp1.getG();
      savedX0 = psp1.getX0();

      System.out.println("Исходный текст: " + text);
      System.out.println("Длина: " + line.length + " символов (" + (line.length * 8) + " бит)");

      StringBuilder encrypted = new StringBuilder();
      int gammaIndex = 0;

      for (int i = 0; i < line.length; i++) {
        int charCode = line[i];
        int encryptedChar = 0;

        for (int bit = 7; bit >= 0; bit--) {
          int textBit = (charCode >> bit) & 1;
          int gammaBit = gamma[gammaIndex] - '0';
          int encryptedBit = textBit ^ gammaBit;

          encryptedChar = (encryptedChar << 1) | encryptedBit;
          gammaIndex++;
        }
        encrypted.append((char) encryptedChar);
      }

      try (PrintWriter writer = new PrintWriter("./encrypted.txt")) {
        writer.print(encrypted.toString());
      }

      System.out.println("Зашифрованный текст сохранен в encrypted.txt");
      System.out.println("Параметры генератора для расшифровки:");
      System.out.println("p = " + savedP);
      System.out.println("g = " + savedG);
      System.out.println("x0 = " + savedX0);
      System.out.println("Первые 16 бит гаммы: " + gammaStr.substring(0, 16));

    } catch (FileNotFoundException e) {
      System.out.println("Ошибка записи файла!");
    }
  }

  public static void decryptFile(psp psp1, Scanner scanner) {
    try {
      FileInputStream input = new FileInputStream("./encrypted.txt");
      Scanner fileScanner = new Scanner(input);

      if (fileScanner.hasNextLine()) {
        String encryptedText = fileScanner.nextLine();

        System.out.println("Введите параметры генератора:");
        System.out.print("p = ");
        BigInteger p = new BigInteger(scanner.nextLine());
        System.out.print("g = ");
        BigInteger g = new BigInteger(scanner.nextLine());
        System.out.print("x0 = ");
        BigInteger x0 = new BigInteger(scanner.nextLine());

        psp1.setParameters(p, g, x0);

        char[] line = encryptedText.toCharArray();
        String gammaStr = psp1.geretatePsp(line.length * 8);

        System.out.println("Зашифрованный текст: " + encryptedText);
        System.out.println("Длина: " + line.length + " символов (" + (line.length * 8) + " бит)");

        StringBuilder decrypted = new StringBuilder();
        int gammaIndex = 0;

        for (int i = 0; i < line.length; i++) {
          int charCode = line[i];
          int decryptedChar = 0;

          for (int bit = 7; bit >= 0; bit--) {
            int encryptedBit = (charCode >> bit) & 1;
            int gammaBit = gammaStr.charAt(gammaIndex) - '0';
            int textBit = encryptedBit ^ gammaBit;

            decryptedChar = (decryptedChar << 1) | textBit;
            gammaIndex++;
          }
          decrypted.append((char) decryptedChar);
        }

        System.out.println("Расшифрованный текст: " + decrypted.toString());

        try (PrintWriter writer = new PrintWriter("./decrypted.txt")) {
          writer.print(decrypted.toString());
        }
        System.out.println("Расшифрованный текст сохранен в decrypted.txt");
      }

      fileScanner.close();

    } catch (FileNotFoundException e) {
      System.out.println("Файл encrypted.txt не найден! Сначала зашифруйте текст.");
    }
  }
}

class psp {
  private BigInteger p;
  private BigInteger g;
  private BigInteger x0;

  public void setParameters(BigInteger p, BigInteger g, BigInteger x0) {
    this.p = p;
    this.g = g;
    this.x0 = x0;
  }

  public BigInteger getP() {
    return p;
  }

  public BigInteger getG() {
    return g;
  }

  public BigInteger getX0() {
    return x0;
  }

  public BigInteger modpow(BigInteger base, BigInteger exponent, BigInteger modulus) {
    return base.modPow(exponent, modulus);
  }

  public String geretatePsp(int len) {
    if (p == null || g == null || x0 == null) {
      Random rand = new Random();
      p = new BigInteger("2305843009213693951");
      g = new BigInteger("1125899906842597");
      x0 = new BigInteger(50 + rand.nextInt(50), rand);
    }

    StringBuilder str = new StringBuilder();
    BigInteger[] x = new BigInteger[len];
    x[0] = x0;

    BigInteger threshold = p.subtract(BigInteger.ONE).divide(BigInteger.valueOf(2));

    for (int i = 0; i < len; i++) {
      if (i > 0) {
        x[i] = modpow(g, x[i - 1], p);
      }
      int bit = (x[i].compareTo(threshold) < 0 ? 1 : 0);
      str.append(bit);
    }
    return str.toString();
  }
}

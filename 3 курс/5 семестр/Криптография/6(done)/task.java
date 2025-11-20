import java.math.BigInteger;
import java.util.Random;
import java.util.Map;
import java.util.HashMap;

public class task {

  static BigInteger modpow(BigInteger base, BigInteger exponent, BigInteger modulus) {
    return base.modPow(exponent, modulus);
  }

  public static void main(String[] args) {
    StringBuilder str = new StringBuilder();
    Random rand = new Random();

    BigInteger p = new BigInteger("2305843009213693951"); // 2**61 - 1
    BigInteger g = new BigInteger("1125899906842597"); // ~2**60

    // Начальное значение
    BigInteger x0 = new BigInteger(50 + rand.nextInt(50), rand);

    System.out.println("Параметры:");
    System.out.println("p = " + p);
    System.out.println("g = " + g);
    System.out.println("x[0] = " + x0);

    BigInteger[] x = new BigInteger[10_000];
    x[0] = x0;

    BigInteger threshold = p.subtract(BigInteger.ONE).divide(BigInteger.valueOf(2));

    // Генерация последовательности
    for (int i = 0; i < x.length; i++) {
      if (i > 0) {
        x[i] = modpow(g, x[i - 1], p);
      }
      int bit = (x[i].compareTo(threshold) < 0 ? 1 : 0);
      str.append(bit);

    }

    System.out.println("\nПервые 200 битов: " + str.substring(0, 200));
    System.out.print("1 правило Голомба ->\n");
    check_zeros_and_ones(str);
    System.out.print("2 правило Голомба ->\n");
    generator(str);
    System.out.print("\n---------------\n3 правило Голомба->\n\n");
    autocorelation(str, x[0].intValue());
  }

  static void check_zeros_and_ones(StringBuilder sequence) {
    int zeros = 0;
    int ones = 0;
    for (int i = 0; i < sequence.length(); i++) {
      char c = sequence.charAt(i);
      if (c == '0')
        zeros++;
      else if (c == '1')
        ones++;
    }
    System.out.printf("Нулей: %d, Единиц: %d (%.1f%% / %.1f%%)%n",
        zeros, ones,
        zeros * 100.0 / sequence.length(),
        ones * 100.0 / sequence.length());
  }

  static void generator(StringBuilder sequence) {
    Map<String, Integer> ngrams = new HashMap<>();

    for (int n = 2; n <= 10; n++) {
      System.out.println("\n===" + n + "-граммы (" + (sequence.length() - n + 1) + " штук) ===");

      // Очищаем словарь перед анализом новой n-граммы
      ngrams.clear();

      // Находим все n-граммы
      for (int i = 0; i <= sequence.length() - n; i++) {
        String ngram = sequence.substring(i, i + n);
        ngrams.put(ngram, ngrams.getOrDefault(ngram, 0) + 1);
      }

      // Выводим результаты
      int totalNGrams = sequence.length() - n + 1;
      System.out.println("Всего уникальных " + n + "-грамм: " + ngrams.size());

      for (Map.Entry<String, Integer> entry : ngrams.entrySet()) {
        double frequency = (double) entry.getValue() / totalNGrams * 100;
        System.out.printf("%s: %d раз (%.2f%%)%n",
            entry.getKey(), entry.getValue(), frequency);
      }
    }
  }

  static void autocorelation(StringBuilder sequence, int period) {
    for (int shift = 1; shift < 100; shift++) {
      int matches = countMatches(sequence, shift);
      System.out.printf("Сдвиг %d: совпадений = %d, shift - %s \n", shift, matches,
          shift % period == 0 ? "Кратно" : "Некратно");
    }
  }

  static int countMatches(StringBuilder seq, int shift) {
    int matches = 0;
    for (int i = 0; i < seq.length() - shift; i++) {
      if (seq.charAt(i) == seq.charAt(i + shift)) {
        matches++;
      }
    }
    return matches;
  }
}

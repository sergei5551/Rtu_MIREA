import java.util.Scanner;

class program {
  public static void main(String[] args) {
    Calculator calc = new Calculator();
    calc.sum(5, 4, 2, 5);
  }
}

class Calculator {
  Calculator() {
    System.out.print("Создал объект");
  }

  void sum(int... nums) {
    int sum = 0;
    for (int num : nums)
      sum += num;
    System.out.println(sum);
  }

}

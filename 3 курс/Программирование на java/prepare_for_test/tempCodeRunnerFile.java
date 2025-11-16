import java.util.Scanner;
import java.util.Arrays;
class Main {
  public static void main(String[] args) {
    Solution task = new Solution();
    Scanner input = new Scanner(System.in);
    int t = input.nextInt();
    for(;t > 0; t--){
      int n = input.nextInt();
      System.out.println(task.task2(n, input));
    }
    input.close();
  }
}

class Solution {
    public String task2(int n, Scanner input) {
      int[] a = new int[n];
      for(int i = 0; i < n; i++){
        a[i] = input.nextInt();
      }
      Arrays.sort(a);
      int glasses = 0;
      for(int i = 0; i < a.length; i++){
        glasses += (i+1) - a[i];
      }
      return (glasses % 2 == 0) ? "Second" : "First";
  }
}

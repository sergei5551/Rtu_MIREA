import java.util.*;

public class Main {
    static final int MOD = 1000000007;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        
        long[][] dp = new long[n+1][n+1];
        dp[0][0] = 1;
        
        for (int num = 1; num <= n; num++) {
            for (int sum = 0; sum <= n; sum++) {
                dp[sum][num] = dp[sum][num-1];
                
                for (int cnt = 1; cnt * num <= sum; cnt++) {
                    long colorWays = nCr(cnt + k - 1, k - 1);
                    dp[sum][num] = (dp[sum][num] + dp[sum - cnt * num][num-1] * colorWays % MOD) % MOD;
                }
            }
        }
        
        System.out.println(dp[n][n]);
    }
    
    static long nCr(int n, int r) {
        if (r < 0 || r > n) return 0;
        if (r == 0 || r == n) return 1;
        r = Math.min(r, n - r);
        long res = 1;
        for (int i = 1; i <= r; i++) {
            res = res * (n - r + i) / i;
        }
        return res % MOD;
    }
}
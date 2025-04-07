class Solution {
    public long mostPoints(int[][] questions) {
        int n = questions.length;
        long[] dp = new long[n + 1]; // Extra space to avoid bounds checking

        for (int i = n - 1; i >= 0; i--) {
            int points = questions[i][0];
            int skip = questions[i][1];

            // Option 1: Solve this question
            int next = i + skip + 1;
            long solve = points + (next < n ? dp[next] : 0);

            // Option 2: Skip this question
            long notSolve = dp[i + 1];

            // Take max of both options
            dp[i] = Math.max(solve, notSolve);
        }

        return dp[0];
    }
}

fun solution(s: List<Int>): Boolean =
1.until(s.size).count{ s[it] <= s[it - 1] } < 2
&& 2.until(s.size).count{s[it] <= s[it - 2]} < 2

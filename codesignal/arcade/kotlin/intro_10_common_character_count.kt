fun solution(s1: String, s2: String): Int {
    return s1.toSet().map{ c -> minOf(s1.count{ it == c }, s2.count{ it == c }) }.sum()
}

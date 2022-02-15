fun solution(n: Int): Boolean {
    val s: String = n.toString()
    val m: Int = s.length / 2
    return s.take(m).sumBy{ it.toInt() } == s.takeLast(m).sumBy{ it.toInt() }
}

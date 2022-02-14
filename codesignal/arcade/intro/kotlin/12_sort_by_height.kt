fun solution(a: List<Int>): List<Int> {
    val b = a.filter{ it != -1 }.sorted().listIterator()
    return (a.map{ if (it == -1) -1 else b.next() })
}

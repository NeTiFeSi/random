fun solution(m: List<List<Int>>): Int {
    return m[0].indices.map{c -> m.indices.map{m[it][c]}.takeWhile{it != 0}.sum()}.sum()
}

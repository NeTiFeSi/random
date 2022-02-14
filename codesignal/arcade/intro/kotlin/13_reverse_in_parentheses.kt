fun solution(inputString: String): String {
    var os : String = inputString
    while (os.contains('(')) {
        val i = os.indexOfLast{ it == '(' }
        val j = os.indexOf(')', i)
        val revsub = os.slice(i.inc()..j.dec()).reversed()
        os = os.replaceRange(i, j.inc(), revsub)
    }
    return os
}

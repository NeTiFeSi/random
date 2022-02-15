fun solution(strings: List<String>): List<String> {
    return strings.filter{ it.length == strings.maxByOrNull { it.length }?.length }
}

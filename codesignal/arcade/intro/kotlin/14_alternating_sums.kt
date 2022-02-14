fun solution(a: List<Int>): List<Int> {
    	return a.indices.partition{ it % 2 == 0 }
                .toList().map{ it.sumOf{ a[it] } }
}

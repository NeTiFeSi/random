fun solution(a: List<Int>): Int = a.zipWithNext(Int::times).maxOrNull()!!

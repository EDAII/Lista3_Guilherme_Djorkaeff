/*
    Djorkaeff Alexandre Vilela Pereira - 16/0026822
    Guilherme Siqueira Brandão - 16/0007763
 */

import UIKit

func generateData(tam: Int) -> [Int] {
    var numbers = [Int]()
    for _ in 0..<tam {
        let ran:Int = Int(arc4random_uniform(10000))
        numbers.append(ran)
    }
    return numbers
}

func heapSort(_ array: [Int]) -> [Int] {
    var vet = array
    
    let n = vet.count
    
    var i = n
    while(i > -1) {
        vet = heapfy(vet, n: n, i: i)
        i -= 1
    }
    
    i = n-1
    while(i > 0) {
        vet.swapAt(i, 0)
        vet = heapfy(vet, n: i, i: 0)
        i -= 1
    }
    
    return vet
}

func heapfy(_ array: [Int], n: Int, i: Int) -> [Int] {
    var vet = array
    
    var greater = i
    var left = 2 * i + 1
    var right = 2 * i + 2

    if left < n && vet[i] < vet[left] {
        greater = left
    }
    
    if right < n && vet[greater] < vet[right] {
        greater = right
    }
    
    if greater != i {
        vet.swapAt(i, greater)
        vet = heapfy(vet, n: n, i: greater)
    }
    
    return vet
}

func shellSort(_ array: [Int]) -> [Int] {
    var vet = array
    
    var h = vet.count/2
    
    while h > 0 {
        var i = h
        while i < vet.count {
            let aux = vet[i]
            var swap = false
            var j = i - h
            while j >= 0 && vet[j] > aux {
                vet[j+h] = vet[j]
                swap = true
                j -= h
            }
            if swap {
                vet[j+h] = aux
            }
            i += 1
        }
        h = h/2
    }
    
    return vet
}

//print(shellSort(generateData(tam: 1000)))
//print(heapSort(generateData(tam: 1000)))

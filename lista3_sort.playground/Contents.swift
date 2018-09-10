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

print(shellSort(generateData(tam: 1000)))

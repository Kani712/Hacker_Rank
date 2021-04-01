import Foundation



guard let n = Int((readLine()?.trimmingCharacters(in: .whitespacesAndNewlines))!)
else { fatalError("Bad input") }

for i in 1 ... 10 {
    var result: Int
    result = n * i
    print("\(n) x \(i) = \(result)");
}
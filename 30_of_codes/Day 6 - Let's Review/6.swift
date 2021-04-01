import Foundation
import Darwin

let numStrings = Int(readLine()!)!

func printEvenAndOdd(string: String) {
    // This prints inputString to stderr for debugging:
    fputs("string: " + string + "\n", stderr)
	
    // Print the even-indexed characters
    // Write your code here
    let strArray = Array(string)
    var even = ""
    for i in 0..<strArray.count{
        if i % 2 == 0{
            even += String(strArray[i])
        }
    
    }
    print(even, terminator: "")
    // Print a space
    print(" ", terminator: "")
	
    // Print the odd-indexed characters
    // Write your code here
    var odd = ""
    for i in 0..<strArray.count{
        if i % 2 == 1{
            odd += String(strArray[i])
        }
    
    }
    print(odd, terminator: "")
    // Print a newline
    print()
}

for _ in 1...numStrings {
    let inputString = readLine()!
    printEvenAndOdd(string: inputString)
}

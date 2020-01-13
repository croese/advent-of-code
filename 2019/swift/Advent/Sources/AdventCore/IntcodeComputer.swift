//
//  IntcodeComputer.swift
//  Advent
//
//  Created by Christian Roese on 1/13/20.
//

import Foundation

public class IntcodeComputer: Solver {
    enum Error: Swift.Error {
        case invalidOpcode(opcode: Int, address: Int)
    }
    
    private let instructions: [Int]
    
    public init(instructions: [Int]) {
        self.instructions = instructions
    }
    
    public convenience init(text: String) {
        self.init(instructions: text.split(separator: ",").map({ Int(String($0)) ?? 0 }))
    }
    
    public func run(startingMemory: [Int:Int]) throws -> Int {
        var program = self.instructions
        
        startingMemory.forEach { (address, value) in
            program[address] = value
        }
        
        for pos in stride(from: 0, to: instructions.count, by: 4) {
            let opcode = program[pos]
            if opcode == 99 {
                break
            }
            
            let leftInput = program[program[pos+1]]
            let rightInput = program[program[pos+2]]
            let outputAddress = program[pos+3]
            
            switch opcode {
            case 1: program[outputAddress] = leftInput + rightInput
            case 2: program[outputAddress] = leftInput * rightInput
            default: throw Error.invalidOpcode(opcode: opcode, address: pos)
            }
        }
        
        return program[0]
    }
    
    public func solveA() -> String {
        do {
            let result = try run(startingMemory: [
                1: 12,
                2: 2
            ])
            return String(result)
        } catch Error.invalidOpcode(let opcode, let address) {
            print("Invalid opcode '\(opcode)' at \(address)")
        } catch {
            print("Error: \(error)")
        }
        
        return ""
    }
    
    public func solveB() -> String {
        for noun in 0...99 {
            for verb in 0...99 {
                do {
                    let result = try run(startingMemory: [
                        1: noun,
                        2: verb
                    ])
                    
                    if result == 19690720 {
                        return String(100 * noun + verb)
                    }
                    
                } catch Error.invalidOpcode(let opcode, let address) {
                    print("Invalid opcode '\(opcode)' at \(address)")
                } catch {
                    print("Error: \(error)")
                }
            }
        }
        
        return "not found!"
    }
}

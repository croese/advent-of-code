//
//  FuelCalculator.swift
//  Advent
//
//  Created by Christian Roese on 1/13/20.
//

import Foundation

public class FuelCalculator: Solver {
    private let masses: [Int]
    
    public init(masses: [Int]) {
        self.masses = masses
    }
    
    public convenience init(text: String) {
        self.init(masses: text.split(separator: "\n").map({ Int(String($0)) ?? 0 }))
    }
    
    public func fuelNeeded(for mass: Int) -> Int {
        return Int(Double(mass) / 3.0) - 2
    }
    
    public func solveA() -> String {
        return String(masses.map({ fuelNeeded(for: $0) }).reduce(0, { $0 + $1 }))
    }
    
    public func solveB() -> String {
        return String(masses.map({
            var total = fuelNeeded(for: $0)
            var weight = fuelNeeded(for: total)
            while weight > 0 {
                total += weight
                weight = fuelNeeded(for: weight)
            }
            return total
        }).reduce(0, { $0 + $1 }))
    }
}

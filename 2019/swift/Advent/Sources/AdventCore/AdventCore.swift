import Foundation
import Files

public final class App {
    private let arguments: [String]
    private var solvers = [Int:Solver]()
    
    public init(arguments: [String] = CommandLine.arguments) {
        self.arguments = arguments
    }
    
    public func run() throws {
        guard arguments.count > 1 else {
            throw Error.missingExerciseNumber
        }
        
        let input = arguments[1]
        if let number = Int(input) {
            print("exercise #\(number) part A: \(solvers[number]?.solveA() ?? "")")
            print("exercise #\(number) part B: \(solvers[number]?.solveB() ?? "")")
        } else {
            throw Error.invalidExerciseNumber(input: input)
        }
    }
    
    public func addSolver(day: Int, solver: Solver) {
        solvers[day] = solver
    }
}

public extension App {
    enum Error: Swift.Error {
        case missingExerciseNumber
        case invalidExerciseNumber(input: String)
    }
}

import AdventCore
import Files

let dataFolder = try! Folder.current.subfolder(at: "data")

let app = App()

app.addSolver(day: 1,
              solver: FuelCalculator(text: (try? dataFolder.file(at: "1/input").readAsString()) ?? ""))
app.addSolver(day: 2,
              solver: IntcodeComputer(text: (try? dataFolder.file(at: "2/input").readAsString()) ?? ""))

do {
    try app.run()
} catch {
    print("Whoops! An error occurred: \(error)")
}

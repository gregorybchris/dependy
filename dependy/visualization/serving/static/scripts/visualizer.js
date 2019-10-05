import { GET } from './request-util.js'
import { Simulation } from './simulation.js'

export class Visualizer {
    constructor() {}

    async visualize() {
        let graph = await GET('/api/graph')
        if (graph) {
            console.log(graph)
            this.simulation = new Simulation(graph)
            this.simulation.simulate()
        }
        else
            console.log("Graph could not be loaded")
    }
}
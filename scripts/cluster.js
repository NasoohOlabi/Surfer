/**
* @param { number[] } data
* @param { number } epsilon - the maximum distance between two points to be considered neighbors
* @param { number } minPts - the minimum number of points required to form a dense region
* @param { ((a: number, b: number) => number) } distanceFunction - a function that takes two data points and returns their distance
* @returns { number[][] } - a list of clusters, where each cluster is represented by an array of data points
*/
function dbscan(data, epsilon = 10, minPts = 1, distanceFunction = (a, b) => Math.abs(a - b)) {
	const clusters = [];
	const visited = new Set();
	const noise = new Set();
	// Helper function to find all neighbors within epsilon distance
	function regionQuery(current, data, epsilon, distanceFunction) {
		const neighbors = [];
		for (let i = 0; i < data.length; i++) {
			if (distanceFunction(current, data[i]) <= epsilon) {
				neighbors.push(i);
			}
		}
		return neighbors;
	}
	// Main DBSCAN algorithm
	for (let i = 0; i < data.length; i++) {
		if (!visited.has(i)) {
			visited.add(i);
			const neighbors = regionQuery(data[i], data, epsilon, distanceFunction);
			if (neighbors.length < minPts) {
				noise.add(i);
			} else {
				const cluster = [i];
				clusters.push(cluster);
				for (let j = 0; j < neighbors.length; j++) {
					const neighbor = neighbors[j];
					if (!visited.has(neighbor)) {
						visited.add(neighbor);
						const subNeighbors = regionQuery(data[neighbor], data, epsilon, distanceFunction);
						if (subNeighbors.length >= minPts) {
							neighbors.push(...subNeighbors);
						}
					}
					if (!clusters.some(c => c.includes(neighbor))) {
						cluster.push(neighbor);
					}
				}
			}
		}
	}
	// Add noise points to existing clusters if within epsilon distance
	noise.forEach(noisePoint => {
		for (let i = 0; i < clusters.length; i++) {
			if (distanceFunction(data[noisePoint], data[clusters[i][0]]) <= epsilon) {
				clusters[i].push(noisePoint);
				break;
			}
		}
	});
	return clusters;
}
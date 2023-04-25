/**
* 
* @param {number[][]} points 
* @param {number[]} targetPoint 
* @param {((a:number[],b:number[])=>number)} distanceFunction 
* @returns 
*/
function calculateAverageDistance(points, targetPoint, distanceFunction) {
	const distances = points.map(point => distanceFunction(point, targetPoint));
	return distances.reduce((accumulator, currentValue) => accumulator + currentValue, 0) / distances.length;
}
/**
* 
* @param {number[][]} points 
* @returns 
*/
function calculateAverage(points) {
	return points.reduce((accumulator, currentValue) => accumulator + currentValue, 0) / points.length;
}
function nearestClusters(clusters, distanceFunction) {
	let minDistance = Infinity;
	let closestClusters = [];
	for (let i = 0; i < clusters.length; i++) {
		for (let j = i + 1; j < clusters.length; j++) {
			const cluster1 = clusters[i];
			const cluster2 = clusters[j];
			const distance = distanceFunction(calculateAverage(cluster1), calculateAverage(cluster2));
			if (distance < minDistance) {
				minDistance = distance;
				closestClusters = [cluster1, cluster2];
			}
		}
	}
	return closestClusters;
}
/**
 * 
 * @param {number[][]} clusters 
 * @param {((a:number,b:number)=>number)} distanceFunction 
 */
function agnesIteration(clusters, distanceFunction) {
	let closestClusters = nearestClusters(clusters, distanceFunction);
	const mergedCluster = closestClusters[0].concat(closestClusters[1]);
	clusters.splice(clusters.indexOf(closestClusters[0]), 1);
	clusters.splice(clusters.indexOf(closestClusters[1]), 1);
	clusters.push(mergedCluster);
}
/**
* 
* @param {number[]} data 
* @param {number[][]} clusters 
* @param {((a:number[],b:number[])=>number)} distanceFunction 
* @returns 
*/
function calculateSilhouetteScore(data, clusters, distanceFunction) {
	const scores = data.map((datum, index) => {
		const cluster = clusters.find(cluster => cluster.includes(datum));
		const a = calculateAverageDistance(cluster.filter(otherDatum => otherDatum !== datum), datum, distanceFunction) || 0;
		const b_points = clusters.flatMap(otherCluster => (otherCluster === cluster) ? [] : otherCluster);
		const b = calculateAverageDistance(b_points, datum, distanceFunction);
		return (b - a) / Math.max(a, b);
	});
	return scores.reduce((accumulator, currentValue) => accumulator + currentValue, 0) / scores.length;
}
/**
* 
* @param {number[]} data 
* @param {((a:number[],b:number[])=>number)} distanceFunction 
* @returns 
*/
function agnes(data, distanceFunction = (a, b) => Math.abs(a - b)) {
	data = [...new Set(data)];
	let allClusters = [];
	let clusters = data.map(x => [x]);
	for (let i = 1; i < data.length - 1; i++) {
		agnesIteration(clusters, distanceFunction);
		const score = calculateSilhouetteScore(data, clusters, distanceFunction);
		const clusterCopy = [...clusters];
		clusterCopy.sort((la, lb) => la[0] - lb[0]);
		allClusters.push({ k: clusters.length, score, cluster: clusterCopy });
	}
	return allClusters;
}
function findElbowPoint(clusters) {
	for (let i = 0; i < clusters.length; i++) {
		const c = clusters[i];
		if (c.score < 0.9) {
			return i - 1;
		}
	}
	return 0;
}
function findClosestNumberIndex(arr, target) {
	let closestIndex = 0;
	let closestDistance = Infinity;
	for (let i = 0; i < arr.length; i++) {
		const subArr = arr[i];
		const first = subArr[0];
		const last = subArr[subArr.length - 1];
		if (target < first) {
			const distance = Math.abs(first - target);
			if (distance < closestDistance) {
				closestIndex = i;
				closestDistance = distance;
			}
		} else if (target > last) {
			const distance = Math.abs(last - target);
			if (distance < closestDistance) {
				closestIndex = i;
				closestDistance = distance;
			}
		} else {
			return i;
		}
	}
	return closestIndex;
}
function Agnes(data, x) {
	let ans = agnes(data);
	const idx = findElbowPoint(ans);
	return findClosestNumberIndex(ans[idx].cluster, x);
}
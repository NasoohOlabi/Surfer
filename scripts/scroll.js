function slowScroll(elementSelector, third, fifth) {
	// Find the element to scroll to using the provided selector
	let elementToScroll = document.querySelector(elementSelector);
	if (!elementToScroll) {
		throw new Error(`Element with selector "${elementSelector}" not found.`);
	}
	const thresholded = (x) => (x > 0) ? Math.max(x, 10) : Math.min(x, -10)
	// Get the current height of the view
	let viewHeight = window.innerHeight;

	// Calculate the target scroll position to make the third element at the fifth of the view
	let boundingClientRect = elementToScroll.getBoundingClientRect();
	let targetScrollPos = boundingClientRect.top + (third * boundingClientRect.height) - (viewHeight * fifth) + window.pageYOffset;

	// Define a function to scroll slowly
	function scroll() {
		// Get the current scroll position
		let currentScrollPos = window.pageYOffset;
		// Calculate the distance to scroll in this iteration (10% of the remaining distance)
		let distanceToScroll = thresholded((targetScrollPos - currentScrollPos) * 0.4);
		// Scroll by the calculated distance
		window.scrollBy(0, distanceToScroll);
		// Check if the target scroll position is reached, otherwise continue scrolling
		if (Math.abs(window.pageYOffset - targetScrollPos) > 20) {
			requestAnimationFrame(scroll);
		}
	}

	// Start scrolling slowly
	scroll();
}

// Usage:
slowScroll('#0)', +'#1', +'#2');

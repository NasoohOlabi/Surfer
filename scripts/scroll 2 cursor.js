function slowScroll(third, fifth, speed_factor) {
	window.scrolling = true;
	let elementToScroll = window.cursor;
	const thresholded = (x) => (x > 0) ? Math.max(x, 10) : Math.min(x, -10);
	let viewHeight = window.innerHeight;

	let boundingClientRect = elementToScroll.getBoundingClientRect();
	let targetScrollPos = boundingClientRect.top + (third * boundingClientRect.height) - (viewHeight * fifth) + window.pageYOffset;

	function scroll() {
		console.debug('scroll');
		let currentScrollPos = window.pageYOffset;
		console.debug(`currentScrollPos:${currentScrollPos}`);
		let distanceToScroll = thresholded((targetScrollPos - currentScrollPos) * speed_factor);
		console.debug(`distanceToScroll:${distanceToScroll}`);
		window.scrollBy(0, distanceToScroll);
		console.debug(`|window.pageYOffset - targetScrollPos|=|${window.pageYOffset} - ${targetScrollPos}|=${Math.abs(window.pageYOffset - targetScrollPos)}`);
		if (Math.abs(window.pageYOffset - targetScrollPos) > 20) {
			console.debug(`requestAnimationFrame(scroll);`);
			requestAnimationFrame(scroll);
		} else {
			window.scrolling = false;
		}
	}

	scroll();
}

slowScroll(+'#0', +'#1', +'#2');
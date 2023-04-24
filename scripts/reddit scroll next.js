function slowScroll(third, fifth, speed_factor) {
	window.scrolling = true;
	let elementToScroll = window.curser;
	const thresholded = (x) => (x > 0) ? Math.max(x, 10) : Math.min(x, -10);
	let viewHeight = window.innerHeight;

	let boundingClientRect = elementToScroll.getBoundingClientRect();
	let targetScrollPos = boundingClientRect.top + (third * boundingClientRect.height) - (viewHeight * fifth) + window.pageYOffset;

	function scroll() {
		let currentScrollPos = window.pageYOffset;
		let distanceToScroll = thresholded((targetScrollPos - currentScrollPos) * speed_factor);
		window.scrollBy(0, distanceToScroll);
		if (Math.abs(window.pageYOffset - targetScrollPos) > 20) {
			requestAnimationFrame(scroll);
		} else {
			window.scrolling = false;
		}
	}

	scroll();
}

slowScroll(+'#0', +'#1', +'#2');


curser = curser.nextSibling;
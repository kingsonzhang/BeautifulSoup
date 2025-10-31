let scpa_loadJs = function(path, position) {
	document.addEventListener('DOMContentLoaded', () => {
		let tag = document.createElement('script');
		tag.src = path;
		if (position == 'head') {
			document.head.appendChild(tag);
		}
		if (position == 'body') {
			document.body.appendChild(tag);
		}
	});
};
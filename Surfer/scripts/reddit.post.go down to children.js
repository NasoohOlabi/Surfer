// doesn't have children
// if (!cursor.querySelector('[slot=children]'))
// 	return false;

children = cursor.querySelector('[slot=children]')
first_child = children.firstElementChild
if (first_child.tagName === 'FACEPLATE-PARTIAL') {
	first_child.click()
	cursor = children.firstElementChild
}
else if (first_child.tagName === 'SHREDDIT-COMMENT') {
	cursor = first_child
}
// return true
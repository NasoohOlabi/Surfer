console.log(`document.getElementsByTagName("p") : `);
console.log([].slice.call(document.getElementsByTagName("p")).map(x => x && x.innerText));
let a = [].slice.call(document.getElementsByTagName("p")).filter(span => span.innerText === "Please solve this puzzle so we know you are a real person").length > 0;
console.log(`a : `);
console.log(a);
console.log(`document.getElementsByTagName("button") : `);
console.log([].slice.call(document.getElementsByTagName("button")).map(x => x && x.innerText));
let b = [].slice.call(document.getElementsByTagName("button")).filter(button => button.innerText === "Start Puzzle").length > 0;
console.log(`b : `);
console.log(b);
console.log(`document.getElementsByTagName("h2") : `);
console.log([].slice.call(document.getElementsByTagName("h2")).map(x => x && x.innerText));
let c = [].slice.call(document.getElementsByTagName("h2")).filter(button => button.innerText === "Protecting your account").length > 0;
console.log(`c : `);
console.log(c);
return (a && b && c);

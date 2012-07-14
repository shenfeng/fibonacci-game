function f (n) {
  if(n > 1) {
    return f(n - 1) + f(n - 2);
  }
  return 1;
}

var start = new Date();
console.log(f(40));
var t = new Date() - start;
console.log(t);

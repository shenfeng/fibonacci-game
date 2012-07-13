function f (n) {
  if(n > 1) {
    return f(n - 1) + f(n - 2);
  }
  return 1;
}

console.log(f(40));

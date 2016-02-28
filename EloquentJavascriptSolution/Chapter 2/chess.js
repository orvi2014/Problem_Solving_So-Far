var row = 8;

var chess = "";

for (var y = 0; y < row; y++) {
  for (var x = 0; x < row; x++) {
    if ((x + y) % 2!= 0)
      chess += "#";
    else
      chess += " ";
  }
  chess += "\n";
}

console.log(chess);
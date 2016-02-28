for(var i=1;i<100;i+=1){
  var fizzbuzz=""
  if(i%3==0){
  fizzbuzz+="Fizz";}
  if(i%5==0){
  fizzbuzz+="Buzz";}
  //for modify version uncomment the lines.
  //---------------------------------------
  //  else if(i%15==0){
  //fizzbuzz+="FizzBuzz";}
  //---------------------------------------
  console.log(fizzbuzz||i);
}
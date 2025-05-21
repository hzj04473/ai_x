// 콜백함수 (매개변수에 들어온 함수)
function callTenTimes(callback) {
  for (let i = 0; i < 10; i++) {
    callback();
  }
}

let fun = () => console.log(new Date());
// function callback() {}
callTenTimes(fun);

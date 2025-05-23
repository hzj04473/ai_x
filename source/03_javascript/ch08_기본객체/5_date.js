Date.prototype.getIntervalDay = function (otherDay) {
  // this와 other 사이의 날짜 수를 return
  // now.getIntervalDay(openDay); this가 now , otherDay가 openDay
  // openDay.getIntervalDay(now); this가 openDay, otherDay가 now

  // if (this > otherDay) {
  //   interValMilliSec = this.getTime() - otherDay.getTime();
  // } else {
  //   interValMilliSec = otherDay.getTime() - this.getTime();
  // }

  // var interValMilliSec = this > otherDay ? this.getTime() - otherDay.getTime() : otherDay.getTime() - this.getTime();
  var interValMilliSec = Math.abs(this.getTime() - otherDay.getTime());
  // return Math.floor(interValMilliSec / (1000 * 60 * 60 * 24));// 반올림
  return Math.trunc(interValMilliSec / (1000 * 60 * 60 * 24)); // 내림
};

// let now = new Date();
// console.log(now);
// console.log(now.toLocaleString());
// console.log(now.toLocaleDateString());
// console.log(now.toLocaleTimeString());

// let openDay = new Date(2025, 3, 7, 9, 30, 0); // 월 0,1,2,3, ~ 11 → 4월 이면 3으로
// console.log(`개강일 : ${openDay.toLocaleString()}`);

// // 몇일 차이인지
// let day = now.getIntervalDay(openDay);

// console.log(`now.getIntervalDay(openDay) : ${day} 일 지났다.`);

// day = openDay.getIntervalDay(now);
// console.log(`openDay.getIntervalDay(now) : ${day} 일 지났다.`);

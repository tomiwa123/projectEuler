var total = 0;

for (var i = 0; i < 1000; i++) {
    if (i%3 === 0 && i%5 === 0) {
        total += i;
    }
}

console.log(total);

//New Code

var arr = [1, 2, 3];
var total = 0;

while(arr[arr.length - 1] < 4000000) {
      arr.push(arr[arr.length - 1] + arr[arr.length - 2]);
      };

for (var i = 0; i < arr.length; i++) {
    if ((arr[i])%2 === 0) {
            total += arr[i]
        }
};

console.log(total);

//New Code

var num = 600851475143;
var arr = [];

for (var i = 2; i < num; i++) {
    if (num%i === 0) {
            arr.push(i);
        }
};

console.log(arr);

for (var j = arr.length - 1; j >= 0; j--) {
    for (var k = 0; k < j; k++) {
        if (arr[j]%arr[k] === 0) {
                arr.splice(j, 1);
                console.log(arr);
            }
    }
};
console.log(arr[arr.length - 1]);
/*for (var i = arr.length - 1; i >= 0; i--) {
    if (arr[i] != 'red') {
            return arr[i];
        }
};*/

let number = 42;
console.log(number.toString() + "cool");


//New Code


function testPallindrome(num) {
    let arr = [];
    const num = 222;

    for (var i = 0; i < num.toString()length; i++) {
        arr.push(num.toString()[i])
    }
    console.log(arr);
    arr.reverse().join("")

    if(num === newnum) {
        return true;
    }
}

testPallindrome(22);
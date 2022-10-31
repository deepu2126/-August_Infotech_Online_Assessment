
// Write a JavaScript program to compute the union of two arrays. [5 marks]

// Sample Data : console.log(union([1, 2, 3], [100, 2, 1, 10]));

// Output: [1, 2, 3, 10, 100]

function union(array){
    var result = [];
    for (let i = 0; i < array.length; i++){
        if (result.includes(array[i])){
            // pass
        }else {
            result.push(array[i]);
        }
    }
    return result;
}

var arr1 = [1, 2, 3];
var arr2 = [100, 2, 1, 10];

var array = [...arr1, ...arr2];

console.log(union(array));
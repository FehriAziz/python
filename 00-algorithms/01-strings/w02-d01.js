/* 
Book Index

Given an array of ints representing page numbers
return a string with the page numbers formatted as page ranges when the nums
span a consecutive range.
*/

var nums1 = [1, 13, 14, 15, 37, 38, 70];
var expected1 = "1, 13-15, 37-38, 70";

var nums2 = [5, 6, 7, 8, 9];
var expected2 = "5-9";

var nums3 = [1, 2, 3, 7, 9, 15, 16, 17];
var expected3 = "1-3, 7, 9, 15-17";


function bookIndex(nums) {
    var result = "";
    var start = nums[0];
    var end = nums[0];

    for (let i = 1; i < nums.length; i++) {
        if (nums[i] === end + 1) {
            end = nums[i];
        } else {
            if (start === end) {
                result += start + ", ";
            } else {
                result += start + "-" + end + ", ";
            }

            start = nums[i];
            end = nums[i];
        }
    }

    if (start === end) {
        result += start;
    } else {
        result += start + "-" + end;
    }

    return result;
}

var nums1 = [1, 13, 14, 15, 37, 38, 70];
console.log(bookIndex(nums1)); // Output: "1, 13-15, 37-38, 70"

var nums2 = [5, 6, 7, 8, 9];
console.log(bookIndex(nums2)); // Output: "5-9"

var nums3 = [1, 2, 3, 7, 9, 15, 16, 17];
console.log(bookIndex(nums3)); // Output: "1-3, 7, 9, 15-17"
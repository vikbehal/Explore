function binarySearch(numbers, element) {
    console.log("Collection being serached ", numbers);
    let midpoint = Math.floor(numbers.length / 2);
    if (numbers[midpoint] == element) {
        return true
    } else if (numbers[midpoint] > element) {
        return binarySearch(numbers.slice(0, midpoint, element))
    } else {
        return binarySearch(numbers.slice(midpoint + 1, numbers.length, element))
    }
}
console.log(binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 7));
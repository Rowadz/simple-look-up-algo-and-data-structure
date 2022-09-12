const obj = { human: { user: { prop01: { prop02: { name: 'rowadz' } } } } }

const setVal = (obj, val, ...keys) => keys.reduce((prev, key, index) => {
    if (index === keys.length - 1) {
        prev[key] = val;
        return prev;
    }
    return prev[key];
}, obj)

const path = ['human', 'user', 'prop01', 'prop02', 'name']

setVal(obj, 'aha', ...path)

// { human: { user: { prop01: { prop02: { name: 'aha' } } } } }
console.log(obj);


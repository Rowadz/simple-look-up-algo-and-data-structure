const a = { user: { name: 'rowadz' } }
const b = { user: { name: 'rowadz' } }

const a2 = { human: { user: { name: 'rowadz' } } }
const b2 = { human: { user: { name: 'rowadz' } } }

const obj = { human: { user: { prop01: { prop02: { name: 'rowadz' } } } } }
const obj2 = { human: { user: { prop01: { prop02: { name: 'rowadz' } } } } }

const getVal = (obj, ...keys) => keys.reduce((prev, key) => prev[key], obj)

const abPath = ['user', 'name']

if (getVal(a, ...abPath) === getVal(b, ...abPath)) {
  console.log('nice')
}

const ab2Path = ['human', 'user', 'name']

if (getVal(a2, ...ab2Path) === getVal(b2, ...ab2Path)) {
  console.log('nice 2')
}

const path = ['human', 'user', 'prop01', 'prop02', 'name']

if (getVal(obj, ...path) === getVal(obj2, ...path)) {
  console.log('very nice')
}

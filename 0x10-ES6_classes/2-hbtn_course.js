export default class ClassRoom {
  constructor(name, length, students) {
    if (typeof name !== 'string') throw TypeError('name must be a String');
    if (typeof length !== 'number') throw TypeError('length must be a Number');
    if (!Array.isArray(students)) throw TypeError('students must be an Array');
    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() {
    return this._name;
  }

  get length() {
    return this._length;
  }

  get students() {
    return this._students;
  }

  set name(altName) {
    if (typeof altName !== 'string') throw TypeError('name must be a String');
    this._name = altName;
  }

  set length(altLength) {
    if (typeof altLength !== 'number') throw TypeError('length must be a Number');
    this._length = altLength;
  }

  set students(altStudents) {
    if (!Array.isArray(altStudents)) throw TypeError('students must be an Array');
    altStudents.forEach((student) => {
      if (typeof student !== 'string') throw TypeError('student must be a String');
    });
    this._students = altStudents;
  }
}

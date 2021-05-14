export default class Currency {
  constructor(code, name) {
    if (typeof code !== 'string') throw TypeError('code must be a String');
    if (typeof name !== 'string') throw TypeError('name must be a String');
    this._code = code;
    this._name = name;
  }

  get code() {
    return this._code;
  }

  get name() {
    return this._name;
  }

  set code(altCode) {
    if (typeof altCode !== 'string') throw TypeError('code must be a String');
    this._code = altCode;
  }

  set name(altName) {
    if (typeof altName !== 'string') throw TypeError('name must be a String');
    this._name = altName;
  }

  displayFullCurrency() {
    return `${this.name} (${this.code})`;
  }
}

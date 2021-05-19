export default function getStudentIdsSum(studentList) {
  return studentList.map((_) => _.id).reduce((accum, initial) => accum + initial);
}

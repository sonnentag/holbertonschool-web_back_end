const getStudentsByLocation = (studentList, city) => {
  const studentsLocation = studentList.filter(
    (_) => _.location === city,
  );
  return studentsLocation;
};

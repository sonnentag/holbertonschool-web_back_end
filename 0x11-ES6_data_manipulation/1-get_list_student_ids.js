const getListStudentIds = (objectArray) => {
  if (!Array.isArray(objectArray)) {
    return [];
  }
  let idList = objectArray.map((_) => _.id);
  return idList;
};

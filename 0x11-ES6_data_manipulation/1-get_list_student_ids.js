const getListStudentIds = (objectArray) => {
  if (!Array.isArray(objectArray)) {
    return [];
  }
  const idList = objectArray.map((_) => _.id);
  return idList;
};

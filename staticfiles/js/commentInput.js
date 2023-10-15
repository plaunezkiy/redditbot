function handler() {
  return {
    fields: [],
    addCommentField() {
      this.fields.push({
        url: "",
      });
    },
    removeField(index) {
      this.fields.splice(index, 1);
    },
  };
}

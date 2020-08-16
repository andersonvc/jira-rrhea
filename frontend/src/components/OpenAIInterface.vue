<template>
  <div id="content">
    <el-row>
      <el-col :span="6">
        <img alt="sidebar" src="../assets/jira-sidebar.png" style="max-width:100%;" align="top" />
      </el-col>

      <el-col :span="18">
        <div style="margin: 38px;"></div>

        <el-form :label-position="Top" label-width="100px" :model="formLabelAlign">
          <el-form-item label="Jira Title">
            <el-input v-model="formLabelAlign.title"></el-input>
          </el-form-item>

          <el-form-item label="Description">
            <el-input
              type="textarea"
              v-model="formLabelAlign.Description"
              :autosize="{ minRows: 25, maxRows: 10}"
            ></el-input>
          </el-form-item>
        </el-form>

        <div style="margin: 10px;"></div>

        <el-button
          type="primary"
          square
          icon="el-icon-lollipop"
          size="small"
        >BS for me</el-button>


      </el-col>
    </el-row>
  </div>
</template>




<script>
export default {
  name: "OpenAIInterface",
  data: () => {},
  methods: {},
};
</script>


// stuff that's needed to make the input appear i think?
<script>
export default {
  data() {
    return {
      formLabelAlign: {
        title: "",
        Description: "",
        type: "",
      },
    };
  },
};
</script>





<style scoped>
</style>
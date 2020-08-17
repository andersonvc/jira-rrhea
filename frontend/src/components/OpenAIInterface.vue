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
            <el-input v-model=title></el-input>
          </el-form-item>

          <el-form-item label="Description">
            <el-input
              type="textarea"
              v-model=blah
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
          @click="submit"
        >BS for me</el-button>


      </el-col>
    </el-row>
  </div>

</template>


// stuff that's needed to make the input appear i think?
<script>
export default {
  name: 'OpenAIInterface',
  data: () => (
    {
      blah:"OpenAI generated Jira ticket description. Update Jira ticket title to start.",
      word_count:0,
      temperature:0.94,
      is_processing:false,
      title:"Add back button to search nav.",
      formLabelAlign: {
        title: "",
        Description: "",
        type: "",
      },
    }),

    methods: {

        async submit(){
          if (this.is_processing==true){
            return
          }

            let config = {
                headers: {
                //"X-CSRFToken": this.csrfToken,
                "Content-Type": 'application/x-www-form-urlencoded',
                }
            }

            this.blah = "";
            let formData = new FormData();
            formData.set('statement', this.title);
            formData.set('hist', 'DUMMY');
            formData.set('temp', '0.93');

            this.is_processing = true;

            await this.axios
            .post('http://llamaland.local:3001/v1/nlp/gpt3/completions/', formData, config)
            .then(resp => {
                this.blah = resp.data.response;
                this.is_processing = false;
            })
            .catch(error => {
                this.is_processing = false;
                console.log(error.response.data)
            });
        }
    }
};
</script>





<style scoped>
</style>
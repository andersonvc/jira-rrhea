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


<el-row type="flex" justify="end">
          
          <el-col :span='13'>
          <el-form :label-position="Top" label-width="100px" :model="formLabelAlign">
          <el-form-item label="Randomness">
            <el-select v-model="randomness_value" placeholder="Set BS Level">
              <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>
          </el-form-item>
          </el-form>
          </el-col>

          

          <el-col :span='3'>
            <pulse-loader :loading="is_processing" :color="color" :size="size"></pulse-loader>
          </el-col>
          <el-col :span='14'>
            <el-button
              type="primary"
              square
              icon="el-icon-lollipop"
              @click="clear_history"
            >Clear History</el-button>

          <el-button
            type="primary"
            square
            icon="el-icon-lollipop"
            @click="submit"
          >BS for me</el-button>
          </el-col>
        </el-row>


          <el-form-item label="Description">
            <el-input
              type="textarea"
              v-model=blah
              :autosize="{ minRows: 25, maxRows: 10}"
            >
            
            
            </el-input>
          </el-form-item>
        </el-form>

        <div style="margin: 10px;"></div>


      </el-col>
    </el-row>
  </div>

</template>


// stuff that's needed to make the input appear i think?
<script>

import PulseLoader from 'vue-spinner/src/PulseLoader.vue'

export default {
  name: 'OpenAIInterface',
  components: { PulseLoader },
  data: () => (
    {
      loading: true,
      blah:"OpenAI generated Jira ticket description. Update Jira ticket title to start.",
      hist:"DUMMY",
      word_count:0,
      temperature:0.94,
      is_processing:false,
      title:"Add back button to search nav.",
      formLabelAlign: {
        title: "",
        Description: "",
        type: "",
      },
      options: [{
          value: '0.8',
          label: 'Minimal'
        }, {
          value: '0.9',
          label: 'Slight'
        }, {
          value: '0.93',
          label: 'Recommended'
        }, {
          value: '0.95',
          label: 'Moderate'
        }, {
          value: '0.98',
          label: 'Max Randomness'
        }],
        randomness_value: '0.93'
    }),

    methods: {

        clear_history(){
          this.hist = "DUMMY"
        },
        async submit(){
          console.log(this.value)
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
            formData.set('hist', this.hist);
            formData.set('temp', this.randomness_value);

            this.is_processing = true;

            await this.axios
            .post('http://llamaland.local:3001/v1/nlp/gpt3/completions/', formData, config)
            .then(resp => {
                this.blah = resp.data.response;
                this.hist = resp.data.hist;
                this.is_processing = false;
                console.log(resp.data.hist);
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
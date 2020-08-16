<template>
<el-row>


    <el-col :span="12">
        
        <el-card class="box-card">

            <div slot="header" class="clearfix">
                <span>Jira Input</span>
            </div>

            <el-form :inline="true" :model="formInline" class="demo-form-inline">
                <el-row>
                    <el-form-item label="Jira Title">
                        <el-input v-model="form.title"></el-input>
                    </el-form-item>
                </el-row>
                
                <el-row>
                    <el-form-item label="Jira Flavor">
                        <el-select v-model="form.region" placeholder="please select your Jira flavor">
                        <el-option label="Business Formal" value="business"></el-option>
                        <el-option label="Passive Agressive" value="passive-agressive"></el-option>
                        <el-option label="Too Creative" value="creative"></el-option>
                        </el-select>
                    </el-form-item>
                </el-row>


                <el-row>
                    <el-button type="primary" icon="el-icon-magic-stick">Generate Jira Description</el-button>
                </el-row>
            </el-form>
        </el-card>
        
    </el-col>

    <el-col :span="12">
        <el-row>
            <h4>Result</h4>
        </el-row>

    </el-col>

</el-row>



</template>






<script>
export default {
  name: "OpenAIInterface",
  data: () => {},
  methods: {},
};
</script>


// stuff that's needed to make the form appear
<script>
  export default {
    data() {
      return {
        form: {
          name: '',
          region: '',
          date1: '',
          date2: '',
          delivery: false,
          type: [],
          resource: '',
          desc: ''
        }
      }
    },
    methods: {
      onSubmit() {
        console.log('submit!');
      }
    }
  }
</script>





<style scoped>
</style>
<template>
<div>
    <v-form>
        <v-container>
            <v-row>
                <h2>Magic Jira Desciption Generator</h2>
            </v-row>
            <v-row>
                <v-col cols='12' md='4'>
                    <v-row>
                        <v-text-field v-model='title' label='JIRA TITLE' required />
                    </v-row>

                    <v-row>
                        <v-textarea v-model='blah' label='Generated Text' > {{ blah }}</v-textarea>
                    </v-row>
                </v-col>

                <v-col cols='12' md='4'>
                    <v-row>
                        <v-h1> Options </v-h1>
                    </v-row>
                    <v-row>
                        <v-select v-model='selected_randomness' :items='randomness_options' outlined dense label='How random do you want this to be?' />
                    </v-row>
                    <v-row>
                        <v-text-field v-model='word_count' dense outlined integer label='How many words do you need?' />
                    </v-row>
                    <v-row>
                        <v-text>Recommended number of words is 200. </v-text>
                    </v-row>
                    <v-row>
                        <v-btn color='accept' class='submit-button' @click='submit'>Generate Legit BS</v-btn>
                    </v-row>
                </v-col>
            </v-row>
        </v-container>
    </v-form>
</div>
</template>

<script>
export default {
    name: 'JiraForm',
    data: () => ({
        word_count: 0,
        title: "",
        selected_randomness: 'I need some BS',
        randomness_options: ['Straightforward','I need some BS','I really need to BS'],
        generated_text: "",
        blah: "nsthsnth"


    }),
    methods: {
        async submit(){

            let config = {
                headers: {
                //"X-CSRFToken": this.csrfToken,
                "Content-Type": 'application/x-www-form-urlencoded',
                }
            }

            let formData = new FormData();
            formData.set('prompt', this.title);
            formData.set('word_count', this.word_count);
            formData.set('temperature', 0.5);

            await this.axios
            .post('http://localhost:3001/v1/nlp/dummy/completions/', formData, config)
            .then(resp => {
                this.blah = resp.data.text;
            })
        }
    }
}
</script>
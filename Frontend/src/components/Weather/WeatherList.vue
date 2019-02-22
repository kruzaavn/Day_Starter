<template>
    <div class="weather-list">
        <WeatherItem v-for="(item, index ) in list.list" :key="index" v-bind:item="item" :index="index" />
    </div>
</template>

<script>

    import axios from 'axios'
    import WeatherItem from "./WeatherItem";

    export default {
        name: "WeatherList",
        components: {WeatherItem},
        data() {
            return {
                list: [],
                poll: null
            }
        },

        methods: {
            getData: function () {

                const options = {
                    method: 'get',
                    baseURL: 'http://localhost:8081',
                    params: {
                        city: 'washington',
                        forecast: true
                    }
                };

                axios.get('/api/weather/', options).then(response => (this.list = response.data))
            },

            pollData: function() {
              this.poll = setInterval(() => this.getData(), 10 * 60 * 1000)
            }
        },

        beforeDestroy () {
            clearInterval(this.polling)
        },

        created: function () {
            this.getData();
            this.pollData()
        }
    }
</script>

<style scoped>

</style>
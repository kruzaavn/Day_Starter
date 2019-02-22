<template>
    <div class="clock">
        <p>{{ time }}</p>
        <WeatherList />
    </div>
</template>

<script>
    import WeatherList from "../Weather/WeatherList";
    export default {
        name: "ClockItem",
        components: {WeatherList},
        data() {
            return {
                time: null,
                interval: null
            }
        },
        methods: {
                getTime: function () {
                    const options = {
                      hour: '2-digit', minute:'2-digit'
                      };

                    this.time = new Date().toLocaleTimeString('en-US', options)
                },

                pollTime: function() {
                    this.interval = setInterval(() => this.getTime(), 500)
                    }
                },

                beforeDestroy () {
                    clearInterval(this.interval)
                },

                created: function () {
                    this.getTime();
                    this.pollTime()
                }
    }
</script>

<style scoped>
    .clock {
        color: white;
        margin: 0 .5em;
        font-size: 4em;
    }

    p {
        margin: 0;
        padding: 0;
    }

</style>
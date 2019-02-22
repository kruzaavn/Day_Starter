<template>
    <div class="weather-item">
        <p>{{ item }}</p>
    </div>
</template>

<script>
    export default {
        name: "WeatherItem",
        props: ['item', 'index'],
        methods: {
            farenheit: function (kelvin) {

                return  this.celsius(kelvin) * (9/5) +32;

            },
            celsius: function (kelvin) {

                return kelvin - 273.15;

            },

        }
    }
</script>

<style scoped>
    p {
        font-size: 12pt;
    }
</style>
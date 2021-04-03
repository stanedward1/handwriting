<template>
    <div class="home">
        <Header />
        <Banner />
        <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
        <Footer />
    </div>
</template>

<script>
    import Header from '../components/Header'
    import Footer from '../components/Footer'
    import Banner from '../components/Banner'

    export default {
        name: "Home",
        components: {
            Header,
            Footer,
            Banner,
        }
    }
</script>

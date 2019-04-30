<template>
    <div v-if="authenticated">
        <h1>Home</h1>
    </div> 
</template>

<script>
    export default {
        props: {
            authenticated: Boolean
        }
    }
</script>
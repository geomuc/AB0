<template>
    <div v-if="authenticated">
        <h1>Auskunft</h1>
    </div> 
</template>

<script>
    export default {
        props: {
            authenticated: Boolean
        }
    }
</script>
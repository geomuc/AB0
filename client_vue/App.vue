<template>
    <div id="app">
        <div class="container">
            <div class="row">
                <div class="col-xs-12 col-sm-8 col-sm-offset-1 col-md-6 col-md-offset-2">
                    <ul class="nav nav-pills">
                    <li class="nav-item">
                        <router-link v-if="authenticated" to="/">Home</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link v-if="authenticated" to="/auskunft">Auskunft</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link v-if="authenticated" to="/bearbeiten">Bearbeiten</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link v-if="authenticated" to="/login" v-on:click.native="logout()" replace>Logout</router-link>
                    </li>
                    </ul>
                </div>
            </div>
        </div>
        <!--<div id="nav">
            <router-link v-if="authenticated" to="/login" v-on:click.native="logout()" replace>Logout</router-link>
        </div>-->
        <router-view @authenticated="setAuthenticated" :authenticated="authenticated"/>
    </div>
</template>

<script>
    export default {
        name: 'App',
        data() {
            return {
                authenticated: false,
                mockAccount: {
                    username: "testuser",
                    password: "test"
                }
            }
        },
        mounted() {
            if(!this.authenticated) {
                this.$router.replace({ name: "login" });
            }
        },
        methods: {
            setAuthenticated(status) {
                this.authenticated = status;
            },
            logout() {
                this.authenticated = false;
            }
        }
    }
</script>

<!--<style>
    body {
        background-color: #F0F0F0;
    }
    h1 {
        padding: 0;
        margin-top: 0;
    }
    #app {
        width: 1024px;
        margin: auto;
    }
</style>-->

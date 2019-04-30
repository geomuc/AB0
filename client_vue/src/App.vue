<template>
    <div id="app">
        <div>
            <b-navbar toggleable="sm" type="dark" variant="info">
                <b-navbar-brand>AB0</b-navbar-brand>
                <b-navbar-toggle target="nav_collapse" />
                <b-collapse is-nav id="nav_collapse">
                    <b-navbar-nav>
                        <b-nav-item v-if="authenticated" to="/">Home</b-nav-item>
                        <b-nav-item v-if="authenticated" to="/auskunft">Auskunft</b-nav-item>
                        <b-nav-item v-if="authenticated" to="/bearbeiten">Bearbeiten</b-nav-item>
                    </b-navbar-nav>
                    <b-navbar-nav class="ml-auto">
                        <b-nav-item  v-if="authenticated" to="/login" v-on:click="logout()">Logout</b-nav-item>
                    </b-navbar-nav>
                </b-collapse>
            </b-navbar>
        </div>
        <div class="container">
            <div class="row">
                <!--<div class="col-xs-12 col-sm-10 col-sm-offset-1 col-md-8 col-md-offset-2">-->
                    <div class="col-sm-8 col-sm-offset-1">
        <router-view @authenticated="setAuthenticated" :authenticated="authenticated"/>
                </div>
            </div>
        </div>
        <!--<div id="nav">
            <router-link v-if="authenticated" to="/login" v-on:click.native="logout()" replace>Logout</router-link>
        </div>-->

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

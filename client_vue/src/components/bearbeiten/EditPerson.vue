<template>
  <div id="editeingabe">
    <p> Id: {{form.id}}</p>
    <b-form @submit="onSubmit" @reset="onReset" v-if="show">
      <b-form-group
        id="nachnameInputGroup"
        label="Nachname:"
        label-for="Nachnamelf"
      >
        <b-form-input
          id="nachname"
          type="text"
          v-model="form.nachname"
          required
          placeholder="Nachname eingeben" />
      </b-form-group>

      <b-form-group id="vornameInputGroup" label="Vorname:" label-for="Vornamelf">
        <b-form-input
          id="vornameInput"
          type="text"
          v-model="form.vorname"
          required
          placeholder="Vorname eingeben" />
      </b-form-group>

    <b-form-group id="geburtstagInputGroup" label="Geburtstag:" label-for="Geburtstaglf">
        <b-form-input
          id="geburtstagInput"
          type="text"
          v-model="form.geburtstag"
          required
          placeholder="Geburtstag eingeben" />
      </b-form-group>

      <b-form-group id="blutgruppeInputGroup" label="Blutgruppe:" label-for="Blutgruppelf">
        <b-form-select id="exampleInput3" :options="blutgruppen" required v-model="form.blutgruppe" />
      </b-form-group>

      <b-button type="submit" variant="primary">Submit</b-button>
      <b-button type="reset" variant="danger">Reset</b-button>
    </b-form>
  </div>
</template>

<script>
  export default {
    props:{person: Object},
    data() {
      return {
        form: {
          id: null,
          nachname: '',
          vorname: '',
          geburtstag: '',
          blutgruppe: ''
        },
        blutgruppen: [{ text: 'Bitte wählen', value: null }, '0', 'A', 'B', 'AB'],
        show: true,
        updatestate : false
      }
    },
    methods: {
      clearForm(){
        this.form.id=null
        this.form.nachname = ''
        this.form.vorname = ''
        this.form.geburtstag = ''
        this.form.blutgruppe = null
        /* Trick to reset/clear native browser form validation state */
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
      },
      onSubmit(evt) {
        evt.preventDefault()
        console.log(this.updatestate)
        if (this.updatestate) {
          var neueperson=this.form
          this.$emit('personEditiert', neueperson)
        } else {
          var neueperson=this.form
          this.$emit('neuePersonErstellt', neueperson)
        }
        //alert(JSON.stringify(this.form))
      },
      onReset(evt) {
        evt.preventDefault()
        /* Reset our form values */
        this.clearForm();
      },
      onInitial(evt) {
        this.form=this.person
        /* Trick to reset/clear native browser form validation state */
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
      }
    },
    watch: { 
      	person: function(newVal, oldVal) { // watch it
          console.log('Prop changed: ', newVal, ' | was: ', oldVal);
          if (this.person.id==null){
            this.updatestate=false
          } else {
            this.updatestate = true
          }
          this.onInitial();
        }
      }
  }
</script>

<style>

#editeingabe {max-width: 300px;}
</style>
<template>
  <div v-if="authenticated">
    <h1>Blutgruppenauskunft</h1>
    <div v-show="liststate">
    <button @click="erstellePerson">Neue Person</button>
    <ListePersonen 
      :personen="personen"/>
    <hr>
    </div>
    <EditPerson :person="aktuellePerson" v-show="editstate" @neuePersonErstellt="addPerson" @personEditiert="editiertPerson"/>

  </div>
</template>

<script>
import ListePersonen from './ListePersonen.vue'
import EditPerson from './EditPerson.vue'
import {eventBus} from '../../main.js';

export default {
  name: 'app',
  components: {
    ListePersonen,
    EditPerson
  },
  props: {
      authenticated: Boolean
  },
  data: function (){
    return {
      //urlapi: "http://localhost:8080/persons/",
      //urlapi: "/api/v1/namespaces/abo/services/aboapi/persons/",
      urlapi: "http://localhost:5000/api/v1/person/",
      personleer: {id: null, nachname: "", vorname: "", geburtstag: "", blutgruppe: ""},
      personen: [{id: 1, nachname: "", vorname: "", geburtstag: "", blutgruppe: ""}],
        //{id: 1, nachname: "Schneider", vorname: "Hans", geburtstag: "17-03-2000", blutgruppe: "A"},
        //{id: 2, nachname: "Wagenknecht", vorname: "Eva", geburtstag: "06-03-1956", blutgruppe: "0"},
        //{id: 3, nachname: "Lee", vorname: "Maria", geburtstag: "12-12-1983", blutgruppe: "AB"}
      //],
      person: this.personleer,
      editstate : false,
      liststate : true,
      aktuellePerson: {id: null, nachname: '', vorname: '', geburtstag: '', blutgruppe: ''}
    }
  },
  methods: {
    addPerson: function(value){
      console.log('füge Person hinzu');
      console.log(value);
      this.$http.post(this.urlapi, value).then(response => {
        console.log('Antwort Post:');
        console.log(response.body);
        this.person={
          id: response.body.id,
          nachname: response.body.nachname,
          vorname: response.body.vorname,
          geburtstag: response.body.geburtstag,
          blutgruppe: response.body.blutgruppe
          };
        this.personen.push(this.person);
      },  response => {
       console.log('error');
      });
      this.editstate = false;
      this.liststate = true;
    },
    erstellePerson: function () {
      console.log ('erstelle Neue Person ...');
      this.editstate = true;
      this.liststate = false;
      this.aktuellePerson=this.personleer;
    },
    ladeDaten: function () {
      console.log ('Daten aus DB laden ...');
      // GET /someUrl
      this.$http.get(this.urlapi).then(response => {

      this.personen=response.body;
      console.log(response.body);
      }, response => {
       console.log('error');
      });
    },
    sichereDaten: function () {
      console.log ('Daten in DB sichern ...');
    },
    editiertPerson: function (value) {
      console.log(value)
      let url=this.urlapi+value.id;
      this.$http.put(url,value).then(response => {
        console.log(response.body);
        this.personen[this.personen.findIndex(element => String(element.id) == String(value.id))]=value;
      }, response => {
        console.log('error');
      });
      this.editstate = false;
      this.liststate = true;
    }

  },
  created () {
    this.ladeDaten();
    eventBus.$on('personLoeschen', (id) => {
      console.log('event gefangen: loesche person');
      console.log(id);
      let url=this.urlapi+id;
      this.$http.delete(url).then(response => {
        console.log(response.body);
        let personel=this.personen.find(element => String(element.id) == String(id));
        this.personen.splice(this.personen.indexOf(personel),1);
      }, response => {
        console.log('error');
      });


    });
    eventBus.$on('personEditieren', (id) => {
      console.log('event gefangen: editiere person');
      console.log(id);
      let i;
      let person;
      for (i = 0; i < this.personen.length; i++) {
          person=this.personen[i];
          if (person.id == id){
            this.aktuellePerson=person
          }                   
      };
      console.log(this.aktuellePerson);
      this.editstate = true;
      this.liststate = false;
    });
  }
}
</script>

<style>
</style>
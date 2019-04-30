<template>
    <!--<p>{{ nachname }}, {{ vorname }}</p>-->
    <tr>
    <td>{{ person.id }} </td>
    <td>{{ person.nachname }} </td>
    <td>{{ person.vorname }}</td>
    <td>{{ person.geburtstag }}</td>
    <td>{{ person.blutgruppe }}</td>
    <td><button @click="editierePerson">Editieren</button></td>
    <td><button @click="loeschePerson">Löschen</button></td>
    </tr>
</template>

<script>
import {eventBus} from '../../main.js';

export default {
  name: 'ListPerson',
  props: {
    person: Object,
  },
  methods: {
    editierePerson: function (){
      console.log('Person editieren');
      eventBus.editPerson(this.person.id);
    },
    loeschePerson: function (){
      console.log('Person löschen');
      eventBus.deletePerson(this.person.id);

    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>

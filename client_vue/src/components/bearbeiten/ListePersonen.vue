<template>
  <div class="listepersonen">
    <table class="table table-striped">
    <tr>
      <th> ID </th>
      <th> Nachname </th>
      <th> Vorname </th>
      <th> Geburtstag </th>
      <th> Blutgruppe </th>
      <th> Editieren </th>
      <th> Löschen </th>
    </tr>
    <tbody>
        <ListPerson v-for="person in personen" v-bind:key="person.id" :person="person"/>
    </tbody>
    </table>

  </div>
</template>

<script>
import ListPerson from './ListPerson.vue'

export default {
  name: 'ListePersonen',
  props: {
    personen: Array,
    index: Number
  },
  components: {
    ListPerson
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>

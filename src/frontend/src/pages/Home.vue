<template>
  <h1>Home Page</h1>

  <div>
  
    <div class='inline-block-child'>
      <button type="button" class="btn btn-primary"  @click="goToTickets">
                My Tickets
      </button>
    </div>

    <div class='inline-block-child' v-if="authStore.user.role == 'ORG'">
      <button type="button" class="btn btn-primary" @click="goToOrganizerPanel">
              Organizer Panel 
      </button>
    </div>

    <div class='inline-block-child'>
      <button @click="logout">Logout</button>
    </div>

  </div>
  

  <h3>List of all Events:</h3>
  
  <!-- <p>{{authStore.user }}</p> -->

  <!-- <p>{{allEventsData.data}}</p> -->

  <!-- <p>selected id: {{dataStore.eventPreviewID}}</p> -->

  <div v-if="allEventsData.length === 0">
    No events at the moment.
  </div>
  <div v-else>
    <table>
      <thead>
            <tr>
              <th> Event </th>
              <th> Location </th>
              <th> Time </th>
              <th> Organizer </th>
              <th> Preview </th>
            </tr>
      </thead>

      <tbody>
        <tr v-for='(event, index) in allEventsData.data'>
          <td>{{ event.title }}</td>
          <td>{{ event.location }}</td>
          <td>{{ event.start_time }}</td>
          <td>{{ event.organizer }}</td>
          <td>
            <button type="button" class="btn btn-primary" @click="view_event_details" :id="event.event_id">
              View Details
            </button>
          </td>
        </tr>
      </tbody>

    </table>
  </div>
               
  


</template>


<script>

import { useAuthStore } from '../store/auth.js'
import { useDataStore } from '../store/data.js'
import { useRouter } from 'vue-router'
import { getEventsData } from '../store/data.js'
import { onMounted, ref, onBeforeMount} from "vue"

export default {

  
  setup() {
    const authStore = useAuthStore()
    const router = useRouter()
    const dataStore = useDataStore()
    var allEventsData = ref([]);

    onBeforeMount(async () => {
      const res = await getEventsData()
      allEventsData.value = res
    });

    // const fetchMessage = async () => {
    //   const res = await getEventsData()
    //   allEventsData.value = res
    // }
    // fetchMessage();
    

    return {
      authStore, router, allEventsData, dataStore
    }
  },
  methods: {
    view_event_details(event){
      //we get and store the selected event ID
      this.dataStore.setSelectedEvent(event.target.id)
      //Then we route to the event preview page
      this.$router.push('/preview')
    },
    goToOrganizerPanel(){
      this.$router.push('/organizer-panel')
    },
    goToTickets(){
      this.$router.push('/tickets')
    },
    async logout() {
      try {
        await this.authStore.logout(this.$router)
      } catch (error) {
        console.error(error)
      }
    }
  },

 

  //display all events in a table (with a link to registration page)

}

</script>

<style>
  thead,
  tfoot {
    background-color: #2c5e77;
    color: #fff;
  }

  tbody {
    background-color: #e4f0f5;
  }

  table {
    border-collapse: collapse;
    border: 2px solid rgb(140 140 140);
    font-family: sans-serif;
    font-size: 0.8rem;
    letter-spacing: 1px;
  }

  caption {
    caption-side: bottom;
    padding: 10px;
  }

  th,
  td {
    border: 1px solid rgb(160 160 160);
    padding: 8px 10px;
  }

  td {
    text-align: center;
  }

  .inline-block-child {
    display: inline-block;
    padding: 0.3rem;
  }
  
</style>
<template>
    <h1>Organizer Panel</h1>
    
    <div>
      <div class='inline-block-child'>
        <button type="button" class="btn btn-primary" @click="goToHome">
            << Go back to home page
        </button>
      </div>

      <div class='inline-block-child'>
        <button type="button" class="btn btn-primary" @click="goToCreateEvent">
            Create New Event
        </button>
      </div>
    </div>


    <br><br>
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
                <th> Tickets Booked </th>
                <th> Update Events </th>
                <th> Delete Events </th>
              </tr>
        </thead>

        <tbody>
          <tr v-for='(event, index) in allEventsData.data'>
            <td>{{ event.title }}</td>
            <td>{{ event.location }}</td>
            <td>{{ event.start_time }}</td>
            <td>{{ event.ticket_count }}</td>
            <td>
              <button type="button" class="btn btn-primary" @click="goToUpdateEvent" :id="event.event_id">
                Update
              </button>
            </td>
            <td>
              <button type="button" class="btn btn-primary" @click="deleteEvent" :id="event.event_id">
                Delete
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
import { getOrganizerEventsData } from '../store/data.js'
import { onMounted, ref, onBeforeMount} from "vue"
import { getCSRFToken } from '../store/auth'
import { getEventData } from '../store/data.js'

export default {

  
  setup() {
    const authStore = useAuthStore()
    const router = useRouter()
    const dataStore = useDataStore()
    var allEventsData = ref([]);

    onBeforeMount(async () => {
      const res = await getOrganizerEventsData()
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
    async deleteEvent(event){

      const response = await fetch("http://localhost:8000/events/api/delete-event", {
                method: 'POST',
                credentials: 'include',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken()
                },
                body: JSON.stringify({"event_id": event.target.id})
            })
            if (response.ok) {
                //const data = await response.json()
                this.success = 'Event Created successfully'
                this.$router.go()
            } else {
                this.error = data.error || 'Failed to create event'
            }
    },
    async goToUpdateEvent(event){

      //we get and store the selected event ID
      //console.log(event.target.id)
      const data = await getEventData(event.target.id)

      this.dataStore.setSelectedEvent(event.target.id, data)

      //Then we route to the update event page
      this.$router.push('/update-event')

    },
    goToCreateEvent(){
      this.$router.push('/create-event')
    },
    goToHome(){
      this.$router.push('/home')
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
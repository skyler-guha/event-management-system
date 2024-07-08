<template>
    <h1>My Tickets</h1>


    <!-- <p>{{ allTicketsData }}</p> -->
    <div v-if="allTicketsData.data.length === 0">
        No Tickets booked under your name yet.
    </div>
    <div v-else>
        <table>
        <thead>
                <tr>
                <th> Ticket ID </th>
                <th> Event </th>
                <th> Purchase Time </th>
                <th> Delete Ticket </th>
                </tr>
        </thead>

        <tbody>
            <tr v-for='(ticket, index) in allTicketsData.data'>
            <td>{{ ticket.ticket_id }}</td>
            <td>{{ ticket.event }}</td>
            <td>{{ ticket.purchase_time }}</td>
            <td>
              <button type="button" class="btn btn-primary" @click="deleteTicket" :id="ticket.ticket_id">
                Delete
              </button>
            </td>
            
            </tr>
        </tbody>
        </table>
    </div>

    <br>
    
    <div class='inline-block-child'>
        <button type="button" class="btn btn-primary" @click="goToHome">
            << Go back to home page
        </button>
    </div>
    
    
</template>

<script>

import { useAuthStore } from '../store/auth.js'
import { useDataStore } from '../store/data.js'
import { useRouter } from 'vue-router'
import { getTicketsData } from '../store/data.js'
import { onMounted, ref, onBeforeMount} from "vue"
import { getCSRFToken } from '../store/auth'

export default {

  
  setup() {
    const authStore = useAuthStore()
    const router = useRouter()
    const dataStore = useDataStore()
    var allTicketsData = ref([]);

    onBeforeMount(async () => {
      const res = await getTicketsData()
      allTicketsData.value = res
    });

    
    

    return {
      authStore, router, allTicketsData, dataStore
    }
  },
  methods: {
    view_event_details(event){
      //we get and store the selected event ID
      this.dataStore.setSelectedEvent(event.target.id)
      //Then we route to the event preview page
      this.$router.push('/preview')
    },
    goToHome(){
    this.$router.push('/home')
    },
    async deleteTicket(event){
        const response = await fetch("http://localhost:8000/events/api/delete-ticket", {
                method: 'POST',
                credentials: 'include',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken()
                },
                body: JSON.stringify({"ticket_id": event.target.id})
            })
            if (response.ok) {
                //const data = await response.json()
                this.success = 'Ticket deleted successfully'
                this.$router.go()
            } else {
                this.error = data.error || 'Failed to ticket event'
            }
    },
  },

 
}

</script>

<style>
.inline-block-child {
    display: inline-block;
    padding: 0.3rem;
  }
</style>
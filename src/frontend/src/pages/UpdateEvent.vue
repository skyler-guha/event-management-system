

<template>
  <h1>Update Event</h1>
  
  <br>
    <form  @submit.prevent="createEvent">

        
        <label>Event Title:</label>
        <input v-model="eventTitle" id="eventTitle" type="text" required @input="resetError">

        <br><br>

        <label>Address:</label>
        <input v-model="Address" id="Address" type="text" required @input="resetError">
        
        <br><br>

        <div style="width: 300px;"   >
            <label>Start date and time:</label>
            <VueDatePicker v-model="startDate" utc required @input="resetError" />
        </div>

        <br>

        <div style="width: 300px;"   >
            <label>End date and time:</label>
            <VueDatePicker v-model="endDate" utc required @input="resetError" />
        </div>

        <br>

        <div>
            <label>Event description:</label> <br>

            <textarea rows="5" cols="70" required @input="resetError" v-model="eventDesc"></textarea> 
        </div>

        <br><br>
        <div>
          <div class='inline-block-child'>
            <button type="button" class="btn btn-primary" @click="goToOrganizerPanel">
                << Go back to organizer panel
            </button>
          </div>
          <div class='inline-block-child'>
            <button type="submit">Update Event</button>
          </div>
        </div>


    </form>

    <p v-if="error">{{ error }}</p>
    <p v-if="success">{{ success }}</p>

</template>



<script>
import { ref, onMounted, onBeforeMount } from 'vue';
import VueDatePicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css'
import { useAuthStore } from '../store/auth'
import { getCSRFToken } from '../store/auth'
import { getEventData } from '../store/data.js'
import { useDataStore } from '../store/data.js'

export default {
    components: {
        VueDatePicker
  },
  setup() {
    const authStore = useAuthStore()
    const dataStore = useDataStore()
    const startDate = ref();
    const endDate = ref()
    const eventTitle = dataStore.otherData.data.title;
    const Address = dataStore.otherData.data.location;
    const eventDesc = dataStore.otherData.data.description

    startDate.value = dataStore.otherData.data.start_time_raw;
    endDate.value = dataStore.otherData.data.end_time_raw;

    return {
      authStore, dataStore, startDate , endDate, error: "", success: "",
      eventTitle, Address, eventDesc
    }
  },
  methods: {
    async createEvent() {
        const response = await fetch("http://localhost:8000/events/api/update-event", {
                method: 'POST',
                credentials: 'include',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken()
                },
                body: JSON.stringify({  event_id: this.dataStore.eventPreviewID,
                                        eventTitle: this.eventTitle, 
                                        Address: this.Address, 
                                        eventDesc: this.eventDesc, 
                                        startDate: this.startDate, 
                                        endDate: this.endDate})
            })
            if (response.ok) {
                //const data = await response.json()
                this.success = 'Event Created successfully'
                    setTimeout(() => {
                    this.$router.push('/organizer-panel')
                    }, 1000)
            } else {
                this.error = data.error || 'Failed to create event'
            }
            
    },
    resetError(){
      this.error = ""
    },
    goToOrganizerPanel(){
      this.$router.push('/organizer-panel')
    }
  }
}
</script>

<style>
  .inline-block-child {
    display: inline-block;
    padding: 0.3rem;
  }
</style>
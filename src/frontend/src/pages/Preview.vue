<template>
    <h1>Event Preview</h1>
    <br>
    <!-- <h3>Event Information:</h3> -->

    <p><b>Event name: </b>{{EventData.data.title}}</p>
    <p><b>Organizer: </b>{{EventData.data.organizer}}</p>
    <p><b>Location: </b>{{EventData.data.location}}</p>
    
    <p><b>Description: </b>{{EventData.data.description}}</p>
    <p><b>Start Time: </b>{{EventData.data.start_time}}</p>
    <p><b>End Time: </b>{{EventData.data.end_time}}</p>
    
    <br>

    <div>
      <div class='inline-block-child'>
        <button type="button" class="btn btn-primary" @click="goToHome">
            << Go back to home page
        </button>
      </div>

      <div class='inline-block-child'>
        <button type="button" class="btn btn-primary" @click="book">
          Book Ticket
        </button>
      </div>
    </div>
  
</template>
  
  
  <script>
  
  import { useAuthStore } from '../store/auth.js'
  import { useDataStore } from '../store/data.js'
  import { useRouter } from 'vue-router'
  import { getEventData } from '../store/data.js'
  import { bookTicket } from '../store/data.js'
  import { onMounted, ref, onBeforeMount} from "vue"
  
  export default {
  
    
    setup() {
      const authStore = useAuthStore()
      const router = useRouter()
      const dataStore = useDataStore()
      var EventData = ref([]);
  
      onBeforeMount(async () => {
        const res = await getEventData(dataStore.eventPreviewID)
        EventData.value = res
      });
  
      return {
        authStore, router, EventData, dataStore
      }
    },
    methods: {
      book(){
        bookTicket(this.dataStore.eventPreviewID)
        this.$router.push('/home')
      },
      goToHome(){
        this.$router.push('/home')
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
import { defineStore } from 'pinia'
import { getCSRFToken } from './auth.js'
//export const dataStore = defineStore('auth', {
 

export const useDataStore = defineStore('data', {
    state: () => {
      const storedState = localStorage.getItem('dataState')
      
      return storedState ? JSON.parse(storedState) : {
        eventPreviewID: 0,
        otherData: ""
        }
    }
    ,
    actions: {
        setSelectedEvent(id, otherData= "") {
            this.eventPreviewID = id
            this.otherData= otherData
            this.saveState()
        },
        saveState() {
            /*
            We save state to local storage to keep the
            state when the user reloads the page.
            */
            localStorage.setItem('dataState', JSON.stringify({
                eventPreviewID: this.eventPreviewID,
                otherData: this.otherData
            }))
        }
    }
  })

export async function getEventsData() {
const response = await fetch("http://localhost:8000/events/api/get-all-events", {
        credentials: 'include',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken()
        }
    })
    if (response.ok) {
        const data = await response.json()
        return(data)
        
    }
    else{
        console.log(response)
        console.log("Unable to get all the event data")
    } 
}


export async function getOrganizerEventsData() {
    const response = await fetch("http://localhost:8000/events/api/get-all-user-organized-events", {
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken()
            }
        })
        if (response.ok) {
            const data = await response.json()
            return(data)
            
        }
        else{
            console.log(response)
            console.log("Unable to get all the event data")
        } 
    }


export async function getEventData(event_id) {
    const response = await fetch("http://localhost:8000/events/api/get-event", {
            method: 'POST',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken()
            },
            body: JSON.stringify({"event_id":event_id })
        })
        if (response.ok) {
            const data = await response.json()
            return(data)
        }
        else{
            console.log(response)
            console.log("Unable to get event data")
        } 
    }



export async function bookTicket(event_id) {
    const response = await fetch("http://localhost:8000/events/api/book-event-ticket", {
            method: 'POST',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken()
            },
            body: JSON.stringify({"event_id":event_id })
        })
        if (response.ok) {
            const data = await response.json()
            return(data)
        }
        else{
            console.log(response)
            console.log("Unable to get event data")
        } 
    }

export async function getTicketsData() {
    const response = await fetch("http://localhost:8000/events/api/get-all-user-tickets", {
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken()
            }
        })
        if (response.ok) {
            const data = await response.json()
            return(data)
            
        }
        else{
            console.log(response)
            console.log("Unable to get all the event data")
        } 
    }
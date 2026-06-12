#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

// 1. The Map Limits
#define TOTAL_PASSENGERS 5
#define TOTAL_SEATS 3

// 2. The Shared Resources & Sync Gear
int seats_remaining = TOTAL_SEATS;
sem_t seat_semaphore;        // Bouncer: Only lets 3 people through
pthread_mutex_t memory_lock; // Security: Protects the 'seats_remaining' integer

// 3. The Thread Function
void* book_ticket(void* arg) {
    int id = *(int*)arg;

    printf("📱 [Passenger %d] Opening the UTS app...\n", id);

    sem_wait(&seat_semaphore);

    pthread_mutex_lock(&memory_lock);
    seats_remaining--;
    printf(" [Passenger %d] Secured a window seat! (Seats left: %d)\n", id, seats_remaining);
    pthread_mutex_unlock(&memory_lock);

    sleep(2);

    pthread_mutex_lock(&memory_lock);
    seats_remaining++;
    printf("🚪 [Passenger %d] Reached Bardhaman. Seat free! (Seats left: %d)\n", id, seats_remaining);
    pthread_mutex_unlock(&memory_lock);

    sem_post(&seat_semaphore);

    return NULL;
}

// 4. Main Server
int main() {
    pthread_t passengers[TOTAL_PASSENGERS];
    int passenger_ids[TOTAL_PASSENGERS];

    printf("🚆 Katwa to Bardhaman Local is ready for booking.\n\n");

    sem_init(&seat_semaphore, 0, TOTAL_SEATS);
    pthread_mutex_init(&memory_lock, NULL);

    for (int i = 0; i < TOTAL_PASSENGERS; i++) {
        passenger_ids[i] = i + 1;
        pthread_create(&passengers[i], NULL, book_ticket, &passenger_ids[i]);
        usleep(100000); 
    }

    for (int i = 0; i < TOTAL_PASSENGERS; i++) {
        pthread_join(passengers[i], NULL);
    }

    sem_destroy(&seat_semaphore);
    pthread_mutex_destroy(&memory_lock);

    printf("\n Journey Complete. All passengers disembarked.\n");
    return 0;
}
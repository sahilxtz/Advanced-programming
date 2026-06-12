#include <stdio.h>
#include <pthread.h>

int squad_kills = 0;

// 1. Initialize the Mutex Lock (The Key)
pthread_mutex_t comms_lock = PTHREAD_MUTEX_INITIALIZER;

void* update_kills(void *arg) {
    for (int i = 0; i < 1000000; i++) {
        
        // 2. Synchronization: Lock the critical section
        // If another thread has the lock, this thread will wait here until it opens.
        pthread_mutex_lock(&comms_lock);   
        
        // CRITICAL SECTION (Protected)
        squad_kills++;                     
        
        // 3. Synchronization: Unlock the critical section
        // Hand the key over to the next thread waiting.
        pthread_mutex_unlock(&comms_lock); 
    }
    return NULL;
}

int main() {
    pthread_t player1, player2;

    printf("Spawning the squad with secure comms...\n");

    pthread_create(&player1, NULL, update_kills, NULL);
    pthread_create(&player2, NULL, update_kills, NULL);

    pthread_join(player1, NULL);
    pthread_join(player2, NULL);

    printf("Final Squad Kills (With Mutex): %d\n", squad_kills);
    printf("Expected Kills: 2000000\n");

    return 0;
}
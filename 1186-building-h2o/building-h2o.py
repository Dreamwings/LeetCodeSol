from threading import Semaphore
from typing import Callable

class H2O:
    def __init__(self):
        # Initialize two semaphores for hydrogen and oxygen.
        # Semaphore for hydrogen starts at 2 since we need two hydrogen atoms.
        self.sem_hydrogen = Semaphore(2)
        # Semaphore for oxygen starts at 0 - it is released when we have two hydrogen atoms.
        self.sem_oxygen = Semaphore(0)


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        # Acquire the hydrogen semaphore.
        self.sem_hydrogen.acquire()
      
        # When this function is called, we output the hydrogen atom.
        # This simulates the release of a hydrogen atom.
        releaseHydrogen()  # Outputs "H"
      
        # If there are no more hydrogen permits available, it means we have two hydrogens.
        # Now we can release oxygen to balance and make an H2O molecule.
        if self.sem_hydrogen._value == 0:
            self.sem_oxygen.release()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        # Acquire the oxygen semaphore.
        self.sem_oxygen.acquire()

        # When this function is called, we output the oxygen atom.
        # This simulates the release of an oxygen atom.
        releaseOxygen()  # Outputs "O"
      
        # After releasing an oxygen, we reset the hydrogen semaphore to 2.
        # This allows two new hydrogen atoms to be processed, starting the cycle over.
        self.sem_hydrogen.release(2)
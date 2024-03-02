#include <iostream>
#include <list>
#include <unordered_map>
#include <fstream>
#include <ctime>
#include <vector>
#include <random>
#include <mutex>
#include <thread>

#define CREATOR_THREAD_COUNT 11

typedef struct {
    int sourceAccountId;
    int destinationAccountId;
    int amount;
    int serialNumber;
} OPERATION;   //Represents a single transaction operation

typedef struct {
    int id;
    int balance;
    int initialBalance;
    std::list<OPERATION> log;
} ACCOUNT; //Holds information about an account

std::unordered_map<int, ACCOUNT> _accounts;
//An unordered map containing account IDs as keys and ACCOUNT structs as values.
// It stores all accounts' information.
std::list<OPERATION> _operations;
//A list to store all transaction operations that occur.
int _nextSerialNumber = 0;
//Tracks the serial number for the next transaction operation.

std::mutex *accountsMutexes;
//An array of mutexes, one for each account
std::mutex operationMutex;
std::mutex serialNumberMutex;
//Mutexes for synchronizing operations and serial number generation respectively.

std::unordered_map<int, ACCOUNT> readAllAccounts(const std::string &filePath) {
    //reads account information from a file and populates the _accounts data structure
    std::unordered_map<int, ACCOUNT> accounts;
    std::ifstream file(filePath);
    ACCOUNT account;
    while (file >> account.id >> account.balance) {
        account.initialBalance = account.balance;
        accounts[account.id] = account;
    }
    return accounts;
}

void printAllOperations() {
    operationMutex.lock();
    for (auto const &operation: _operations) {
        std::cout << "--> OPERATION serial number: " << operation.serialNumber << "-----" << std::endl;
        std::cout << "source account: " << operation.sourceAccountId << std::endl;
        std::cout << "destination account: " << operation.destinationAccountId << std::endl;
        std::cout << "amount: " << operation.amount << std::endl << std::endl;
    }
    operationMutex.unlock();
}

int generateRandomNumberInRange(int min, int max) {
    std::random_device rd;
    std::mt19937 mt(rd());
    std::uniform_int_distribution<int> dist(min, max);
    return dist(mt);
}

void createTransaction() {
    OPERATION operation;
    operation.amount = generateRandomNumberInRange(1, 100);
    int senderAccount = generateRandomNumberInRange(0, _accounts.size() - 1);
    int receiverAccount = generateRandomNumberInRange(0, _accounts.size() - 1);
    while (senderAccount == receiverAccount) {
        receiverAccount = generateRandomNumberInRange(0, _accounts.size() - 1);
    }
    operation.sourceAccountId = senderAccount;
    operation.destinationAccountId = receiverAccount;
    if (operation.sourceAccountId < operation.destinationAccountId){
        accountsMutexes[operation.sourceAccountId].lock();
        accountsMutexes[operation.destinationAccountId].lock();
        if (_accounts[operation.sourceAccountId].balance < operation.amount) {
            accountsMutexes[operation.destinationAccountId].unlock();
            accountsMutexes[operation.sourceAccountId].unlock();
            return;
        }
        serialNumberMutex.lock();
        operation.serialNumber = _nextSerialNumber++;
        serialNumberMutex.unlock();
        _accounts[operation.sourceAccountId].balance -= operation.amount;
        _accounts[operation.sourceAccountId].log.push_back(operation);
        _accounts[operation.destinationAccountId].balance += operation.amount;
        _accounts[operation.destinationAccountId].log.push_back(operation);
        accountsMutexes[operation.sourceAccountId].unlock();
        accountsMutexes[operation.destinationAccountId].unlock();
    } else {
        accountsMutexes[operation.destinationAccountId].lock();
        accountsMutexes[operation.sourceAccountId].lock();
        if (_accounts[operation.sourceAccountId].balance < operation.amount) {
            accountsMutexes[operation.sourceAccountId].unlock();
            accountsMutexes[operation.destinationAccountId].unlock();
            return;
        }
        serialNumberMutex.lock();
        operation.serialNumber = _nextSerialNumber++;
        serialNumberMutex.unlock();
        _accounts[operation.destinationAccountId].balance += operation.amount;
        _accounts[operation.destinationAccountId].log.push_back(operation);
        _accounts[operation.sourceAccountId].balance -= operation.amount;
        _accounts[operation.sourceAccountId].log.push_back(operation);
        accountsMutexes[operation.destinationAccountId].unlock();
        accountsMutexes[operation.sourceAccountId].unlock();
    }
    operationMutex.lock();
    _operations.push_back(operation);
    operationMutex.unlock();
}

bool checkIfOperationFromSourceAccountIsInDestinationAccountLog(OPERATION operation) {
    for (auto const &operationFromLog: _accounts[operation.destinationAccountId].log) {
        if (operationFromLog.serialNumber == operation.serialNumber) {
            return true;
        }
    }
    return false;
}

bool checkIfOperationFromDestinationAccountIsInSourceAccountLog(OPERATION operation) {
    for (auto const &operationFromLog: _accounts[operation.sourceAccountId].log) {
        if (operationFromLog.serialNumber == operation.serialNumber) {
            return true;
        }
    }
    return false;
}

void checkConsistency() {
    bool isConsistent = true;
    for (auto const &account: _accounts) {
        accountsMutexes[account.first].lock();
        //Locks the associated accountsMutexes for each account
        // to prevent concurrent access to the same account's data.
        auto initialBalance = account.second.initialBalance;
        for (auto const &operation: account.second.log) {
            if (operation.sourceAccountId == account.first) {
                initialBalance -= operation.amount;
                isConsistent = checkIfOperationFromSourceAccountIsInDestinationAccountLog(operation);
            } else {
                initialBalance += operation.amount;
                isConsistent = checkIfOperationFromDestinationAccountIsInSourceAccountLog(operation);
            }
        }
        if (initialBalance != account.second.balance) {
            isConsistent = false;
            break;
        }
        accountsMutexes[account.first].unlock();
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
        //Introduces a delay of 100 milliseconds before moving to the next account
        // to simulate processing time and yield the CPU to other threads.
    }
    if (isConsistent) {
        std::cout << "Consistency check passed" << std::endl;
    } else {
        std::cout << "Consistency check failed" << std::endl;
    }
}

int main() {
    std::srand(std::time(nullptr));
    //Seeds the random number generator with the current time
    // to generate random numbers during the program execution.
    _accounts = readAllAccounts(R"(C:\Scoala\AnulIII\PDP\Lab1\accounts.txt)");
    std::thread creatorThreads[CREATOR_THREAD_COUNT];
    accountsMutexes = new std::mutex[_accounts.size()];

    for (int i = 0; i < CREATOR_THREAD_COUNT; i++) {
        //Sets up multiple threads (CREATOR_THREAD_COUNT) to execute the createTransaction function
        // that simulates creating financial transactions.
        creatorThreads[i] = std::thread(createTransaction);
    }
    for (int i = 0; i < CREATOR_THREAD_COUNT; i++) {
        //Runs the transaction threads, and after each set of 6 threads execution,
        // performs a consistency check using the checkConsistency function.
        // This check occurs at intervals of 6 threads.
        creatorThreads[i].join();
        if (i % 6 == 0) {
            checkConsistency();
        }
    }
    std::thread checkerThread(checkConsistency);
    checkerThread.join();
    //Executes a separate thread to perform another consistency check
    // after all initial transaction threads have completed.
    std::thread printerThread(printAllOperations);
    printerThread.join();
    //Runs a thread to print all the operations stored during the transactions.
    delete[] accountsMutexes;
    //Releases the allocated memory for accountsMutexes, likely an array of mutexes
    // used for managing account access in the createTransaction function.
    return 0;

}
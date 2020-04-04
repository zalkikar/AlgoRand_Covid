#!/usr/bin/env python
# coding: utf-8

import algosdk
import math
import time

class Algorand_IReportScrape():
    
    def __init__(self, api_key):
        self.purestake_api_key = api_key
        self.connectMainnet()
        self.client_check()
        
        # For retrieving the real covid data from mainnet
        self.address = "COVIDR5MYE757XMDCFOCS5BXFF4SKD5RTOF4RTA67F47YTJSBR5U7TKBNU"
        self.fromRound = 5646000
        self.maxTxnPerCall = 500 # max transactions in a batch
        self.batchSize = 512 #Read the transactions from the blockchain in 512-block installations
        self.params = self.algod_client.suggested_params()
        self.lastRound = self.params['lastRound']
        #self.lastRound = self.fromRound + 20*self.batchSize # for testing
        
        print("\n total rounds:",self.lastRound - self.fromRound)
        
        self.txns = []
        self.batch_limit = math.ceil((self.lastRound - self.fromRound)/self.maxTxnPerCall)
        
        rnd = self.fromRound
        while rnd < self.lastRound:
            toRnd = rnd + self.batchSize
            if toRnd > self.lastRound:
                toRnd = self.lastRound
            self.txns.extend(self.getTransactionBatch(rnd,toRnd)) # Fetch transactions for these rounds 
            rnd += self.batchSize
            time.sleep(0.1)

        print("found {} transactions".format(len(self.txns)))
                             
    def connectMainnet(self):
        algod_address_mainnet = "https://mainnet-algorand.api.purestake.io/ps1"
        port = ""
        token = {
            'X-API-key' : self.purestake_api_key,
        }
        # Initialize the algod client
        self.algod_client = algosdk.algod.AlgodClient(port, algod_address_mainnet, token) 
    
    def client_check(self):
        try:
            status = self.algod_client.status()
        except Exception as e:
            print("Failed to get algod status: {}".format(e))

        if status:
            print("algod last round: {}".format(status.get("lastRound")))
            print("algod time since last round: {}".format(status.get("timeSinceLastRound")))
            print("algod catchup: {}".format(status.get("catchupTime")))
            print("algod latest version: {}".format(status.get("lastConsensusVersion")))

        # Retrieve latest block information                                                                                                                                               
        last_round = self.algod_client.status().get("lastRound")
        print("####################")
        block = self.algod_client.block_info(last_round)
        print(block)
                             
    def getTransactionBatch(self,fromRnd,lastRnd):
        if (fromRnd > lastRnd):# sanity check
            return []
        txs = self.algod_client.transactions_by_address(self.address,fromRnd,lastRnd,self.maxTxnPerCall) 
        # make an API call to get the transactions - 500 at a time
        return txs['transactions']

        #  A recursive function for getting a batch of transactions, to overcome
        # the limitation of maxTxnPerCall transaction per call to the API
        '''
        # If we got all the transactions, just return them
        if (fromRnd == toRnd | len(txs['transactions']) < maxTxnPerCall):
            return txs['transactions']

            # FIXME: If a single block contains more than maxTxnPerCall
            # transactions for the target address, the code above will return
            # only maxTxnPerCall of them.
            # This is an unlikely case, and not easy to handle. The only way to
            # handle it is to call algod.block(round#), then go over all the
            # transactions in this block and take only the ones corresponding
            # to the target address.

        else: # recursive call to get them in two smaller chunks
            midRnd = math.floor((fromRnd+toRnd) / 2)
            txns1 = getTransactionBatch(fromRnd, midRnd)
            txns2 = getTransactionBatch(midRnd+1, toRnd)
            # return the concatenation of the two chunks
            return txns1.concat(txns2)
        '''
                             
    def get_txns(self):
        return self.txns


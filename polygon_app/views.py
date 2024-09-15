from django.http import JsonResponse
from web3 import Web3

# Your Polygon RPC URL
POLYGON_RPC_URL = "https://rpc.cardona.zkevm-rpc.com/"

def connect_polygon_network(request):
    try:
        # Initialize Web3 connection
        web3 = Web3(Web3.HTTPProvider(POLYGON_RPC_URL))
        
        # Verify connection by checking the latest block number
        try:
            # Fetch the latest block number
            latest_block = web3.eth.get_block('latest')
            block_number = latest_block['number']            
            return JsonResponse({'status': 'success', 'block_number': block_number})
        except Exception as e:
            # Handle exceptions when fetching the block number
            return JsonResponse({'status': 'error', 'message': 'Failed to fetch block number', 'error': str(e)})
    except Exception as e:
        # Handle any exceptions that occur during initialization
        return JsonResponse({'status': 'error', 'message': 'Failed to connect to Polygon network', 'error': str(e)})

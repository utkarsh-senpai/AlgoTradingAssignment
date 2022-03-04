curl --location --request POST 'https://asia-south1-trading-session-manager.cloudfunctions.net/task' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'apiKey=0aa6d29a91b778130aaeb925a7504c9a67d6b7f28c1efd064b61f1077b71463b' \
--data-urlencode 'apiSecret=d3cc55242b9811642ae45701662e038442cfc248aacc171c3855529522c4aec9' \
--data-urlencode 'email=utkarsh.meshram2000@gmail.com'

# Ensure you pass correct email. We will communicate with shortlisted cadidates through this

# Output:
# {
#    isTask1Done: boolean,
#    isTask2Done: boolean,
#    clientIDsReceived: array
# }
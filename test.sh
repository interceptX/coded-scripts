# You can check if the tool is working with
prips 1.0.0.0/30 | hakoriginfinder -h one.one.one.one

# If you know the company is using AWS you could use the previous tool to search the
## web page inside the EC2 IPs
DOMAIN="client-api.arkoselabs.com"
WIDE_REGION=us
for ir in `curl https://ip-ranges.amazonaws.com/ip-ranges.json | jq -r '.prefixes[] | select(.service=="EC2") | select(.region|test("^us")) | .ip_prefix'`; do 
    echo "Checking $ir"
    prips $ir | hakoriginfinder -h "$DOMAIN"
done

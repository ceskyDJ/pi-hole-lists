# Pi-Hole Block Lists

## Risk e-shops (mainly for Czechia)

I parse [website with risk e-shops](https://www.coi.cz/pro-spotrebitele/rizikove-e-shopy/) created and maintained by
the [Czech Trade Inspection Authority](https://www.coi.cz/en/) (CTIA) into Pi-Hole block list using simple Python
script, and release the result block list on my website. It is mainly for Czech people (there are only Czech e-shops),
but anyone can use it in his/her Pi-Hole installation.

If you want to use this block list, use this URL:
```
https://pi-hole-lists.ceskydj.cz/risk-eshops
```

## How to install

It is pretty easy to install any of block lists specified above. Just go step-by-step throw this guide:

1. Open your Pi-Hole admin webpage (http://pi.hole/admin should work in general if you don't modify your configuration,
and you don't use some web proxy as nginx).
2. Go to "Adlists" (in vertical menu on the left).
3. Fill in the block list's URL into to "Address" field and optionally name of the block list into "Comment" field.
4. Click on the "Add" button.
5. Now you need to update your gravity list (cache of DNS entries used by Pi-Hole). So, go to "Tools" --> "Update
Gravity" (in vertical menu on the left).
6. Click on the "Update" button.
7. Wait a second until the updating process is done. You should see "Success!" alert on green background.

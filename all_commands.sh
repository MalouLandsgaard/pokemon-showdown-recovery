#!/bin/sh

# skott pokemon-showdown-master/server/index.ts  --displayMode=json
# python3 script.py skott.json

# Final used commands

# Skott for project dependencies
skott pokemon-showdown  --displayMode=json 
python3 script.py skott.json

# Skott for servers dependencies
skott server/index.ts

# Dependency cruise for the server directory 
depcruise --collapse "^(lib|data|sim|server/tournaments|server/chat-commands|server/chat-plugins|server/private-messages|server/artemis)" --include-only "^(sim|lib|data|server/tournaments|server/chat-commands|server/chat-plugins|server/private-messages|server/artemis|server/index.ts|server/rooms.ts|server/users.ts|server/room-game.ts|server/room-battle.ts|server/chat.ts)"  --output-type dot server/index.ts | dot -T svg > dependencygraph_may16.svg

# Dependency cruise for the modules view
depcruise --collapse "^(lib|data|sim)" --include-only "^(sim|lib|data|server)"  --output-type dot server | dot -T svg > dependencygraph_may15.svg  

# Dependency cruise for HTML view
npx dependency-cruise -T html -f dependencies.html server   

# Git Truck
npx -y git-truck 

# Ts Dependency Graph
npx ts_dependency_graph --start server/index.ts --hotspots  --graph_folder | dot -T svg > dependencygraph2.svg
npx ts_dependency_graph --verbose  --start server/index.ts --graph_folder | dot -T svg > dependencygraph2.svg

# Magde list readable dependencies
madge --json pokemon-showdown-master/server/index.ts | tr '[a-z]' '[A-Z]' | madge --stdin

# Magde debug
madge --image graph.svg pokemon-showdown-master/server/index.ts --debug 

# Magde dependency graph
madge --image graph.svg pokemon-showdown-master/server/index.ts   
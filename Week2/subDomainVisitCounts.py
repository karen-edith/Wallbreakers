from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        # set up visits map and visits array
        visits, visitsArray = {}, []
        # loop throuh cpdomains
        for i in range(len(cpdomains)):
            # split each domain at empty empty spaces this will create a value
            # array and a domain array
            viewsDomainSplit = cpdomains[i].split()
            baseCount = int(viewsDomainSplit[0])
            # split domain at .
            domainSplit = viewsDomainSplit[1].split('.')

            # loop through split domain array
            for j in range(len(domainSplit)):
                # join words split array words to create sub domain strings
                subdomain = '.'.join(domainSplit[j:])
                if subdomain in visits:
                    # if subdomain word already invisits map add basecount value
                    visits[subdomain] = visits[subdomain] + baseCount
                else:
                    # if not already in map, count for subdmoain is base value
                    visits[subdomain] = baseCount

        # place answers in list
        for key, value in visits.items():
            visitsArray.append(str(value) + ' ' + str(key))

        return visitsArray

    '''
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        viewsMap, helperArray, visits, final = defaultdict(int), [], [], []
        string = ''

        for i in range(len(cpdomains)):
            test = cpdomains[i].split(' ')
            viewsMap[test[1]] = int(test[0])
            helperArray.append(test[1])
            visits.append(int(test[0]))

        for j in range(len(helperArray)):
            for k in reversed(range(len(helperArray[j]))):
                if helperArray[j][k] != '.':
                    string = helperArray[j][k] + string
                else:
                    string = '.' + string
                    viewsMap[string] = viewsMap[string] + visits[j]
            string = ''

        for key,value in viewsMap.items():
            if key[0] == '.':
                final.append(str(value) + ' ' + key[1:len(key)])
            else:
                final.append(str(value) + ' ' + key)

        return(final)
    '''

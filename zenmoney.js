waitForKeyElements(('#FilterBlock ul.accountFilter'), accountsLoaded);

function accountsLoaded(jNode) {
    jNode.children().not('.hidden').slice(0, 3).css({
        "background-color": "lawngreen",
        "padding": "2px"
    });
    jNode.children().not('.hidden').slice(3, 4).addClass('borrowed');
    jNode.children().not('.hidden').slice(4, 7).css({
        "background-color": "wheat",
        "padding": "2px"
    });
    jNode.children().not('.hidden').slice(7, 11).css({
        "background-color": "pink",
        "padding": "2px"
    });
    sum = calcBalanceHrv(jNode);
    // TODO: Use templates, Use toggle(show/hide block) link
    jNode.append('<li style="padding: 2px">' +
                   '<span class="balance">' +
                     '<span class="sum">'+sum[0]+'<span class="cent">,'+sum[1]+'</span></span>' +
                     '&nbsp;<span class="symbol">грн</span>' +
                   '</span>' +
                   '<span class="title">Всего, грн</span>' + 
                 '</li>');
}

//TODO: Return JSON as follows
// res = {'account_hrv': {'sum': 0, 'cent': 0}, 'account_usd': {'sum': 0, 'cent': 0}, 'account_euro': {'sum': 0, 'cent': 0}, 'all_hrv': {'sum': 0, 'cent': 0}}
function calcBalanceHrv(jNode) {
    allHrv = 0;
    jNode.children().not('.hidden, .borrowed').each(function() {
        val = parseFloat($(this).find('.sum').text().replace(' ', '').replace(',', '.'));        
        //TODO: Make show/hide for block below
        //jNode.append('<li>' + val.toFixed(2).replace('.', ',') + '</li>');
        symbol = $(this).find('.symbol').text();
        if (symbol == '$') {
            //console.log(val * usdRate);
            allHrv += val * usdRate;
        } else if (symbol == '€') {
            //console.log(val * euroRate);
            allHrv += val * euroRate;
        } else {
            //console.log(val);
            allHrv += val;
        }    
    });
    
    return allHrv.toFixed(2).split('.');
}    

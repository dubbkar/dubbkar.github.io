/*
 * Videojs Plugin for download
 * By: tutorialspots.com
 * Base on Video.js Resolution Selector (https://github.com/dominic-p/videojs-resolution-selector)
 * Thanks for Dominic P
*/
 
(function (_V_) {
 
    var methods = {
        res_label: function (res) {
            return (/^\d+$/.test(res)) ? res + 'p' : res;
        }
    };
 
    _V_.DownloadMenuItem = _V_.MenuItem.extend({
        call_count: 0,
        init: function (player, options) {
            var touchstart = false;
            // Modify options for parent MenuItem class's init.
            options.label = methods.res_label(options.res);
            // Call the parent constructor
            _V_.MenuItem.call(this, player, options);
            // Store the resolution as a property
            this.resolution = options.res;
            // Register our click and tap handlers
            this.on(['click', 'tap'], this.onClick);
        }
    });
 
    // Handle clicks on the menu items
    _V_.DownloadMenuItem.prototype.onClick = function () {
        // Check if this has already been called
        if (this.call_count > 0) {
            return;
        }
        // Call the player.changeDl method
        this.player().changeDl(this.resolution);
        // Increment the call counter
        this.call_count++;
    };
 
 
    _V_.DownloadTitleMenuItem = _V_.MenuItem.extend({
        init: function (player, options) {
            // Call the parent constructor
            _V_.MenuItem.call(this, player, options);
            // No click handler for the menu title
            this.off('click');
        }
    });
 
    _V_.DownloadSelector = _V_.MenuButton.extend({
 
        init: function (player, options) {
            // Add our list of available resolutions to the player object
            player.availableRes = options.available_res;
            // Call the parent constructor
            _V_.MenuButton.call(this, player, options);
            // Set the button text based on the option provided
            this.el().firstChild.firstChild.innerHTML = options.buttonText;
        }
    });
 
    // Set class for resolution selector button
    _V_.DownloadSelector.prototype.className = 'vjs-dl-button';
 
    // Create a menu item for each available resolution
    _V_.DownloadSelector.prototype.createItems = function () {
        var player = this.player(),
            items = [];
        // Add the menu title item
        items.push(new _V_.DownloadTitleMenuItem(player, {
            el: _V_.Component.prototype.createEl('li', {
                className: 'vjs-menu-title vjs-dl-menu-title',
                innerHTML: player.localize('Quality')
            })
        }));
 
        // Add an item for each available resolution
        for (current_res in player.availableRes) {
            // Don't add an item for the length attribute
            if ('length' == current_res) {
                continue;
            }
            items.push(new _V_.DownloadMenuItem(player, {
                res: current_res
            }));
        }
 
        // Sort the available resolutions in descending order
        items.sort(function (a, b) {
            if (typeof a.resolution == 'undefined') {
                return -1;
            } else {
                return parseInt(b.resolution) - parseInt(a.resolution);
            }
        });
 
        return items;
    };
 
    _V_.plugin('DownloadSelector', function (options) {
        // Only enable the plugin on HTML5 videos
        if (!this.el().firstChild.canPlayType) {
            return;
        }
        var player = this,
            sources = player.options().sources,
            i = sources.length,
            available_res = {
                length: 0
            },
            current_res,
            DownloadSelector;
 
        // Get all of the available resolutions
        while (i > 0) {
            i--;
            // Skip sources that don't have data-res attributes
            if (!sources[i]['data-res']) {
                continue;
            }
            current_res = sources[i]['data-res'];
            if (typeof available_res[current_res] !== 'object') {
 
                available_res[current_res] = [];
                available_res.length++;
            }
            available_res[current_res].unshift(sources[i]);
        }
 
        if (typeof player.localize !== 'function') {
            player.localize = function (string) {
                return string;
            };
        }
 
        // Define the change res method
        player.changeDl = function (target_resolution) {
            callback = options.callback || function (a) {
                return a;
            }
            var win = window.open(callback(player.availableRes[target_resolution][0].src), '_blank');
            //var win = window.open(player.availableRes[target_resolution][0].src, '_blank');
            if (win) {
                //Browser has allowed it to be opened
                win.focus();
            } else {
                //Broswer has blocked it
                alert('Please allow popups for this site');
            }
        };
 
        // Add the resolution selector button
        DownloadSelector = new _V_.DownloadSelector(player, {
            buttonText: 'Download',
            available_res: available_res
        });
 
        // Add the button to the control bar object and the DOM
        player.controlBar.DownloadSelector = player.controlBar.addChild(DownloadSelector);
    });
 
})(videojs);
const statusComponent = {
        template: '<a v-for="service in services" :key="service.id">blah</a>',
        methods: {
                checkStatus(site) {
                        axios.get(site).then(function (response) {
                                console.log(response.json);
                                if (response.status == 200) {
                                        console.log("UP");
                                        return;
                                } else {
                                        console.log("DOWN");
                                        return;
                                }
                        }).catch(function (error) {
                                console.log(error.toJSON());
                        });
                },
        },
        data() {
                return {
                        services: [
                                {
                                        name: "Library website",
                                        site: "https://library.kbcc.cuny.edu/homepage",
                                        siteStatus: this.checkStatus("https://library.kbcc.cuny.edu/homepage"),
                                        id: 1,
                                },
                                {
                                        name: "ILLiad",
                                        site: "https://kbcc-cuny.illiad.oclc.org/illiad/logon.html",
                                        siteStatus: this.checkStatus("https://kbcc-cuny.illiad.oclc.org/illiad/logon.html"),
                                        id: 2,
                                },
                                {
                                        name: "dummy",
                                        site: "https://library.kbcc.cuny.edu/fajlfk",
                                        siteStatus: this.checkStatus("https://library.kbcc.cuny.edu/fajlfk"),
                                        id: 3,
                                },
                        ],
                }
        }
};

const app = Vue.createApp({
        components: {"status-component": statusComponent}
}).mount('#app');

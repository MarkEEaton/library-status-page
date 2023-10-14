const statusComponent = {
        template: '<a v-for="service in services" :key="service.id">blah</a>',
        methods: {
                checkStatus(site) {
                        console.log("function!");
                        fetch(site).then(function (response) {
                                if (response.status == 200) {
                                        console.log("UP");
                                        return;
                                } else {
                                        console.log("DOWN");
                                        return;
                                }
                        });
                },
        },
        props: ["services"],
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
                        ],
                }
        }
};

const app = Vue.createApp({
        components: {"status-component": statusComponent}
}).mount('#app');

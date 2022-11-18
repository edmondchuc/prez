import { ref } from "vue";

/**
 * Generic wrapper for an API GET request
 * @returns 
 */
export function useGetRequest() {
    const data = ref("");
    const loading = ref(false);
    const error = ref("");

    /**
     * Executes the API GET request, with success & error callbacks
     * @param {*} url 
     * @param {*} callback 
     * @param {*} errorCallback 
     */
    function doRequest(url, callback = () => {}, errorCallback = () => {}) {
        loading.value = true;

        fetch(url)
        .then(r => {
            if (!r.ok) {
                throw new Error("Response was not OK");
            }
            return r.text();
        })
        .then(text => {
            data.value = text;
            callback();
            loading.value = false;
        })
        .catch(e => {
            error.value = e;
            errorCallback();
            loading.value = false;
        });
    }

    return { data, loading, error, doRequest };
};
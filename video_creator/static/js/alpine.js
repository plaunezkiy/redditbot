document.addEventListener('alpine:init', () => {
    Alpine.data('controls', () => ({
        modalOpen: false,
        videoControls: [
            {
                name: "Post",
                attrs: {
                        name: "Text",
                        value: "Hello there",
                        reload: () => {
                            console.log(self);
                        },
                        preview: () => {
                            return `<p>Hello there</p>`
                        },
                        setPreview :(element) => {
                            setModalContent(element);
                            modalOpen = true;
                        }
                    }
            },
        ],
        setModalContent: (element) => {
            const dialog = document.getElementById("modelDialogContent")
            console.log(dialog);
            console.log(element.preview);
            modalOpen = true;
            return
        }
    }))
})

// [
//     {
//         name: "Text",
//         value: "Hello there",
//         reload: () => {
//             console.log(self);
//         },
//         preview: () => {
//             return `<p>Hello there</p>`
//         },
//         setPreview :(element) => {
//             setModalContent(element);
//             modalOpen = true;
//         },
//     }
// ]
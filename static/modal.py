from browser import document, bind, window

modal_list = document.select('.modal')
if modal_list:
    modal = modal_list[0]
    span = document.select('.close')[0]

    @bind(window, 'click')
    @bind(span, 'click')
    def close_modal(event=None):
        if event.target == span:
            modal.style.display = 'none'
        elif event.target == modal:
            modal.style.display = 'none'
